from pagina import paginaSemplice

class pagina16 ( paginaSemplice ) :
	def __init__ ( self , parent , grandParent , index ) :
		paginaSemplice.__init__ ( self, parent , grandParent , index )
		self.caricaImmagineDiSfondo ("16_RossiCecchi/schermo.png")
