import wx
from pagina import paginaSemplice

class paginaChimica ( paginaSemplice ) :
	def __init__ ( self, parent , grandParent , index ) :
		paginaSemplice.__init__ ( self, parent , grandParent , index )
		
		#caricaImmagineDiSfondo (nome)
		self.caricaImmagineDiSfondo ("02_chimica/schermoCHIMICA.png")
		
		#caricaImmagine (nome, id, posX, posY, invisibile=True)
		self.caricaImmagine ("02_chimica/1picnometro.png",0,960,300)
		self.caricaImmagine ("02_chimica/2vigreux.png",1,1365,275)
		self.caricaImmagine ("02_chimica/3condensatore.png",2,935,630)
		self.caricaImmagine ("02_chimica/4schroedter.png",3,1350,575)
		self.caricaImmagine ("02_chimica/5beuta.png",4,890,860)
		self.caricaImmagine ("02_chimica/6capsula.png",5,1365,890)
		
		#associazioni.append ( (idImmagine,linguetta,timeout=0) )
		self.associazioni.append((0,13,5000))
		self.associazioni.append((1,16,5000))
		self.associazioni.append((2,4,5000))
		self.associazioni.append((3,10,5000))
		self.associazioni.append((4,1,5000))
		self.associazioni.append((5,7,5000))
		
