Relevance

Thus, designing an automatic  MWP solver, with semantic understanding and
 inference capability, has been considered as a crucial step towards general AI. 
 Solving a math problem manually involves too many steps. So MWP will reduc
Attachment final.pdf added.Conversation opened. 1 read message.

Skip to content
Using Gmail with screen readers
jithin 

5 of about 62
Code
Inbox
x

jithin p <jithinappu.p6@gmail.com>
Attachments
Tue, 6 Mar, 23:44
to me

Attachments area

import wx
import MySQLdb
import nltk
import string
from string import punctuation
from nltk.corpus import stopwords
from nltk.corpus import wordnet as w
from wx import grid as gr
from itertools import chain
from nltk.corpus.reader import NOUN
from scipy import spatial
import os
import sys





dbc=''
database_name=''
#natural_query=''
query=''
path=os.path.dirname(os.path.realpath(sys.argv[0]))
class MainWindow(wx.Frame) :
	
	def __init__(self,parent,id) :
		wx.Frame.__init__(self,parent,id,'Natural Query To SQL Translator',size=(500,400))
		panel = wx.Panel(self)
		panel.SetBackgroundColour(wx.Colour(200,200,225))
		font1 = wx.Font(30, wx.DEFAULT, wx.MODERN, wx.FONTWEIGHT_BOLD)
		#name_top = wx.StaticText(panel, -1, "Natural Query To", (42,50), (360,-1),wx.ALIGN_CENTER)
		#name_top.SetFont(font)
		name = wx.StaticText(panel, -1, "Query Translator", (59,50), (360,-1),wx.ALIGN_CENTER)
                name.SetFont(font1)
		font2 = wx.Font(12, wx.DEFAULT, wx.MODERN, wx.FONTWEIGHT_BOLD)
		name.SetForegroundColour('blue')
		translator_button = wx.Button(panel,label="Translator",pos=(160,200),size=(175,60))
		translator_button.SetBackgroundColour(wx.Colour(220,220,230))
		translator_button.SetFont(font2)
		self.Bind(wx.EVT_BUTTON, self.translating_window, translator_button)
		#self.Bind(wx.EVT_BUTTON, self.database_window, translator_button)
		statusbar = self.CreateStatusBar()
		menubar = wx.MenuBar()
		first = wx.Menu()
		second = wx.Menu()
		first.Append(wx.NewId(),"New Window","This is new window")
		second.Append(wx.NewId(),"Open...","Open new window")
		menubar.Append(first,"File")
		menubar.Append(second,"Edit")
		self.SetMenuBar(menubar)


	'''
	def databse_window(self,event):
		dtbase_window = create_databse_window(parent=None,id=-1)
		dtbase_window.Show()
	'''


	
	def translating_window(self,event):
		translate_window = create_translate_window(parent=None,id=-1)
		translate_window.Show()
	



