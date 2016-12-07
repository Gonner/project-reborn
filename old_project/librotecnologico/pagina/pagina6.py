import wx
from pagina import paginaSemplice

#TODO: mancano i video
class pagina6 ( paginaSemplice ) :
	def __init__ ( self, parent , grandParent , index ) :
		paginaSemplice.__init__ ( self, parent , grandParent , index )
		
		#caricaImmagineDiSfondo (nome)
		self.caricaImmagineDiSfondo ("06_informatici/schermo.png")
		
		#caricaVideo (nome, id, posX, posY, invisibile=True)
		
		#self.caricaVideo("06_informatici/videoPagine.avi",0,0,0,1920,1080);
		#self.caricaVideo("06_informatici/videoFacce.mp4",1,0,0,1920,1080);
		#self.caricaVideo("06_informatici/videoLampada.mp4",2);
		#self.caricaVideo("06_informatici/videoLibro.avi",3,0,0,1920,1080);
		
		#associazioni.append ( (idVideo,linguetta,timeout=0) )
		
		#self.associazioni.append((0,3))
		#self.associazioni.append((1,8))
		#self.associazioni.append((2,12))
		#self.associazioni.append((3,15))
