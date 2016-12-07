import wx
from pagina import paginaSemplice

class pagina4 ( paginaSemplice ) :
	def __init__ ( self, parent , grandParent , index ) :
		paginaSemplice.__init__ ( self, parent , grandParent , index )
		
		#caricaImmagineDiSfondo (nome)
		self.caricaImmagineDiSfondo ("04_tessile/schermo.png")
		
		self.caricaImmagine("04_tessile/storiaArazzo.png",0);
		self.caricaVideo("04_tessile/videoPittrici.mp4",1);
		self.caricaVideo("04_tessile/videoCasarosa.mp4",2);
		self.caricaVideo("04_tessile/videoPieri.mp4",3);

		#associazioni.append ( (idVideo,linguetta,timeout=0) )
		self.associazioni.append((0,5,30000))
		self.associazioni.append((1,2))
		self.associazioni.append((2,16))
		self.associazioni.append((3,13))
