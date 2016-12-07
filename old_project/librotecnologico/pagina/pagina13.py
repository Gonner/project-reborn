#encoding: utf-8

from pagina import paginaSemplice

class pagina13 ( paginaSemplice ) :
	def __init__ ( self , parent , grandParent , index ) :
		paginaSemplice.__init__ ( self, parent , grandParent , index )
		self.caricaImmagineDiSfondo ("13_fiera/schermo.png")
