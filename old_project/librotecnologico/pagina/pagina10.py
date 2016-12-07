#encoding: utf-8

import wx
from pagina import pagina
import os

class paginaItalia ( pagina ) :
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		
		self.cod=-1
		self.NUMERO_CITTA=12
		self.OFFSET=10
		
		self.linguette=[]
		self.codiceImmagineClima=30
		
		#file per dialogare con il demone del clima
		self.FILE_INPUT="/tmp/clima"
		self.FILE_OUTPUT="/tmp/citta"
		
		#sfondo
		self.caricaImmagineDiSfondo ("10_italia/schermo.png")
		
		#città
		self.caricaImmagine ("10_italia/citta/milano.png",0,960,270)
		self.caricaImmagine ("10_italia/citta/torino.png",1,960,270)
		self.caricaImmagine ("10_italia/citta/venezia.png",2,960,270)
		self.caricaImmagine ("10_italia/citta/bologna.png",3,960,270)
		self.caricaImmagine ("10_italia/citta/firenze.png",4,960,270)
		self.caricaImmagine ("10_italia/citta/ancona.png",5,960,270)
		self.caricaImmagine ("10_italia/citta/roma.png",6,960,270)
		self.caricaImmagine ("10_italia/citta/napoli.png",7,960,270)
		self.caricaImmagine ("10_italia/citta/bari.png",8,960,270)
		self.caricaImmagine ("10_italia/citta/catanzaro.png",9,940,270)
		self.caricaImmagine ("10_italia/citta/palermo.png",10,960,270)
		self.caricaImmagine ("10_italia/citta/cagliari.png",11,960,270)
		
		#bersagli
		self.caricaImmagine ("10_italia/bersaglio.png",12,770,245)
		self.caricaImmagine ("10_italia/bersaglio.png",13,725,270)
		self.caricaImmagine ("10_italia/bersaglio.png",14,860,250)
		self.caricaImmagine ("10_italia/bersaglio.png",15,830,280)
		self.caricaImmagine ("10_italia/bersaglio.png",16,820,310)
		self.caricaImmagine ("10_italia/bersaglio.png",17,890,315)
		self.caricaImmagine ("10_italia/bersaglio.png",18,870,375)
		self.caricaImmagine ("10_italia/bersaglio.png",19,920,420)
		self.caricaImmagine ("10_italia/bersaglio.png",20,1000,400)
		self.caricaImmagine ("10_italia/bersaglio.png",21,1010,495)
		self.caricaImmagine ("10_italia/bersaglio.png",22,900,525)
		self.caricaImmagine ("10_italia/bersaglio.png",23,745,480)
		
		#climi
		self.caricaImmagine ("10_italia/climi/neve.png",24,1300,200)
		self.caricaImmagine ("10_italia/climi/fulmini.png",25,1300,200)
		self.caricaImmagine ("10_italia/climi/temporale.png",26,1300,200)
		self.caricaImmagine ("10_italia/climi/pioggia.png",27,1300,200)
		self.caricaImmagine ("10_italia/climi/nubi.png",28,1300,200)
		self.caricaImmagine ("10_italia/climi/nebbia.png",29,1300,200)
		self.caricaImmagine ("10_italia/climi/sereno.png",30,1300,200,False)
		self.caricaImmagine ("10_italia/climi/luna.png",31,1300,200)
		self.caricaImmagine ("10_italia/climi/sole.png",32,1300,200)
		self.caricaImmagine ("10_italia/climi/solissimo.png",33,1300,200)
		
		self.linguette.append (15) #codice 0 - Milano ha linguetta 15
		self.linguette.append (13) #codice 1 - Torino ha linguetta 13
		self.linguette.append (17) #codice 2 - Venezia ha linguetta 17
		self.linguette.append (12) #codice 3 - Bologna ha linguetta 12
		self.linguette.append (10) #codice 4 - Firenze ha linguetta 10
		self.linguette.append (8) #codice 5 - Ancona ha linguetta 8
		self.linguette.append (6) #codice 6 - Roma ha linguetta 6
		self.linguette.append (3) #codice 7 - Napoli ha linguetta 3
		self.linguette.append (5) #codice 8 - Bari ha linguetta 5
		self.linguette.append (2) #codice 9 - Catanzaro ha linguetta 2
		self.linguette.append (0) #codice 10 - Palermo ha linguetta 0
		self.linguette.append (1) #codice 11 - Cagliari ha linguetta 1

	def show ( self ) :
		pass
	
	def routineVisibile (self, puntiToccati) :
		#self.i += 1
		#if (self.i%160 == 0):
		#	self.mostraImmagine ((self.i/160)%15,3900)
		#	self.mostraImmagine ((self.i/160)%15+self.NUMERO_CITTA,3900)
		for i in range (self.NUMERO_CITTA):
			if ( puntiToccati[ self.linguette[i] ]==1 ) :
				self.mostraImmagine (i,-1)
				self.mostraImmagine (i+self.NUMERO_CITTA,-1)
				self.nascondiTutte ([i,i+self.NUMERO_CITTA,self.codiceImmagineClima])
				self.interrogaDemone (i+self.OFFSET)
				self.cod=i
		if ( self.cod!=-1 and puntiToccati[self.cod]==0 and os.path.isfile( self.FILE_INPUT ) ):
			f=open (self.FILE_INPUT, "r")
			cod=f.read ()
			#print ("calcolato "+cod)
			self.nascondiImmagine (self.codiceImmagineClima)
			self.codiceImmagineClima=int(cod)+2*self.NUMERO_CITTA
			self.mostraImmagine (self.codiceImmagineClima,-1)
			f.close()
			os.remove (self.FILE_INPUT)
		
	def routineInvisibile (self) :
		pass

	def interrogaDemone (self, idCitta) :
		f=open (self.FILE_OUTPUT, "w")
		f.write (str(idCitta))
		f.close ()
