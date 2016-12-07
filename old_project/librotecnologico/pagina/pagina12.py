# -*- coding: utf-8 -*-
import wx
import random
from pagina import pagina

class pagina12 ( pagina ) :
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		self.caricaImmagineDiSfondo ("12_Gioco_carte/Forma schermo.png")
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/0001.png",0b0001,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/0010.png",0b0010,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/0011.png",0b0011,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/0100.png",0b0100,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/0101.png",0b0101,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/0110.png",0b0110,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/0111.png",0b0111,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/1000.png",0b1000,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/1001.png",0b1001,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/1010.png",0b1010,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/1011.png",0b1011,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/1100.png",0b1100,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/1101.png",0b1101,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/1110.png",0b1110,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/1111.png",0b1111,1150,800)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/la_tua_carta.png",20,1080,700)
		self.caricaImmagine ("12_Gioco_carte/carte_prosp/non_hai.png",21,950,750)
		self.puntiToccatiSalva = [0,0,0,0]
		self.time = 5000;
		self.bPuntiToccati = False
		self.stato = 0
		self.nliguetta1 = 17
		self.nliguetta2 = 14
		self.nliguetta3 = 11
		self.nliguetta4 = 8
		self.indovinatoSi = 3
		self.indovinatoNo = 5

	def controllo (self, event) :
		n= self.puntiToccatiSalva[3]+ (self.puntiToccatiSalva[2]<<1) + (self.puntiToccatiSalva[1]<<2) + (self.puntiToccatiSalva[0]<<3)
		self.mostraImmagine(20,10000)
		self.mostraImmagine(n,10000)
		self.puntiToccatiSalva = [0,0,0,0]
		self.stato = 1
		self.temporizzatore = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.resetta, self.temporizzatore)
		self.temporizzatore.Start( self.time, wx.TIMER_ONE_SHOT)


	def routineVisibile (self, puntiToccati) :
		if self.stato == 0 :
			self.bPuntiToccati = False
			if puntiToccati[self.nliguetta1] == 1 :
				self.puntiToccatiSalva[0] = 1
				self.bPuntiToccati = True
			elif puntiToccati[self.nliguetta2] == 1 :
				self.puntiToccatiSalva[1] = 1
				self.bPuntiToccati = True
			elif puntiToccati[self.nliguetta3] == 1 :
				self.puntiToccatiSalva[2] = 1
				self.bPuntiToccati = True
			elif puntiToccati[self.nliguetta4] == 1 :
				self.puntiToccatiSalva[3] = 1
				self.bPuntiToccati = True

			if self.bPuntiToccati :
				self.nascondiImmagine(21)
				self.temporizzatore = wx.Timer(self)
				self.Bind(wx.EVT_TIMER, self.controllo, self.temporizzatore)
				self.temporizzatore.Start( self.time, wx.TIMER_ONE_SHOT)
				
		elif self.stato == 1 :	
			if puntiToccati[self.indovinatoSi] == 1 :
				self.resetta()
			elif puntiToccati[self.indovinatoNo] == 1 :
				self.resetta()
				self.mostraImmagine(21,10000)
				
	def resetta (self, event=None) : 
		self.stato = 0
		self.temporizzatore.Stop()
		self.nascondiTutte()
	
	def routineInvisibile (self) :
		print ("Routine invisibile -- 0")

	def hide (self):
		self.nascondiTutte()
