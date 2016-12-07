import wx
from pagina import pagina

class paginaAbbraccio ( pagina ) :
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		self.linguette=[]
		
		self.caricaImmagineDiSfondo ("09_abbraccio/schermo.png")
		
		self.i=0
		self.NUMERO_CLIMI=10
		self.FILE_OUTPUT="/tmp/citta"
		
		self.caricaImmagine ("09_abbraccio/climi/neve.png",0,1375,400,True)
		self.caricaImmagine ("09_abbraccio/climi/fulmini.png",1,1375,400,True)
		self.caricaImmagine ("09_abbraccio/climi/temporale.png",2,1375,400,True)
		self.caricaImmagine ("09_abbraccio/climi/pioggia.png",3,1375,400,True)
		self.caricaImmagine ("09_abbraccio/climi/nubi.png",4,1375,400,True)
		self.caricaImmagine ("09_abbraccio/climi/nebbia.png",5,1375,400,True)
		self.caricaImmagine ("09_abbraccio/climi/sereno.png",6,1375,400,True)
		self.caricaImmagine ("09_abbraccio/climi/luna.png",7,1375,400,True)
		self.caricaImmagine ("09_abbraccio/climi/sole.png",8,1375,400,True)
		self.caricaImmagine ("09_abbraccio/climi/solissimo.png",9,1375,400,True)
		
		
		#associazioni codice clima - linguetta
		self.linguette.append (3) #codice 0 - neve ha linguetta 3
		self.linguette.append (0) #codice 1 - fulmini ha linguetta 0
		self.linguette.append (2) #codice 2 - temporale ha linguetta 2
		self.linguette.append (13) #codice 3 - pioggia ha linguetta 13
		self.linguette.append (4) #codice 4 - nubi ha linguetta 4
		self.linguette.append (10) #codice 5 - nebbia ha linguetta 10
		self.linguette.append (6) #codice 6 - sereno ha linguetta 6
		self.linguette.append (7) #codice 7 - luna ha linguetta 7
		self.linguette.append (5) #codice 8 - sole ha linguetta 5
		self.linguette.append (1) #codice 9 - solissimo ha linguetta 1

	def show ( self ) :
		pass
	
	def routineVisibile (self, puntiToccati) :
		#self.i += 1
		#if (self.i%160 == 0):
		#	self.mostraImmagine ((self.i/160)%10,3900)
		for i in range (self.NUMERO_CLIMI):
			if ( puntiToccati[ self.linguette[i] ]==1 ) :
				self.interrogaDemone (i)
				self.mostraImmagine (i,-1)
				self.nascondiTutte ([i])


	def routineInvisibile (self) :
		pass

	def interrogaDemone (self, idClima):
		f=open (self.FILE_OUTPUT, "w")
		f.write (str(idClima))
		f.close ()
