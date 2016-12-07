# -*- coding: utf-8 -*-
import wx
from pagina import pagina

class pagina0 ( pagina ) :
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		self.caricaImmagineDiSfondo ("00_copertina/schermo.png")
#		self.caricaVideo ("cacca/video.flv",0)
				
	def show ( self ) :
		pass
		
	def routineVisibile (self, puntiToccati) :
		pass
		
	def routineInvisibile (self) :
		pass

	def hide (self):
		pass
