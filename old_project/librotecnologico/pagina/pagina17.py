
import wx
from pagina import pagina
import os
import sys
import random
import subprocess
import time

class presentazione(pagina):
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )

		self.nRigheFile = 0
		self.img = 0
		self.timeoutImmagine = 10*1000
		self.nullaAttivo=True
		self.videoAttivo=False
		self.imgAttiva=False
		self.firstTime = True
		self.controlVlc = False
		self.nMaxMedia = 0
		self.mediaCorrente = 0
		self.videoTot = 0
		self.path="/home/arazzo/librotecnologico/immagini/17_presentazione/"
		self.dirs = os.listdir(self.path)
		for file in self.dirs:
			self.nMaxMedia = self.nMaxMedia + 1
		
		
	def show ( self ) :
		pass
	
	def routineVisibile (self, puntiToccati) :
		#se non c'e'nulla sullo schermo
		if self.firstTime:
			#subprocess.call("nvidia-smi", shell=True)
			self.firstTime = False
			self.avviaVideo(self.path+"arazzo_corto.mpg")
		elif(self.nullaAttivo):	
			#subprocess.call("top -n1 -o %MEM", shell=True)	
			if(self.mediaCorrente > self.nMaxMedia):
				self.mediaCorrente = 0
			print self.mediaCorrente
			pathControllo = self.path+str(self.mediaCorrente)
			#se sono immagini
			if(os.path.exists(pathControllo+".png")):
				pathControllo = pathControllo+".png"
				self.showImmagine(pathControllo)
			if(os.path.exists(pathControllo+".jpg")):
				pathControllo = pathControllo+".jpg"
				self.showImmagine(pathControllo)
			#se sono video
			if(os.path.exists(pathControllo+".mp4")):
				pathControllo = pathControllo+".mp4"
				self.avviaVideo(pathControllo)
			if(os.path.exists(pathControllo+".m4v")):
				pathControllo = pathControllo+".m4v"
				self.avviaVideo(pathControllo)
			if(os.path.exists(pathControllo+".mpg")):
				pathControllo = pathControllo+".mpg"
				self.avviaVideo(pathControllo)
			if(os.path.exists(pathControllo+".mov")):
				pathControllo = pathControllo+".mov"
				self.avviaVideo(pathControllo)
			self.mediaCorrente = self.mediaCorrente + 1
		else:
			if self.videoAttivo and self.controlVlc == False:
				subprocess.call("ps aux | grep bin/vlc >/home/arazzo/librotecnologico/immagini/17_presentazione/vlcOpen.txt", shell=True)
				time.sleep(1)
				self.checkVlcOpen()
			
	def checkVlcOpen(self):
		#Controllo nel file se e' attivo o no
		self.controlVlc = True
		with open('/home/arazzo/librotecnologico/immagini/17_presentazione/vlcOpen.txt') as f:
			self.nRigheFile = sum(1 for _ in f)
		if(self.nRigheFile == 1):
			self.nullaAttivo = True
			self.scriviTxtVlc("False", "")
		print self.nRigheFile
		self.controlVlc = False
	
	def avviaVideo(self, path):
		self.videoAttivo = True
		self.nullaAttivo = False
		#Avvio vlc con la path
		print "Avviato"
		#Scrive true qui /home/arazzo/controlloAvviaVideo.txt e sotto la path
		self.scriviTxtVlc("True", path)		
		
	def stopVideo (self):
		print "Stoppato"
		self.scriviTxtVlc("False", "")
		subprocess.call("killall vlc", shell=True)
		self.videoAttivo = False
		self.nullaAttivo = True
	
	def scriviTxtVlc(self, boolean, path):
		out_file = open("/home/arazzo/controlloAvviaVideo.txt","w")
		out_file.write(boolean+"\n"+path+"\n")
		out_file.flush()
		out_file.close()
	
	def showImmagine(self, path):
		self.nullaAttivo = False
		self.imgAttiva = True
		self.img = self.loadImage (path, 0, 0, 0, True, True)
		self.img.Show()
		self.Layout()
		self.timerImmagine = wx.Timer(self)
		self.Bind(wx.EVT_TIMER,self.nascondiImmagine, self.timerImmagine)
		self.timerImmagine.Start(self.timeoutImmagine , wx.TIMER_ONE_SHOT)
		print "show immagine: " + str(self.nullaAttivo)
			
	def nascondiImmagine (self, event=None):
		self.img.Hide()
		self.img.Destroy()
		self.imgAttiva = False
		print "nascondi immagine " + str(self.nullaAttivo)
		self.nullaAttivo = True

	def routineInvisibile (self) :
		pass
		
	def hide (self):
		self.firstTime = True
		self.nullaAttivo = True
		self.mediaCorrente = 0
		if self.videoAttivo:
			self.stopVideo()
		elif self.imgAttiva:
			self.nascondiImmagine()
			self.timerImmagine.Stop()
		
