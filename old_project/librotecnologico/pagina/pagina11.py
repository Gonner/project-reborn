#encoding: utf-8

import wx
from pagina import pagina
import os

class paginaMappamondo ( pagina ) :
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		
		self.i=-1
		self.codiceImmagineClima=30
		
		self.cod=-1
		self.NUMERO_CITTA=15
		self.OFFSET=22
		
		#file per dialogare con il demone del clima
		self.FILE_INPUT="/tmp/clima"
		self.FILE_OUTPUT="/tmp/citta"
		
		#sfondo
		self.caricaImmagineDiSfondo ("11_mappamondo/schermo.png")
		
		#città
		self.caricaImmagine ("11_mappamondo/scritte_citta/canberra.png",1,1400,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/antananarivo.png",2,1400,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/giacarta.png",3,1400,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/abuja.png",4,1400,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/il_cairo.png",5,1400,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/pechino.png",6,1400,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/parigi.png",7,1425,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/buenos_aires.png",8,1375,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/londra.png",9,1425,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/mosca.png",10,1425,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/brasilia.png",11,1400,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/citta_del_messico.png",12,1385,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/washington.png",13,1400,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/new_york.png",14,1425,375)
		self.caricaImmagine ("11_mappamondo/scritte_citta/ottawa.png",0,1425,375)
		
		#bersagli
		self.caricaImmagine ("11_mappamondo/bersaglio.png",16,1200,770)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",17,840,700)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",18,1050,620)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",19,615,760)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",20,780,500)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",21,1080,450)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",22,700,410)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",23,430,700)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",24,690,390)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",25,810,370)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",26,470,650)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",27,350,530)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",28,370,450)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",29,395,435)
		self.caricaImmagine ("11_mappamondo/bersaglio.png",15,375,410)
		
		#climi
		self.caricaImmagine ("09_abbraccio/climi/neve.png",31,1375,600,True)
		self.caricaImmagine ("09_abbraccio/climi/fulmini.png",32,1375,600,True)
		self.caricaImmagine ("09_abbraccio/climi/temporale.png",33,1375,600,True)
		self.caricaImmagine ("09_abbraccio/climi/pioggia.png",34,1375,600,True)
		self.caricaImmagine ("09_abbraccio/climi/nubi.png",35,1375,600,True)
		self.caricaImmagine ("09_abbraccio/climi/nebbia.png",36,1375,600,True)
		self.caricaImmagine ("09_abbraccio/climi/sereno.png",37,1375,600,True)
		self.caricaImmagine ("09_abbraccio/climi/luna.png",38,1375,600,True)
		self.caricaImmagine ("09_abbraccio/climi/sole.png",39,1375,600,True)
		self.caricaImmagine ("09_abbraccio/climi/solissimo.png",40,1375,600,True)
		
	def show ( self ) :
		pass
	
	def routineVisibile (self, puntiToccati) :
		#self.i += 1
		#if (self.i%160 == 0):
		#	self.mostraImmagine ((self.i/160)%15,3900)
		#	self.mostraImmagine ((self.i/160)%15+self.NUMERO_CITTA,3900)
		for i in range (self.NUMERO_CITTA):
			if (puntiToccati[i]==1 and self.cod!=i) :
				self.mostraImmagine (i,-1)
				self.mostraImmagine (i+self.NUMERO_CITTA,-1)
				self.nascondiTutte ([i,i+self.NUMERO_CITTA])
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