'''
class create_databse_window(wx.Frame) :
	def __init__(self,parent,id) :
		wx.Frame.__init__(self,parent,id,'Query Translator',size=(500,300))
		self.panel = wx.Panel(self)
                self.panel.SetBackgroundColour(wx.Colour(200,200,225))
                font = wx.Font(12, wx.DEFAULT, wx.DEFAULT, wx.FONTWEIGHT_NORMAL)
		self.database_name = wx.StaticText(self.panel, -3, "Database Name", (42,85), (360,-1))
		self.database_name.SetFont(font)
		self.database_name_text = wx.TextCtrl(self.panel, -1, "", pos=(200,75), size=(400,42))
                self.natural_query_text.SetInsertionPoint(0)
'''		

	 


	
class create_translate_window(wx.Frame) :
	global dbc
	global database_name
	global natural_query
	global query
	def __init__(self,parent,id) :
		wx.Frame.__init__(self,parent,id,'Query Translator',size=(650,600))
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour(wx.Colour(200,200,225))
		font = wx.Font(12, wx.DEFAULT, wx.DEFAULT, wx.FONTWEIGHT_NORMAL)
		database_connect_button = wx.Button(self.panel, label="Connect", pos=(262,50), size=(120,40))
                database_connect_button.SetFont(font)
		self.Bind(wx.EVT_BUTTON, self.connect_database, database_connect_button)
		database_button = wx.Button(self.panel, label="Select Database", pos=(250,130), size=(150,40))
		database_button.SetFont(font)
		self.Bind(wx.EVT_BUTTON, self.select_database, database_button)
		self.selected_dtname = wx.StaticText(self.panel, -3, "Database", (42,215), (360,-1))
		self.selected_dtname.SetFont(font)
		self.sel_dtname = wx.TextCtrl(self.panel, -1, pos=(207,210), size=(250,-1))
                self.sel_dtname.SetInsertionPoint(0)
		self.natural_query = wx.StaticText(self.panel, -3, "English query", (42,290), (360,-1))
		self.natural_query.SetFont(font)
		self.natural_query_text = wx.TextCtrl(self.panel, -1, pos=(185,280), size=(300,42), style=wx.TE_MULTILINE)
		self.natural_query_text.SetInsertionPoint(0)
		generate_button = wx.Button(self.panel, label="Generate", pos=(265,360), size=(120,40))
		generate_button.SetFont(font)
		self.Bind(wx.EVT_BUTTON, self.generate_query, generate_button)
		self.sql_query = wx.StaticText(self.panel, -3, "SQL query", (42,450), (360,-1))
		self.sql_query.SetFont(font)
		self.sql_query_text = wx.TextCtrl(self.panel, -1, pos=(185,440), size=(300,42), style=wx.TE_MULTILINE)
		self.sql_query_text.SetInsertionPoint(0)
		result_button = wx.Button(self.panel, label="Result", pos=(265,519), size=(120,40))
                result_button.SetFont(font)
		self.Bind(wx.EVT_BUTTON, self.show_result, result_button)
		





	def connect_database(self,event):
		global dbc
		try:
			self.dbc=MySQLdb.connect("localhost","root","")
			dbc=self.dbc
			#print dbc
			box=wx.MessageDialog(None,"Connection Established",'Alert',wx.OK)
			ans=box.ShowModal()
        		box.Destroy()
		except:
			box=wx.MessageDialog(None,"Error occured while establishing connection",'Alert',wx.OK)
                        ans=box.ShowModal()
                        box.Destroy()



	#def generate_query(self,event):
	#	t=self.natural_query_text.GetValue()
	#	print t



	def select_database(self,event):
		#lobal dbc
		try:
			temp=self.dtbase_window.GetSize()
		except:
			self.dtbase_window = self.create_databse_window(parent=None,id=1)
                	self.dtbase_window.Show()
			self.dtbase_window.Bind(wx.EVT_CLOSE,self.addDatabase,self.dtbase_window)
			#print dbc







	def addDatabase(self,event):
		try:
			global database_name
			#print database_name
			self.dt_name=database_name
			self.sel_dtname.SetValue(self.dt_name)
			self.dtbase_window.Destroy()
		except:
			self.dtbase_window.Destroy()





	def generate_query(self,event):
		global query
		self.n_query_feature_file=[]
		#global natural_query
		#print "hdgfhgf"
        	t=self.natural_query_text.GetValue()
		self.natural_queryy=t
        	#print self.natural_queryy
		self.n_query_feature_file.append(feature(self.natural_queryy))
		#print self.n_query_feature_file
		for f in self.n_query_feature_file:
			f.extract_feature()
			f.csv_file()
			f.mapping()
		print "query"
		print query
		self.queryy=query
		if len(self.queryy) != 0:
			self.sql_query_text.SetValue(self.queryy)
	
	
	
	
	def show_result(self,event):
		#global query
		try:
                        temp=self.reslt_window.GetSize()
                except:
                        self.reslt_window = self.create_result_window(parent=None,id=1)
                        self.reslt_window.Show()
                        #self.reslt_window.Bind(wx.EVT_CLOSE,self.addDatabase,self.dtbase_window)

		
			


	
	



	class create_databse_window(wx.Frame):
		global dbc
		global database_name
		def __init__(self,parent,id) :
                	wx.Frame.__init__(self,parent,id,'Select Database',size=(590,350))
                	self.panel = wx.Panel(self)
                	self.panel.SetBackgroundColour(wx.Colour(200,200,225))
                	font = wx.Font(12, wx.DEFAULT, wx.DEFAULT, wx.FONTWEIGHT_NORMAL)
			self.sel_dtbase = wx.StaticText(self.panel, -3, "Select Database", (42,100), (360,-1))
                	self.sel_dtbase.SetFont(font)
			self.dt_choice=wx.Choice(self.panel,-1,pos=(190,95),size=(250,30))
			self.dt_choice.SetSelection(0)
			refresh_button = wx.Button(self.panel, label="Refresh", pos=(450,95), size=(90,30))
                	refresh_button.SetFont(font)
			self.Bind(wx.EVT_BUTTON, self.list_dt_base, refresh_button)
			select_button = wx.Button(self.panel, label="Select", pos=(250,200), size=(95,30))
                        select_button.SetFont(font)
			self.Bind(wx.EVT_BUTTON, self.database_return, select_button)
			
			#t = self.dt_choice.GetSelection()
			#print t
			#print dbc





		
		def list_dt_base(self,event):
			global dbc
			global database_name
			#try:
			self.list_dtnames=[]
			self.dbc=dbc
			#print dbc
			cursor=self.dbc.cursor()
			cursor.execute("SHOW DATABASES")
			self.dt_names=cursor.fetchall()
			#print self.dt_names
			for i in self.dt_names:
			#cursor.execute("DESC "+i[0])
				name_t=i[0]
				#t=(i[0],det)
				self.list_dtnames.append(name_t)
				#self.dt_choice.SetItems(name_t)
			#database_name=self.list_dtnames
			self.dt_choice.SetItems(self.list_dtnames)
			#print self.list_dtnames
			#except:
			#	box=wx.MessageDialog(None,"Error occured. Connect database",'Alert',wx.OK)
                        #	ans=box.ShowModal()
                        #	box.Destroy()





		def database_return(self,event):
			try:
				global dbc
				global database_name
				self.dbc=dbc
				t = self.dt_choice.GetSelection()
				#print self.list_dtnames[t]
				cursor=self.dbc.cursor()
                        	cursor.execute("USE "+self.list_dtnames[t])
				dt_choose=cursor.fetchall()
				print dt_choose
				database_name=self.list_dtnames[t]
				#self.sel_dtname.SetValue(database_name)
				self.Close()
			except:
				box=wx.MessageDialog(None,"Database no longer exist. Hit the refresh button",'Alert',wx.OK)
                               	ans=box.ShowModal()
                               	box.Destroy()




	class create_result_window(wx.Frame):
		global dbc
                global database_name
		global query
                def __init__(self,parent,id) :
			wx.Frame.__init__(self,parent,id,'Result',size=(500,600))
                        self.panel = wx.Panel(self)
                        self.panel.SetBackgroundColour(wx.Colour(200,200,225))
                        font = wx.Font(12, wx.DEFAULT, wx.DEFAULT, wx.FONTWEIGHT_NORMAL)
			self.queryy=query
			self.dbc=dbc
			attribute_name=[]
			t=self.queryy.split(' ')
			tt=[]
			for i in t:
				tt.append(i.split(','))
			print tt
			for i in range(len(tt)):
				if 'FROM' in tt[i]:
					s=i
			#s=tt.index('FROM')
			#if len(tt) > 0:
			#for i in range(len(tt)):
			#	attribute_name.append(tt[i])
			#else:
			for i in tt[1:s]:
				for j in i:
					attribute_name.append(j)
			if '*' in attribute_name:
				cursor=self.dbc.cursor()
				cursor.execute("DESC "+tt[s+1][0])
				det=cursor.fetchall()
				attribute_name=[]
				for i in range(len(det)):
					attribute_name.append(det[i][0])
			
			#try:
			cursor=self.dbc.cursor()
			cursor.execute(self.queryy)
			result=cursor.fetchall()
			print result
			n_rows=len(result)
			n_cols=len(result[0])
			table=gr.Grid(self.panel, -1, size=(500,600))
			#print attribute_name
			table.CreateGrid(n_rows,n_cols)
			for i in range(len(attribute_name)):
				table.SetColLabelValue(i,attribute_name[i])

			for i in range(len(result)):
				for j in range(len(result[i])):
					table.SetCellValue(i,j,str(result[i][j]))
			#except:
			#print "grid error"
				
				
			
			








