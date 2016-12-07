import wx
from pagina import paginaSemplice

#TODO: mancano i video
class pagina5 ( paginaSemplice ) :
	def __init__ ( self, parent , grandParent , index ) :
		paginaSemplice.__init__ ( self, parent , grandParent , index )
		
		#caricaImmagineDiSfondo (nome)
		self.caricaImmagineDiSfondo ("05_meccanici/schermo.png")
		
		#self.caricaVideo("05_meccanici/videoMeccanici.wmv",0,0,0,1920,1080);
		self.caricaImmagine("05_meccanici/struttura.png",1,1090,130);

		#associazioni.append ( (idVideo,linguetta,timeout=0) )
		#self.associazioni.append((0,11))
		self.associazioni.append((1,8,30000))
