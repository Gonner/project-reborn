import wx
from pagina import pagina


class pagina14 ( pagina ) :
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		self.caricaImmagineDiSfondo ("14_castello/schermo.png")
		
		#self.caricaImmagine("14_castello/imperatore1.png",0,264,124)
		self.caricaImmagine("14_castello/imperatore2.png",1,264,567)
		self.caricaImmagine("14_castello/arazzo1.png",2,1012,58)
		self.caricaImmagine("14_castello/arazzo2.png",3,1012,579)
		self.liguetta10 = 10
		self.liguetta4 = 4
		
	def routineVisibile ( self, puntiToccati ):
		if puntiToccati[self.liguetta4] == 1 :
			self.nascondiTutte()
			self.mostraImmagine(1,30000)
			self.mostraImmagine(3,30000)
		if puntiToccati[self.liguetta10] == 1 :
			self.nascondiTutte()
			self.mostraImmagine(0,30000);
			self.mostraImmagine(2,30000)