class feature():
	global dbc
	global database_name
	global query
	def __init__(self,query):
		self.natural_query=query
		self.token=nltk.tokenize.word_tokenize(self.natural_query)
		print self.token



	


	def extract_feature(self):
		global query
		self.natural_query_features=[]
		self.list1=self.token


		#Removing punctuations
		remov_p=[]
		for i in self.list1:
			if i in punctuation:
				remov_p.append(self.list1.index(i))
		remov_p.reverse()
		for j in remov_p[:]:
			#print j
			del(self.list1[j])
		#print self.list2
		self.featuress=self.list1
		#print self.featuress

		
		#word co-occurrence matrix
		self.occurr=[]
		self.words=[]
		self.list2=self.featuress
		for i in self.list2:
			if i not in self.words:
				self.words.append(i)
		
		w=5
		#self.list4 = self.list3
		self.occurr_val=[]
		for i in range(len(self.list2)):
			self.occurr=[0 for x in range(len(self.words)+1)]
			self.occurr[0]=self.list2[i]
			j=i
			#while (j+w) <= (len(self.list1)-1):
			if (j+w+1) <= (len(self.list2)-1):
				j=j+w+1
			else:
				j=len(self.list2)
			#print "j"
			#print j
			
			for k in range(i+1,j):
				#print "i"
				#print i
				#self.occurr_val.append(self.occurr)
				self.word=self.list2[k]
				try:
					for p in range(len(self.words)):
						if self.words[p] == self.list2[i]:
							ind_row_word=p

					if self.list2[k] == self.list2[i]:
	                                       	occ=w-(k-i-1)
                    		        	ind=self.words.index(self.word)
                        	               	#self.occurr[ind]+=occ
						self.occurr_val[ind_row_word][ind+1]+=occ
					else:
                                        	occ=w-(k-i-1)
                                        	#print k
                                       		ind=self.words.index(self.word)
                                       		#self.occurr[ind]+=occ
						self.occurr_val[ind_row_word][ind+1]+=occ
				
				except:
					if self.list2[k] == self.list2[i]:
						occ=w-(k-i-1)
						ind=self.words.index(self.word)
						self.occurr[ind+1]+=occ
						
				
					#if k+1 > j-1:
					#	self.occurr[k]+=0
					else:
						occ=w-(k-i-1)
						#print k
						ind=self.words.index(self.word)
						self.occurr[ind+1]+=occ
						#self.occurr_val.append(self.occurr)
						#print self.words[i]
			
			if len(self.occurr_val) != len(self.words):
				self.occurr_val.append(self.occurr)
			
			print self.occurr_val

			
		#Postagging
		self.list3=self.featuress
		tagged_string=nltk.pos_tag(self.list3)
		self.featuress=tagged_string
                print self.featuress


		#Noun clause extracting
		self.noun_clause_list=[]
		self.list4=self.featuress
		for i in range(len(self.list4)):
			if self.list4[i][1] == 'NN' or self.list4[i][1] == 'NNS':
				self.noun_clause_list.append(self.list4[i][0])
		print self.noun_clause_list

		'''
		#Removing stopwords
		self.list5=self.featuress
                remov_s=[]
                stop_words = set(stopwords.words('english'))
                for i in range(len(self.list5)):
                        if self.list5[i][0] in stop_words:
                                remov_s.append(i)
		#print remov_s
                remov_s.reverse()
		#print remov_s
                for j in range(len(remov_s)):
                        #print self.list4
			t=remov_s[j]
			#print self.list5[t]
                        del(self.list5[t])
                #print self.list5
                self.featuress=self.list5
		print self.featuress
		'''
		
		#Finding Cosine-similarity of noun-pro noun
		self.list6=self.featuress
		self.list7=self.occurr_val
		self.list_pro_noun=[]
		#self.temp_occ_val=[]
		self.occ_values_n_p=[]
		for i in range(len(self.list6)):
			self.list_noun=[]
			if self.list6[i][1] == 'NN' or self.list6[i][1] == 'NNS':
				ind=self.words.index(self.list6[i][0])
				for j in self.list7[ind][1:]:
					self.list_noun.append(j)	
				for k in self.list7:
					self.list_noun.append(k[ind+1])
				#print self.list_noun
				for j in range(i+1,len(self.list6)):
					self.temp_occ_val=[]
				#self.list_pro_noun=[]
					if self.list6[j][1] == 'NNP':
						ind1=self.words.index(self.list6[j][0])
						for l in self.list7[ind1][1:]:
							self.list_pro_noun.append(l)
						for m in self.list7:
							self.list_pro_noun.append(m[ind1+1])
						#print self.list_pro_noun
						#self.list_pro_noun=[]
						occ_value=1-spatial.distance.cosine(self.list_noun,self.list_pro_noun)
						self.temp_occ_val.append(self.list6[i][0])
						self.temp_occ_val.append(self.list6[j][0])
						self.temp_occ_val.append(occ_value)
						#print occ_value
						self.list_pro_noun=[]
					self.occ_values_n_p.append(self.temp_occ_val)
		self.occ_values_n_p.sort()
		#Remove empty lists
		del_list=[]
		#self.occ_values_n_p
		for i in range(len(self.occ_values_n_p)):
			if len(self.occ_values_n_p[i]) == 0:
				del_list.append(i)
		del_list.reverse()
		for j in del_list[:]:
			print del_list
			del(self.occ_values_n_p[j])
		#self.occ_values_n_p.sort(reverse=True)
		#Sorting the list
                sort_t=[]
                sort_tt=self.occ_values_n_p
                self.occ_values_n_p=[]
                for i in sort_tt:
                        sort_t.append(i[2])
                sort_t.sort(reverse=True)
                for i in sort_t:
                        for j in sort_tt:
                                if i == j[2]:
                                        self.occ_values_n_p.append(j)

		print self.occ_values_n_p


		#Finding cosine similarity of verb-noun
		self.list8=self.featuress
                self.list9=self.occurr_val
                #self.list_noun=[]
                self.list_noun1=[]
                #self.temp_occ_val=[]
                self.occ_values_v_n=[]
                for i in range(len(self.list8)):
			self.list_verb=[]
                        if self.list8[i][1] == 'VB' or self.list8[i][1] == 'VBP':
                                ind=self.words.index(self.list8[i][0])
                                for j in self.list9[ind][1:]:
                                        self.list_verb.append(j)
                                for k in self.list9:
                                        self.list_verb.append(k[ind+1])
                                #print self.list_verb
                                for j in range(i+1,len(self.list8)):
                                        self.temp_occ_val=[]
                                #self.list_pro_noun=[]
					if self.list8[j][1] == 'NN' or self.list8[j][1]=='NNS' or self.list8[j][1]=='NNP':
                                                ind1=self.words.index(self.list8[j][0])
                                                for l in self.list9[ind1][1:]:
                                                        self.list_noun1.append(l)
                                                for m in self.list9:
                                                        self.list_noun1.append(m[ind1+1])
                                                #print self.list_noun1
                                                #self.list_pro_noun=[]
                                                occ_value=1-spatial.distance.cosine(self.list_verb,self.list_noun1)
                                                self.temp_occ_val.append(self.list8[i][0])
                                                self.temp_occ_val.append(self.list8[j][0])
                                                self.temp_occ_val.append(occ_value)
                                                #print self.temp_occ_val
                                                self.list_noun1=[]
                                	self.occ_values_v_n.append(self.temp_occ_val)
		self.occ_values_v_n.sort()
		#Remove empty lists
                del_list=[]
                for i in range(len(self.occ_values_v_n)):
                        if len(self.occ_values_v_n[i]) == 0:
                                del_list.append(i)
		del_list.reverse()
                for j in del_list:
                	del(self.occ_values_v_n[j])

		#self.occ_values_v_n.sort(reverse=True)
		#Sorting the list
                sort_t=[]
                sort_tt=self.occ_values_v_n
                self.occ_values_v_n=[]
                for i in sort_tt:
                        sort_t.append(i[2])
                sort_t.sort(reverse=True)
                for i in sort_t:
                        for j in sort_tt:
                                if i == j[2]:
                                        self.occ_values_v_n.append(j)

                print self.occ_values_v_n


		#Finding cosine-similarity of noun-number
		self.list10=self.featuress
                self.list11=self.occurr_val
                #self.list_noun=[]
                self.list_number=[]
                #self.temp_occ_val=[]
                self.occ_values_n_num=[]
                for i in range(len(self.list10)):
			self.list_noun2=[]
                        if self.list10[i][1] == 'NN' or self.list10[i][1] == 'NNS':
                                ind=self.words.index(self.list10[i][0])
                                for j in self.list11[ind][1:]:
                                        self.list_noun2.append(j)
                                for k in self.list11:
                                        self.list_noun2.append(k[ind+1])
                                #print self.list_noun
                                for j in range(i+1,len(self.list10)):
                                        self.temp_occ_val=[]
                                #self.list_pro_noun=[]
					if self.list10[j][1] == 'CD':
                                                ind1=self.words.index(self.list10[j][0])
                                                for l in self.list11[ind1][1:]:
                                                        self.list_number.append(l)
                                                for m in self.list11:
                                                        self.list_number.append(m[ind1+1])
                                                #print self.list_pro_noun
                                                #self.list_pro_noun=[]
                                                occ_value=1-spatial.distance.cosine(self.list_noun2,self.list_number)
                                                self.temp_occ_val.append(self.list10[i][0])
                                                self.temp_occ_val.append(self.list10[j][0])
                                                self.temp_occ_val.append(occ_value)
                                                #print occ_value
                                                self.list_number=[]
                                        self.occ_values_n_num.append(self.temp_occ_val)
		self.occ_values_n_num.sort()
		#Remove empty lists
                del_list=[]
                for i in range(len(self.occ_values_n_num)):
                        if len(self.occ_values_n_num[i]) == 0:
                                del_list.append(i)
		del_list.reverse()
                for j in del_list:
                	del(self.occ_values_n_num[j])

		#self.occ_values_n_num.sort(reverse=True)
		#Sorting the list
                sort_t=[]
                sort_tt=self.occ_values_n_num
                self.occ_values_n_num=[]
                for i in sort_tt:
                        sort_t.append(i[2])
                sort_t.sort(reverse=True)
                for i in sort_t:
                        for j in sort_tt:
                                if i == j[2]:
                                        self.occ_values_n_num.append(j)

                print self.occ_values_n_num
		
		#Find cosine-similarity of noun-noun
		self.list12=self.featuress
                self.list13=self.occurr_val
                #self.list_nounN=[]
                self.list_nounn=[]
                #self.temp_occ_val=[]
                self.occ_values_n_n=[]
                for i in range(len(self.list12)):
                        self.list_noun3=[]
                        if self.list12[i][1] == 'NN' or self.list12[i][1] == 'NNS':
                                ind=self.words.index(self.list12[i][0])
                                for j in self.list13[ind][1:]:
                                        self.list_noun3.append(j)
                                for k in self.list13:
                                        self.list_noun3.append(k[ind+1])
                                #print self.list_noun
                                for j in range(i+1,len(self.list12)):
                                        self.temp_occ_val=[]
                                #self.list_pro_noun=[]
                                        if self.list12[j][1] == 'NN' or self.list12[j][1] == 'NNS':
                                                ind1=self.words.index(self.list12[j][0])
                                                for l in self.list13[ind1][1:]:
                                                        self.list_nounn.append(l)
                                                for m in self.list13:
                                                        self.list_nounn.append(m[ind1+1])
						occ_value=1-spatial.distance.cosine(self.list_noun3,self.list_nounn)
                                                self.temp_occ_val.append(self.list12[i][0])
                                                self.temp_occ_val.append(self.list12[j][0])
                                                self.temp_occ_val.append(occ_value)
                                                #print self.temp_occ_val
                                                self.list_nounn=[]
                                        self.occ_values_n_n.append(self.temp_occ_val)
		
		self.occ_values_n_n.sort()
                #Remove empty lists
                del_list=[]
                for i in range(len(self.occ_values_n_n)):
                        if len(self.occ_values_n_n[i]) == 0:
                                del_list.append(i)
                del_list.reverse()
                for j in del_list:
                	del(self.occ_values_n_n[j])

		#self.occ_values_n_n.sort(reverse=True)
		#Sorting the list
                sort_t=[]
                sort_tt=self.occ_values_n_n
                self.occ_values_n_n=[]
                for i in sort_tt:
                        sort_t.append(i[2])
                sort_t.sort(reverse=True)
                for i in sort_t:
                        for j in sort_tt:
                                if i == j[2]:
                                        self.occ_values_n_n.append(j)

                print self.occ_values_n_n

		#Find cosine values of wh-noun
		self.list15=self.featuress
                self.list16=self.occurr_val
		self.list_Noun=[]
                #self.temp_occ_val=[]
                self.occ_values_w_n=[]
		for i in range(len(self.list15)):
                        self.list_wh=[]
                        if self.list15[i][1] == 'WDT' or self.list15[i][1] == 'WP' or self.list15[i][1] == 'WP$' or self.list15[i][1] == 'WRB':
                                ind=self.words.index(self.list15[i][0])
                                for j in self.list16[ind][1:]:
                                        self.list_wh.append(j)
                                for k in self.list16:
                                        self.list_wh.append(k[ind+1])
                                #print self.list_noun
				for j in range(i+1,len(self.list15)):
                                        self.temp_occ_val=[]
                                #self.list_pro_noun=[]
                                        if self.list15[j][1] == 'NN' or self.list15[j][1] == 'NNS' or self.list15[j][1] == 'NNP':
                                                ind1=self.words.index(self.list15[j][0])
                                                for l in self.list16[ind1][1:]:
                                                        self.list_Noun.append(l)
                                                for m in self.list16:
                                                        self.list_Noun.append(m[ind1+1])
						occ_value=1-spatial.distance.cosine(self.list_wh,self.list_Noun)
                                                self.temp_occ_val.append(self.list15[i][0])
                                                self.temp_occ_val.append(self.list15[j][0])
                                                self.temp_occ_val.append(occ_value)
                                                #print self.temp_occ_val
                                                self.list_Noun=[]
                                        self.occ_values_w_n.append(self.temp_occ_val)
		self.occ_values_w_n.sort()
                #Remove empty lists
                del_list=[]
                for i in range(len(self.occ_values_w_n)):
                        if len(self.occ_values_w_n[i]) == 0:
                                del_list.append(i)
                del_list.reverse()
                for j in del_list:
                        del(self.occ_values_w_n[j])
		#self.occ_values_w_n.sort(reverse=True)
                #print self.occ_values_w_n
		
		#Sorting the list
		sort_t=[]
		sort_tt=self.occ_values_w_n
		self.occ_values_w_n=[]
		for i in sort_tt:
			sort_t.append(i[2])
		sort_t.sort(reverse=True)
		for i in sort_t:
			for j in sort_tt:
				if i == j[2]:
					self.occ_values_w_n.append(j)
		print self.occ_values_w_n
					
					
		
		







		
		
		
		

	def mapping(self):
		global dbc
		global database_name
		global query
		self.dbc=dbc
		self.table_names=[]
		name_synonyms=[]
		syn_set=[]
		syn_set_noun_t=[]
		self.extract_table_name=[]
		self.table_names_t=[]
		syn_set_table_t=[]
		self.lower_noun=[]
		syn_set_table=[]
		self.maped_table_names=[]
		self.query=[]
		self.select_clause='SELECT'
		self.from_clause='FROM'
		self.where_clause=''
		self.nouns=self.noun_clause_list
		cursor=self.dbc.cursor()
                cursor.execute("SHOW TABLES")
                table_name=cursor.fetchall()
		#print table_name

		#Finding table names
		for i in range(len(table_name)):
			self.table_names.append(table_name[i][0])
		print self.table_names
		
		table_det=[]
		cursor=self.dbc.cursor()
		for i in range(len(self.table_names)):
			cursor.execute("DESC "+self.table_names[i])
			det=cursor.fetchall()
			t=(self.table_names[i],det)
			table_det.append(t)
		print table_det
		'''
		#Finding synonyms and tables
		for i in range(len(self.nouns)):
			if self.nouns[i] not in self.table_names:
				syns=w.synsets(self.nouns[i])
				#print syns
				#print syns[0].name()
				for j in syns:
					syn_set=list(chain.from_iterable([j.lemma_names()]))
				#print syn_set
				for k in range(len(syn_set)):
					if syn_set[k] in self.table_names:
						self.extract_table_name.append(syn_set[k])
						#print "found"
		'''
		#Converting to lower case
		for i in range(len(self.table_names)):
			l_name=self.table_names[i].lower()
			self.table_names_t.append(l_name)
		
		for j in range(len(self.nouns)):
                        l_noun=self.nouns[j].lower()
                        self.lower_noun.append(l_noun)

		for i in range(len(self.table_names_t)):
			syns_table=w.synsets(self.table_names_t[i],NOUN)
			syn_set_table_t=[]
			for j in syns_table:
                        	syn_set_table_t.append(list(chain.from_iterable([j.lemma_names()])))
			syn_set_table.append(syn_set_table_t)
		#print syn_set_table
			

		#print self.table_names_t
		#Finding synonyms and tables
                for i in range(len(self.lower_noun)):
			#lower_case_name=self.noun[i].lower()
                        if self.lower_noun[i] not in self.table_names_t:
                                syns_noun=w.synsets(self.nouns[i],NOUN)
                                #print syns
                                #print syns[0].name()
                                for j in syns_noun:
                                        syn_set_noun=list(chain.from_iterable([j.lemma_names()]))
                                	print syn_set_noun
                                	for k in range(len(syn_set_noun)):
						for l in range(len(syn_set_table)):
							for m in range(len(syn_set_table[l])):
                                        			if syn_set_noun[k] in syn_set_table[l][m]:
									try:
										self.noun_table=self.lower_noun[i]
										self.extract_table_name.append(self.table_names[l])
										#print self.table_names[l]
							#print self.extract_table_name
                                        	        			#print "found"
									except:
										pass
			else:
				self.noun_table=self.lower_noun[i]
				ind=self.table_names_t.index(self.lower_noun[i])
				self.extract_table_name.append(self.table_names[ind])
		#print self.extract_table_name
		for i in self.extract_table_name:
			if i not in self.maped_table_names:
				self.maped_table_names.append(i)
		#print self.maped_table_names
		#print self.noun_table
		
		#Attribute mapping
		syn_set_attribute=[]
		table_attr=[]
		self.extract_table_attr=[]
		self.mapped_attr=[]
		self.list14=[]
		self.from_clause+=' '
                self.from_clause+=self.maped_table_names[0]
		if len(self.maped_table_names) == 1:
			'''
			self.list14=self.featuress
			for i in range(len(self.list14)):
				if self.list14[i][1] == 'WDT' or self.list14[i][1] == 'WP' or self.list14[i][1] == 'WP$' or self.list14[i][1] == 'WRB':
					attribute_name=self.occ_values_w_n[0][1]
					for i in table_det:
                                        	if i[0] == self.maped_table_names[0]:
                                 	        	for j in i[1]:
                                                       		table_attr.append(j[0])
                                                               	#print table_attr
                                                                syns_attribute=w.synsets(j[0],NOUN)
                                                      	        syn_set_attribute_t=[]
                                                                for k in syns_attribute:
                                                     			syn_set_attribute_t.append(list(chain.from_iterable([k.lemma_names()])))
                                                         	syn_set_attribute.append(syn_set_attribute_t)
                                                                #print syn_set_attribute
                                                       	attr_l=attribute_name.lower()
                                                        if attr_l not in table_attr:
                                                        	syns_attr=w.synsets(attr_l,NOUN)
                                                                for k in syns_attr:
                                                                syn_set_attr=list(chain.from_iterable([k.lemma_names()]))
                                                                #print syn_set_attr
								for l in range(len(syn_set_attr)):
                                                                	for m in range(len(syn_set_attribute)):
                                                                        	for n in range(len(syn_set_attribute[m])):
                                                                                	#print syn_set_attr[l]
                                                                                        #print syn_set_attribute[m][n]
                                                                                        if syn_set_attr[l] in syn_set_attribute[m][n]:
                                                                                        	#print syn_set_attribute[m][n]
                                                                                                #print m
                                                                                                try:
                                                                                                	self.extract_table_attr.append(table_attr[m])
                                                                                        	except:
													pass
					for i in self.extract_table_attr:
                                        	if i not in self.mapped_attr:
                                                	self.mapped_attr.append(i)
                                        print self.mapped_attr
					self.where_clause+=' '
                                        self.where_clause+=self.mapped_attr[0]
					self.where_clause+='='
					self.where_clause=self.where_clause+"'"+self.list14[i+1][1]+"'"
			'''	

	
			#attribute_name=self.occ_values_v_n[0][1]
                                #self.select_clause+=self.self.occ_values_v_n[0]
                        #print attribute_name
			
			#self.from_clause+=' '
			#self.from_clause+=self.maped_table_names[0]
			#Converting to lower case
			try:
				self.list14=self.featuress
                        	for wh in range(len(self.list14)):
                                	if self.list14[wh][1] == 'WDT' or self.list14[wh][1] == 'WP' or self.list14[wh][1] == 'WP$' or self.list14[wh][1] == 'WRB':
						self.where_clause+='WHERE'
                                        	attribute_name=self.occ_values_w_n[0][1]
						print "attribute_name"
						print attribute_name
                                        	for i in table_det:
                                                	if i[0] == self.maped_table_names[0]:
                                                        	for j in i[1]:
                                                                	table_attr.append(j[0])
                                                                	#print table_attr
                                                                	syns_attribute=w.synsets(j[0],NOUN)
                                                                	syn_set_attribute_t=[]
                                                               		for k in syns_attribute:
                                                                     		syn_set_attribute_t.append(list(chain.from_iterable([k.lemma_names()])))
                                                                	syn_set_attribute.append(syn_set_attribute_t)
                                                                	print syn_set_attribute
                                                        	attr_l=attribute_name.lower()
                                                        	if attr_l not in table_attr:
                                                                	syns_attr=w.synsets(attr_l,NOUN)
                                                                	for k in syns_attr:
                                                                		syn_set_attr=list(chain.from_iterable([k.lemma_names()]))
                                                                	print syn_set_attr
                                                               		for l in range(len(syn_set_attr)):
                                                                        	for m in range(len(syn_set_attribute)):
                                                                                	for n in range(len(syn_set_attribute[m])):
                                                                                        	#print syn_set_attr[l]
                                                                                        	#print syn_set_attribute[m][n]
                                                                                        	if syn_set_attr[l] in syn_set_attribute[m][n]:
                                                                                                	#print syn_set_attribute[m][n]
                                                                                                	#print m
                                                                                                	try:
                                                                                                        	self.extract_table_attr.append(table_attr[m])
                                                                                                	except:
                                                                                                        	pass
							
						for i in self.extract_table_attr:
							#print i
							#print self.mapped_attr
                                                	if i not in self.mapped_attr:
                                                        	self.mapped_attr.append(i)
								#print "i"
								#print i
							#print "self.mapped_attr"
                                        		#print self.mapped_attr
						print "list"
						print self.list14
						occ_val_temp=0
						for val in self.occ_values_n_n:
							#print "333333"
							if val[0] == self.occ_values_w_n[0][1]:
								if val[2] >= occ_val_temp:
									occ_val_temp=val[2]
									val_temp=val[1]
						#print val_temp
                                                #print "val_temp"
						for val in self.occ_values_n_num:
							#print "333333"
							if val[0] == self.occ_values_w_n[0][1]:
								if val[2] >= occ_val_temp:
									occ_val_temp=val[2]
									val_temp=val[1]
						#print val_temp
                                                #print "val_temp"



						for val in self.occ_values_n_p:
							#print "333333"
							if val[0] == self.occ_values_w_n[0][1]:
								if val[2] >= occ_val_temp:
                                                                        occ_val_temp=val[2]
                                                                        val_temp=val[1]
								
						print val_temp
						print "val_temp"
						print self.mapped_attr[0]
						if not self.mapped_attr:
							box=wx.MessageDialog(None,"Invalid Attribute name",'Alert',wx.OK)
                        				ans=box.ShowModal()
                        				box.Destroy()
						else:
                                        		self.where_clause+=' '
                                        		self.where_clause+=self.mapped_attr[0]
						#print "mapped_attr"	
						#print self.mapped_attr
						#print self.where_clause
                                        	#self.where_clause+='='
						print self.list14[wh+3][0]
						
						#Finding where clause condition
						try:
							
							syn_set_con_t=[]
							syn_set_con_q=[]
							syn_set_con_q_g=[]
							syns_con=w.synsets(self.list14[wh+3][0])


                                                        for c in syns_con:
                                                        	syn_set_con_t=list(chain.from_iterable([c.lemma_names()]))
							print syn_set_con_t


							syns_q_con=w.synsets('lesser')
							for c in syns_q_con:
								syn_set_con_q.append(list(chain.from_iterable([c.lemma_names()])))


							syns_q_con=w.synsets('below')
							for c in syns_q_con:
                                                	        syn_set_con_q.append(list(chain.from_iterable([c.lemma_names()])))


							syns_q_con=w.synsets('lower')
							for c in syns_q_con:
                                                	        syn_set_con_q.append(list(chain.from_iterable([c.lemma_names()])))


							syns_q_con=w.synsets('fewer')
							for c in syns_q_con:
                                                	        syn_set_con_q.append(list(chain.from_iterable([c.lemma_names()])))


							syns_q_con=w.synsets('smaller')
							for c in syns_q_con:
                                                	        syn_set_con_q.append(list(chain.from_iterable([c.lemma_names()])))


							#print "error"
							print syn_set_con_q
							syns_q_con=w.synsets('greater')
                                                	for c in syns_q_con:
                                                	        syn_set_con_q_g.append(list(chain.from_iterable([c.lemma_names()])))


							#print syn_set_con_q_g
							syns_q_con=w.synsets('larger')
							for c in syns_q_con:
                                                	        syn_set_con_q_g.append(list(chain.from_iterable([c.lemma_names()])))


							syns_q_con=w.synsets('above')
							for c in syns_q_con:
                                                	        syn_set_con_q_g.append(list(chain.from_iterable([c.lemma_names()])))


							#print syn_set_con_q_g
							syns_q_con=w.synsets('higher')
							for c in syns_q_con:
                                                	        syn_set_con_q_g.append(list(chain.from_iterable([c.lemma_names()])))


							#print syn_set_con_q_g
							syns_q_con=w.synsets('more')
							for c in syns_q_con:
                                                	        syn_set_con_q_g.append(list(chain.from_iterable([c.lemma_names()])))
							#print syn_set_con_q_g
							
							#print "condition entered"
							#print self.list14
							#print syn_set_con_q
							for c in range(len(syn_set_con_t)):
								#print syn_set_con_t[c]
                                                                for x in range(len(syn_set_con_q)):
									#print syn_set_con_q[x]
                                                                	for y in range(len(syn_set_con_q[x])):
										#print "dgfjhdjfhjdhfjhfjdfhjhqqqqqqqq"
										#print syn_set_con_t[c]
										#print syn_set_con_q[x][y]
                                                                                if syn_set_con_t[c] in syn_set_con_q[x][y]:
											#print syn_set_con_t[c]
											try:
												print "try"
												print self.list14[wh+6][0]

                                                                                        	if self.list14[wh+6][0] == 'equal':
                                                                                        	        #self.where_clause+='<='
                                                                                        	        condition='<='
												print condition
                                                                                                print "condition"
                                                                                        	#else:
                                                                                        	        #self.where_clause+='<'
                                                                                        	#        condition='<'
											except:
												condition='<'
												#print condition
                                                                                                #print "condition"
										#else:
										#	condition='='

							for c in range(len(syn_set_con_t)):
                                                                for x in range(len(syn_set_con_q_g)):
                                                                        for y in range(len(syn_set_con_q_g[x])):
                                                                                if syn_set_con_t[c] in syn_set_con_q_g[x][y]:
											print syn_set_con_q_g[x][y]
											print syn_set_con_t[c]
											#print self.list14[wh+6][0]
											try:
												if self.list14[wh+6][0] == 'equal':
                                                                                        	        #self.where_clause+='<='
                                                                                        	        condition='>='
                                                                                        	#else:
                                                                                        	        #self.where_clause+='<'
                                                                                        	#        condition='>'
											except:
												condition='>'
												#print condition
												#print "condition"
										#else:
										#	condition='='


							if len(condition) < 1:	
								condition='='
						
                                                except:
							condition='='                                        


						
							
								  

							
						

						#print "condition"	
						#print condition					
						self.where_clause+=condition	
                                       		self.where_clause=self.where_clause+"'"+str(val_temp)+"'"
						#print self.list14
						#print "where clause"
						print self.where_clause
				syn_set_attribute=[]
                		table_attr=[]
                		self.extract_table_attr=[]
                		self.mapped_attr=[]
                		self.list14=[]
				attribute_name_t=[]
				attribute_name=[]
				attr_l=[]
                		#self.from_clause+=' '

				
				#attribute_name=self.occ_values_v_n[0][1]
				for i in self.occ_values_v_n[:]:
					attribute_name_t.append(i[1])
				print attribute_name_t
				#print "attribute_name_t"
				print self.noun_table[0]
				#print len(attribute_name_t)
				if len(attribute_name_t) > 1:
					#print "entered"
					for i in attribute_name_t:
						#print i
						if i != self.noun_table:
							#print i
							attribute_name.append(i)
                                print attribute_name
				#print "ghfggfhgefhgehfehfghefgehfg"
				#Removing nouns after wh from attributes list
				try:
					del_ind=[]
					for d in range(len(attribute_name)):
						if attribute_name[d] == self.occ_values_w_n[0][1]:
							del_ind.append(d)
                                		#del(attribute_name[del_ind])
							print attribute_name[d]
					del_ind.reverse()
					print del_ind
					for d in del_ind:
						del(attribute_name[d])
				except:
					print "pass"
					pass
				
				#Removing table names if other attributes present

					
				#self.select_clause+=self.self.occ_values_v_n[0]
				#print "attribute_name 111"
				#print attribute_name
				for i in table_det:
					if i[0] == self.maped_table_names[0]:
						for j in i[1]:
							table_attr.append(j[0])
							#print table_attr
                        				syns_attribute=w.synsets(j[0],NOUN)
                        				syn_set_attribute_t=[]
                        				for k in syns_attribute:
                                				syn_set_attribute_t.append(list(chain.from_iterable([k.lemma_names()])))
                        				syn_set_attribute.append(syn_set_attribute_t)
							#print syn_set_attribute
						for atn in attribute_name:
							attr_l.append(atn.lower())
						for atn in attr_l:
							if atn not in table_attr:
								syns_attr=w.synsets(atn,NOUN)
								for k in syns_attr:
                                					syn_set_attr=list(chain.from_iterable([k.lemma_names()]))
								#print syn_set_attr
								for l in range(len(syn_set_attr)):
									for m in range(len(syn_set_attribute)):
                                        		        	        for n in range(len(syn_set_attribute[m])):
											#print syn_set_attr[l]
											#print syn_set_attribute[m][n]
											if syn_set_attr[l] in syn_set_attribute[m][n]:
												#print syn_set_attribute[m][n]
												#print m
												try:
													self.extract_table_attr.append(table_attr[m])
												except:
													pass
				#print "self.extract_table_attr"
				#print self.extract_table_attr
				if len(self.extract_table_attr) < 1:
					#print "fgvfhhfghfjghfjghfu"
					select_attr=self.occ_values_v_n[0][1]
					#print select_attr
					if select_attr == 'details' or select_attr == 'contents' or select_attr == 'detail' or select_attr == 'content':
						self.select_clause+=' '
						self.select_clause+='*'
						self.query=self.select_clause+' '+self.from_clause+' '+self.where_clause
						print self.query
					else:
						syns_tb=w.synsets(select_attr,NOUN)
						for i in syns_tb:
                                			syns_tbb=list(chain.from_iterable([i.lemma_names()]))
						syns_tb_q=w.synsets(self.maped_table_names[0],NOUN)
						#print self.maped_table_names[0]
						#print syns_tb_q
                                      		for i in syns_tb_q:
                                        		syns_tbb_q=list(chain.from_iterable([i.lemma_names()]))
						#print syns_tbb
						#print syns_tbb_q
						for i in range(len(syns_tbb)):
							#for j in range(len(sysns_tbb_q)):
							if syns_tbb[i] in syns_tbb_q:
								#print "hgfhg"
								self.select_clause+=' '
                        		                        self.select_clause+='*'
                        		                        self.query=self.select_clause+' '+self.from_clause+' '+self.where_clause
                        		                        print self.query
								break
		
						


				
				else:
					for i in self.extract_table_attr:
						if i not in self.mapped_attr:
							self.mapped_attr.append(i)
					print self.mapped_attr
					self.select_clause+=' '
					for i in range(len(self.mapped_attr)):
						self.select_clause+=self.mapped_attr[i]
						if i < (len(self.mapped_attr)-1):
							self.select_clause+=','
						#print self.select_clause
					self.query=self.select_clause+' '+self.from_clause+' '+self.where_clause
					print self.query
					
				

						
				
			except:
				syn_set_attribute=[]
                                table_attr=[]
                                self.extract_table_attr=[]
                                self.mapped_attr=[]
                                self.list14=[]
				attribute_name=[]
				attr_l=[]
				#print self.where_clause
				#pass
				#print "bgjgjshfcjhj"
				#for i in self.occ_values_n_n:
				#if self.maped_table_names[0] in i:
						#print i
						#attribute_name=i[1]
						#attribute_name=attribute_name.lower()
				try:
					print "self.noun_table"
					print self.noun_table
					#attribute_name=self.occ_values_n_n[0][1]
					for i in self.occ_values_n_n:
						if self.noun_table in i:
							for j in i:
								if j != self.noun_table and isinstance(j,float) == False:
									attribute_name.append(j)
					try:
						del_ind=attribute_name.index(self.occ_values_w_n[0][1])
						del(attribute_name[del_ind])
					except:
						pass
					if attribute_name[0] == 'details' or attribute_name[0] == 'detail' or attribute_name[0] == 'contents' or attribute_name[0] == 'content':
						self.select_clause+=' '
                                		self.select_clause+='*'
                               			self.query=self.select_clause+' '+self.from_clause+' '+self.where_clause
                                		print self.query
					else:
						for i in table_det:
                                			if i[0] == self.maped_table_names[0]:
                                	       			for j in i[1]:
                      		          	               		table_attr.append(j[0])
                                			               	#print table_attr
                                	        		    	syns_attribute=w.synsets(j[0],NOUN)
                                	   		             	syn_set_attribute_t=[]
                                	     		           	for k in syns_attribute:
                                	               				syn_set_attribute_t.append(list(chain.from_iterable([k.lemma_names()])))
                                	                		syn_set_attribute.append(syn_set_attribute_t)
                                	                		#print syn_set_attribute
								for atn in attribute_name:
                                                        		attr_l.append(atn.lower())
								for atn in attr_l:
									if atn not in table_attr:
                               			 	        		syns_attr=w.synsets(atn,NOUN)
                                			        	 	for k in syns_attr:
                                        				        	syn_set_attr=list(chain.from_iterable([k.lemma_names()]))
                                        	        			        print syn_set_attr
										for l in range(len(syn_set_attr)):
                                        	        				for m in range(len(syn_set_attribute)):
                                        	        			        	for n in range(len(syn_set_attribute[m])):
                                        	                	               			#print syn_set_attr[l]
                                        	                			                	#print syn_set_attribute[m][n]
                                        	                	                		if syn_set_attr[l] in syn_set_attribute[m][n]:
                                               	                	            				#print syn_set_attribute[m][n]
                                               	                	                 			#print m
                                                                	                	        	try:
                                            				                                    		self.extract_table_attr.append(table_attr[m])
                                                        			                        	except:
                                                                			                                pass
						for i in self.extract_table_attr:	
                                        	        if i not in self.mapped_attr:
                                               	        	self.mapped_attr.append(i)
                                        	print self.mapped_attr
						self.select_clause+=' '
						if not self.mapped_attr:
                                                        box=wx.MessageDialog(None,"Invalid Attribute name",'Alert',wx.OK)
                                                        ans=box.ShowModal()
                                                        box.Destroy()
						else :
                                        		#self.select_clause+=' '
                                        		#self.select_clause+=self.mapped_attr[0]
							for i in range(len(self.mapped_attr)):
                                                		self.select_clause+=self.mapped_attr[i]
                                                		if i < (len(self.mapped_attr)-1):
                                                	        	self.select_clause+=','
                                        		self.query=self.select_clause+' '+self.from_clause+' '+self.where_clause
                                        		print self.query
				except:
					self.select_clause+=' '
                                        self.select_clause+='*'
                                        self.query=self.select_clause+' '+self.from_clause+' '+self.where_clause
                                        print self.query
		query=self.query

					
			
	
	
								
	
						
	
						
						

				
				
				
			
			
			
		
			
			
		
						

					
				
			
			
			
		
		

		
		
		
		
		
		
		
		
		
		

		
		
				
		
		
		




	def csv_file(self):
		#global path
		if not os.path.exists(os.path.dirname("matrix/matrix.csv")):
                        os.makedirs(os.path.dirname("matrix/matrix.csv"))

		try:
			os.remove("./matrix/matrix.csv")
			file1 = open("./matrix/matrix.csv","a+")
		except:
			file1 = open("./matrix/matrix.csv","a+")
		t = ","
		for i in self.words:
			t += i
			t +=","
		t+="\n"
		file1.write(t)
		for l in range(len(self.occurr_val)):
			tt=''
			for m in range(len(self.occurr_val[l])):
				tt+=str(self.occurr_val[l][m])
				tt+=','
			tt+='\n'
			file1.write(tt)
		file1.close()
			
		

		

			
			 

			

		
		
		
		
		

	





if __name__=='__main__' :
	app=wx.PySimpleApp()
	main_window=MainWindow(parent=None,id=-1)
	main_window.Show()
	app.MainLoop()
1.txt
Displaying 1.txt.e the manual work and time. As for children and
adults, people are most challenged by word problem solving
not because of their mathematical skills but because of text
comprehension. Regularly, incorrect answers to word
problems are because of correct calculations to incorrect
problem representation.



