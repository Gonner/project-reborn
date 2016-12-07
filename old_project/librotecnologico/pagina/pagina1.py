import wx
import wx.animate
import time
from pagina import pagina

class paginaLibro ( pagina ) :
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		self.gif={}
		self.oldFase=-1
		self.fase=0
		
		self.puntiToccatiPrecedentemente=[]
		for i in range (0,19):
			self.puntiToccatiPrecedentemente.append(0)
		self.timerCambiaFase = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.prossimaFase, self.timerCambiaFase)
		self.sequenzaPunti = []
		self.immaginiDaMostrare = []
		self.tempoDaAspettare = []
		
		#fase 0
		self.sequenzaPunti.append (0)
		self.immaginiDaMostrare.append ([7]) #tocca il libro per iniziare
		self.tempoDaAspettare.append (-1)
		
		#fase 1
		self.sequenzaPunti.append (-1)
		self.immaginiDaMostrare.append ([0,8]) #spiegazione libro
		self.tempoDaAspettare.append (15000)
		
		#fase 2
		self.sequenzaPunti.append (1)
		self.immaginiDaMostrare.append ([1,9]) #spiegazione pallini - tocca l'arduino per continuare
		self.tempoDaAspettare.append (-1)
		
		#fase 3
		self.sequenzaPunti.append (-1)
		self.immaginiDaMostrare.append ([2]) #transitorio linguette-arduino
		self.tempoDaAspettare.append (2160)
		
		#fase 4
		self.sequenzaPunti.append (14)
		self.immaginiDaMostrare.append ([3,10]) #spiegazione arduino - tocca il pc per contunuare
		self.tempoDaAspettare.append (-1)
		
		#fase 5
		self.sequenzaPunti.append (14)
		self.immaginiDaMostrare.append ([4,11]) #spiegazione pc - tocca la tv per continuare
		self.tempoDaAspettare.append (-1)
		
		#fase 6
		self.sequenzaPunti.append (-1)
		self.immaginiDaMostrare.append ([5,12]) #spiegazione tv
		self.tempoDaAspettare.append (10000)
		
		#fase 7
		self.sequenzaPunti.append (-1)
		self.immaginiDaMostrare.append ([6]) #transitorio tv-libro
		self.tempoDaAspettare.append (1600)
		
		self.numeroFasi = len (self.sequenzaPunti)
		
		self.caricaImmagineDiSfondo ("01_libro/temp.png")
	
		self.caricaGif ("01_libro/00_libro.gif",0,484,532)
		self.caricaGif ("01_libro/01_pallino.gif",1,927,535)
		self.caricaGif ("01_libro/02_linguette.gif",2,566,311)
		self.caricaGif ("01_libro/03_arduino.gif",3,591,376)
		self.caricaGif ("01_libro/04_pc.gif",4,429,168)
		self.caricaGif ("01_libro/05_tv.gif",5,205,85)
		self.caricaGif ("01_libro/06_tv_che_si_allarga.gif",6,0,0)
		
		'''self.caricaGif ("01_libro/00_libro.gif",0,0,0)
		self.caricaGif ("01_libro/01_pallino.gif",1,0,0)
		self.caricaGif ("01_libro/02_linguette.gif",2,0,0)
		self.caricaGif ("01_libro/03_arduino.gif",3,0,0)
		self.caricaGif ("01_libro/04_pc.gif",4,0,0)
		self.caricaGif ("01_libro/05_tv.gif",5,0,0)
		self.caricaGif ("01_libro/06_tv_che_si_allarga.gif",6,0,0)'''

		self.caricaImmagine ("01_libro/07_tocca.png",7,161,236)
		self.caricaImmagine ("01_libro/08_spiegazione_libro.png",8,140,582)
		self.caricaImmagine ("01_libro/09_spiegazione_pallino.png",9,140,247)
		self.caricaImmagine ("01_libro/10_spiegazione_arduino.png",10,598,158)
		self.caricaImmagine ("01_libro/11_spiegazione_pc.png",11,196,247)
		self.caricaImmagine ("01_libro/12_spiegazione_tv.png",12,1023,666)
				
	def show ( self ) :
		self.oldFase=-1
		self.fase=0
	
	def hide ( self ) :
		self.nascondiTutte ()
	
	def routineVisibile (self, puntiToccati) :
		#print "fase: "+str(self.fase)
		#print "aspetto punto "+str (self.sequenzaPunti[self.fase])
		#print "aspetto tempo "+str (self.tempoDaAspettare[self.fase])
		#print "prima "+str (self.puntiToccatiPrecedentemente)
		#print "dopo  "+str (puntiToccati)
		if self.oldFase != self.fase:
			self.oldFase=self.fase
			self.nascondiTutte (self.immaginiDaMostrare[self.fase])
			for i in self.immaginiDaMostrare[self.fase]:
				self.mostraImmagine (i,-1)
				if i<6: #era un gif
					self.gif[i].Play()
			if self.tempoDaAspettare[self.fase] > 0:
				self.timerCambiaFase.Start( self.tempoDaAspettare[self.fase], wx.TIMER_ONE_SHOT )
		if self.sequenzaPunti[self.fase] >= 0 and puntiToccati[ self.sequenzaPunti[self.fase] ] == 1 and self.puntiToccatiPrecedentemente[ self.sequenzaPunti[self.fase] ] == 0 :
			self.timerCambiaFase.Stop()
			self.prossimaFase (None)
		self.puntiToccatiPrecedentemente=puntiToccati
			
	def routineInvisibile (self) :
		pass

	def caricaGif (self, nome, id, posX, posY):
		gif_fname = self.prefissoImmagini+nome
		self.gif[id] = wx.animate.GIFAnimationCtrl(self, id, gif_fname, pos=(posX, posY))
		self.gif[id].GetPlayer().UseBackgroundColour(True)
		self.media[id] = self.gif[id]

	def prossimaFase (self,event):
		self.fase = ( self.fase+1 ) % self.numeroFasi
