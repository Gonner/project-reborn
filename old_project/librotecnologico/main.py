#!/usr/bin/python

import wx, random, serial
import subprocess as sp
import os

#import pagine
from pagina import *


def sign ( x ) :
	return 1 if x>0 else ( -1 if x<0 else 0 )
		
class Pager (wx.Panel):
	def __init__(self , parent):
		wx.Panel.__init__( self, parent )
		#IL PROBLEMA E' QUI!!!!!!!!!!!!
		#CON 18 NON FA...
		#BISOGNA ELIMINARE UNA PAGINA
		self.numOfPage = 17 
		self.SetInitialSize( ( wx.DisplaySize()[0] + 1, wx.DisplaySize()[1] - 25 ) )
		self.SetPosition( ( 0 , 0 ) )
		self.slide = wx.Panel ( self )
		self.slide.SetInitialSize ( ( self.GetSize().width*self.numOfPage , self.GetSize().height +1 ) ) 
		self.pages = []
		self.pages.append ( pagina0.pagina0 ( self.slide , self , 0 ) )
		self.pages.append ( pagina1.paginaLibro ( self.slide , self , 1 ) )
		self.pages.append ( pagina2.paginaChimica ( self.slide , self , 2 ) )
		self.pages.append ( pagina3.pagina3 ( self.slide , self , 3 ) )
		self.pages.append ( pagina4.pagina4 ( self.slide , self , 4 ) )
		self.pages.append ( pagina5.pagina5 ( self.slide , self , 5 ) )
		self.pages.append ( pagina6.pagina6 ( self.slide , self , 6 ) )
		self.pages.append ( pagina7.pagina7 ( self.slide , self , 7 ) )
		self.pages.append ( pagina8.pagina8 ( self.slide , self , 8 ) )
		self.pages.append ( pagina9.paginaAbbraccio ( self.slide , self , 9 ) )
		self.pages.append ( pagina10.paginaItalia ( self.slide , self , 10 ) )
		self.pages.append ( pagina11.paginaMappamondo ( self.slide , self , 11 ) )
		self.pages.append ( pagina12.pagina12 ( self.slide , self , 12 ) )
		self.pages.append ( pagina13.pagina13 ( self.slide , self , 13 ) )
		self.pages.append ( pagina14.pagina14 ( self.slide , self , 14 ) )
		self.pages.append ( pagina15.pagina15 ( self.slide , self , 15 ) )
		#self.pages.append ( pagina16.pagina16 ( self.slide , self , 16 ) )
		self.pages.append ( pagina17.presentazione( self.slide , self , 17 ) )

		for i in range ( self.numOfPage):
			self.pages[i].SetPosition ( ( i*self.GetSize().width , 0 ) ) 
			
			
