#encoding: utf-8
import wx
import wx.media
import warnings
import random
import os
import sys
import subprocess
import time

class pagina (wx.Panel):
	def __init__ ( self , parent , grandParent , index ) :
		wx.Panel.__init__( self, parent )
		self.SetInitialSize (  wx.Size(1920,1080))
		self.index=index
		
		self.media={}
		self.timer={}

		self.ContentSize =  (1920,1080)
		self.ScaleFactor = 1		
		self.Offset = (0,0)
		
		self.controlVlc = False
		self.videoAttivoP=False
		
		self.timerFineVideo = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.checkVlcOpen, self.timerFineVideo)
		#self.timerFineVideo.Start( 500 )
		self.controlVlc = False
		
		self.prefissoImmagini=None
		self.percorso=["/usr/share/librotecnologico/immagini/",os.getcwd()+"/immagini/"]
		for p in self.percorso:
			if (os.path.isdir(p)):
				self.prefissoImmagini=p 
		
		if not self.prefissoImmagini:
			sys.exit("Errore: non trovo la cartella con le immagini.\nInstalla il pacchetto librotecnologico o esegui main.py da un'altra locazione")
		
		self.SetBackgroundColour( (random.random()*255,random.random()*255,random.random()*255) )
			
	def checkVlcOpen(self,event=None):
		#Controllo nel file se e' attivo o no
		if self.controlVlc == False:
			self.controlVlc = True
			subprocess.call("ps aux | grep bin/vlc >/home/arazzo/librotecnologico/immagini/17_presentazione/vlcOpen.txt", shell=True)
			time.sleep(0.500)
			with open('/home/arazzo/librotecnologico/immagini/17_presentazione/vlcOpen.txt') as f:
				self.nRigheFile = sum(1 for _ in f)
			if(self.nRigheFile == 1):
				self.nullaAttivo = True
				self.scriviTxtVlc("False", "")
			print self.nRigheFile
			self.controlVlc = False
			
	def evalueScaleFactor (self, width,height): 
		self.ContentSize = (width,height)
		ContentRatio = self.ContentSize[0]/self.ContentSize[1]
		PageRatio = self.GetSize().width/self.GetSize().height
		self.ScaleFactor = 1
		
		self.Offset = (0,0)
		
		if ContentRatio < PageRatio :
			height = min (self.ContentSize[1],self.GetSize().height)
			self.ScaleFactor = float(height)/float(self.ContentSize[1])
			width = self.ScaleFactor * self.ContentSize[0]
			self.Offset = ( 0.5*float(self.GetSize().width-width), 0.5*float(self.GetSize().height-height) )
		else : 
			width = min (self.ContentSize[0],self.GetSize().width)
			self.ScaleFactor = float(width)/float(self.ContentSize[0])
			height = self.ScaleFactor * self.ContentSize[1]
			self.Offset = ( 0.5*float(self.GetSize().width-width), 0.5*float(self.GetSize().height-height) )
		
			
	def loadImage (self, nome, id, posX=0, posY=0, evalue = False, percorsoAssoluto=False):
		nomeDefinitivo=nome
		if not percorsoAssoluto:
			nomeDefinitivo=self.prefissoImmagini+nome
		if not os.path.isfile(nomeDefinitivo):
			sys.exit("pagina"+str(self.index)+".caricaImmagine: file "+nomeDefinitivo+" non trovato")
		img = wx.Image(nomeDefinitivo, wx.BITMAP_TYPE_ANY)
		if evalue :
			self.evalueScaleFactor(img.GetWidth(),img.GetHeight())
		img = img.Scale(img.GetWidth()*self.ScaleFactor , img.GetHeight()*self.ScaleFactor )
		img = img.ConvertToBitmap()
		return wx.StaticBitmap(self, bitmap=img, pos=(float(posX)*self.ScaleFactor+self.Offset[0],
														float(posY)*self.ScaleFactor+self.Offset[1]) )
		
	def caricaImmagineDiSfondo (self, nome):
		self.immagineDiSfondo = self.loadImage (nome, wx.ID_ANY, evalue=True)
	
	def caricaImmagine ( self , nome , id, posX=0, posY=0, invisibile=True, percorsoAssoluto=False ) :
		self.media[id] = self.loadImage (nome , id, posX, posY, False, percorsoAssoluto  )
		if ( invisibile == True ):
			self.media[id].Hide()
			
	def mostraImmagine (self, id, timeout=-1):
		if (id in self.media):
			self.media[id].Show()
			self.Layout()
			if (timeout>0):
				self.timer[id] = wx.Timer(self)
				self.Bind(wx.EVT_TIMER, lambda m: self.nascondiImmagine(id), self.timer[id])
				self.timer[id].Start( timeout, wx.TIMER_ONE_SHOT)
		else:
			warnings.warn ("pagina"+str(self.index)+".mostraImmagine: non è stata caricata alcuna immagine con id "+str(id))
			
	def nascondiImmagine (self, id):
		if (id in self.media):
			self.media[id].Hide()
		else:
			warnings.warn ("pagina"+str(self.index)+".nascondiImmagine: non è stata caricata alcuna immagine con id "+str(id))
	
	def mostraTutte (self):
		pass;

	def nascondiTutte (self,tranne=[]):
		for i in self.media:
			if ( not i in tranne ):
				if self.getTypeMedia(i)  == "StaticBitmap":
					self.media[i].Hide()
		self.stopVideo()
	
	def hide ( self ) :
		return
	def show ( self ) :
		return	
	def routineVisibile ( self, puntiToccati ):
		return
	def routineInvisibile ( self ):
		return
		
	def loadVideo ( self , path, percorsoAssoluto = False):		
		if not os.path.isfile(self.prefissoImmagini+path) and not percorsoAssoluto:
			sys.exit("pagina"+str(self.index)+".caricaVideo: file "+path+" non trovato")
		if not percorsoAssoluto:
			path = self.prefissoImmagini+path
		return path
 
	def caricaVideo (self, nome, id):
		self.media[id] = self.loadVideo ("/home/arazzo/librotecnologico/immagini/" + nome , True)
	
	def avviaVideo(self, path):
		self.videoAttivoP = True
		#Avvio vlc con la path
		#print "Avviato"
		#Scrive true qui /home/arazzo/controlloAvviaVideo.txt e la path
		self.scriviTxtVlc("True", path)
		
	def stopVideo (self):
		#print "Stoppato"
		self.scriviTxtVlc("False", "")
		subprocess.call("killall vlc", shell=True)
		self.videoAttivoP = False
	
	def scriviTxtVlc(self, boolean, path):
		out_file = open("/home/arazzo/controlloAvviaVideo.txt","w")
		out_file.write(boolean+"\n"+path+"\n")
		out_file.flush()
		out_file.close()
	
	def mostraVideo (self, id):
		if (id in self.media):
			self.avviaVideo(self.media[id])
		else:
			warnings.warn ("pagina"+str(self.index)+".mostraVideo: non è stato caricato alcun video con id "+str(id))
			
	def nascondiVideo (self):
		self.stopVideo()
		
	def playVideo (self, id):
		pass
		
	def pausaVideo (self, id):
		pass

	def getTypeMedia(self,id):
		#restituisce il nome della classe dell' oggetto dentro il map media
		return self.media[id].__class__.__name__

	def nascondiMedia (self, id):
		if (id in self.media):
			if(self.getTypeMedia(id) == "StaticBitmap"):
				self.media[id].Hide()
			else:
				self.stopVideo()
		else:
			warnings.warn ("pagina"+str(self.index)+".nascondiMedia: non è stato caricato alcun media con id "+str(id))		

	def on_media_stop(self, id):
		self.nascondiVideo(id)

class paginaSemplice (pagina):
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		self.associazioni=[]
		self.precId = 0
		
	def show ( self ) :
		pass
	
	def routineVisibile (self, puntiToccati) :
		for ass in self.associazioni:
			#ass=(idMedia, linguetta, timeout)
			#       ass[0]      ass[1]    ass[2]
			if (puntiToccati[ ass[1] ]==1):
				#Controlla se l' oggetto scelto è di tipo immagine
				if self.getTypeMedia(ass[0]) == "StaticBitmap":
					self.nascondiTutte ([ass[0]])
					self.mostraImmagine (ass[0], ass[2])
				else: #if self.videoAttivoP == False
					self.precId = puntiToccati[ ass[1] ]
					#se non è di tipo immagine allora mostra il video e lo fa partire
					self.nascondiTutte ([ass[0]])
					self.mostraVideo(ass[0])
					#self.playVideo(ass[0])
				
	def routineInvisibile (self) :
		pass

	def hide (self):
		self.nascondiTutte()