class BottomBar ( wx.Panel ):
	def __init__( self, parent, pager ):
		wx.Panel.__init__( self, parent )
		self.pager = pager
		self.fontColor = wx.BLACK
		self.SetInitialSize( ( pager.GetSize().width , wx.DisplaySize()[1] - pager.GetSize().height + 1 ) )
		self.SetPosition( ( 0, pager.GetSize().height ) )
		self.SetBackgroundColour( wx.WHITE )
		self.insertNums ()
		weight = 6 		
		self.space = wx.Panel ( self , size = (self.GetSize().width/self.pager.numOfPage+1 , weight) , pos = ( 0 , self.GetSize().height - weight ) )
		
		self.space.SetBackgroundColour ( (200,100,100,0.4) )
		self.paintText ( 0 )
		
		self.selected = 0
		self.to_select = 0
		self.suc_ending_pos = -1
		self.ending_pos = 0
		self.starting_pos = self.x = 0
		self.max_acc = 0.004
		self.min_acc = 0.002
		self.acc = self.min_acc
		self.cur_vel = 0
		self.time = 25
		self.dec_time = 1000
		self.precpage = 0		
		self.timeStartPres = 1000*60*7
		self.startCountdown = False;
		self.timerPres = wx.Timer(self)
		
		self.mappaturaTasti = "1 2 3 4 5 6 7 8 9 0 Q W E R T Y U I O P A S D F G H J K L Z X C V B N M ,".split()
		self.fileLinguette="/var/www/html/txtfiles/linguette.txt"
		#self.fileLinguette="/var/www/html/controllo.txt"
		
		self.linguette = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.linguettePrecedenti=self.linguette
		
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.update, self.timer)
		self.timer.Start( self.time )
		
		#Controlla sempre che quando toccato riinizi
		self.timerNonTocca = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.nonTocca, self.timerNonTocca)
		self.timerNonTocca.Start( self.time )
		
		self.parametro=[]
		self.timerLinguette=[]
		for i in range (len(self.linguette)):
			self.timerLinguette.append ( wx.Timer(self) )
		
		
	def key (self,event=None) :
		if ( event.GetKeyCode() in range (256) ):
			c=chr (event.GetKeyCode())
			if (c in self.mappaturaTasti):
				self.linguette[ self.mappaturaTasti.index(c) ] = 1-self.linguette[ self.mappaturaTasti.index(c) ]
	
				
	def avviaPresentazione(self,event=None):
		self.avviataPres = True
		self.precpage = self.selected
		self.goto(16)
		for i in range(0,len(self.linguette)):
			self.linguette[i]=0
		self.linguette[16] = 1
		
	def nonTocca(self,event=None):
		if (self.startCountdown == False):
			print "Avviato countdown"
			self.startCountdown = True;
			self.Bind(wx.EVT_TIMER, self.avviaPresentazione, self.timerPres)
			self.timerPres.Start( self.timeStartPres, wx.TIMER_ONE_SHOT )
	
	
	def rimettiZero (self, i):
		self.linguette[i]=0
		
	def update ( self , event ) :
		#print self.linguette
		if os.path.isfile (self.fileLinguette):
			fd=open (self.fileLinguette, "r")
			linea=fd.read()
			i=0
			for l in linea.split():
				self.linguette[i]=int(l)
				if i>=self.pager.numOfPage and self.linguette[i] != self.linguettePrecedenti[i] and self.linguette[i]==1 : #i pallini vanno resettati
					self.parametro.append(i)
					self.Bind(wx.EVT_TIMER, lambda m: self.rimettiZero(self.parametro.pop()), self.timerLinguette[i])
					self.timerLinguette[i].Start( 4000, wx.TIMER_ONE_SHOT )
				i += 1

			fd.close()
			os.remove (self.fileLinguette)
			if(self.startCountdown == True):
				print "Stoppato timer"
				self.startCountdown = False
				self.timerPres.Stop()
		i=0
		while (self.linguette[i]==0 and i<self.pager.numOfPage):
			i=i+1
		if (i<self.pager.numOfPage):
			self.goto (i+1)
		else:
			self.goto (0)
		self.linguettePrecedenti=list(self.linguette)
		
		prev_x = self.x
		arrived = False
		perc = 0.75
		if(self.x>=self.ending_pos and self.ending_pos>=self.starting_pos)or(self.x<=self.ending_pos and self.ending_pos<=self.starting_pos): 
			arrived = True
		if float(abs(self.x-self.starting_pos)) >= perc*float(abs(self.ending_pos-self.starting_pos)) and self.acc > 0 and not arrived:
			self.acc = -self.acc*3*0.9
		if self.starting_pos < self.ending_pos :		
			self.cur_vel += self.acc
			self.cur_vel = self.cur_vel if self.cur_vel > 0 else 0.002 
		else :
			self.cur_vel += -self.acc
			self.cur_vel = self.cur_vel if self.cur_vel < 0 else -0.002 
		if self.starting_pos != self.ending_pos : 
			self.x += self.cur_vel * self.time
		
		if arrived :
			self.cur_vel = 0
			self.starting_pos = self.ending_pos
			self.x = float(self.ending_pos)
			self.acc = self.min_acc
			if self.suc_ending_pos != -1 : 			
				self.ending_pos = self.suc_ending_pos
				self.suc_ending_pos = -1
			if self.to_select != self.selected :
				self.pager.pages[self.to_select].show()
				self.selected = self.to_select
			else :
				#print self.linguette[self.pager.numOfPage:]
				self.pager.pages[self.to_select].routineVisibile( self.linguette[self.pager.numOfPage:] )
			self.paintText(self.to_select)
		if prev_x != self.x:
			self.space.SetPosition ( ( self.x/100 * (self.GetSize().width) , self.space.GetPosition().y ) )
			self.pager.slide.SetPosition ( ( - self.x/100 * (self.pager.GetSize().width*17) , 0 ) )
		#for i in range (len(self.pager.pages)) :
			#self.pager.pages[i].routineInvisibile ()
			
			
	def goto ( self, i ) :
		if i >= 17  or i==self.selected: return
		self.paintText()
		self.pager.pages[self.selected].hide()
		self.to_select = i
		self.suc_ending_pos = float(self.pager.pages[i].GetPosition().x) / float(self.pager.GetSize().width*17) * 100

	def paintText ( self , i=-1 ) :
		for j in range( self.pager.numOfPage ) :
			self.texts[j].SetForegroundColour ( self.fontColor ) 
		if i!=-1 : self.texts[i].SetForegroundColour ( self.space.GetBackgroundColour () )
		
	def insertNums (self) :
		self.cont = wx.Panel ( self )
		self.cont.SetInitialSize( self.GetSize() )
		sizer = wx.BoxSizer( wx.HORIZONTAL )
		self.cont.SetSizer( sizer )
		self.texts = []
		for i in range( self.pager.numOfPage ) :
			panel = wx.Panel(self.cont)
			panel.SetInitialSize( (self.GetSize().width/self.pager.numOfPage+i%2 , self.GetSize().height) ) 
			text = wx.StaticText ( panel , label = ( "Inizio" if i==0 else 
										"Fine" if i==self.pager.numOfPage-1 else str((i-1)*2+1)+"-"+str((i-1)*2+2) ) , style=wx.ALIGN_CENTRE )
			text.SetPosition (( int((panel.GetSize().width-text.GetSize().width)/2) , 0 ))
		#	t_s = wx.BoxSizer( wx.HORIZONTAL ) 
		#	t_s.Add( text )
		#	panel.SetSizer( t_s )
			sizer.Add( panel )
			self.texts.append( text )


class Frame (wx.Frame):
	def __init__ (self):
		wx.Frame.__init__(self,None,wx.ID_ANY,"Arazzo")
		self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)	
		self.SetPosition(wx.Point(1280,0))
		self.pager = Pager(self)
		self.botBar = BottomBar(self, self.pager)
		
		#TODO: sostituire la lettura da tastiera con quella da seriale 
		self.Bind(wx.EVT_KEY_DOWN, self.botBar.key)
		self.Bind(wx.EVT_KEY_UP, self.botBar.key)
		self.Bind(wx.EVT_CHAR, self.botBar.key)
		
		self.botBar.SetFocus()
		
		#serve a farlo iniziare alla pagina su cui si sta lavorando
		#self.botBar.goto (10)
		#print (wx.DisplaySize())
		#(1366, 768)
		
app = wx.App(False)
Frame()
app.MainLoop()


