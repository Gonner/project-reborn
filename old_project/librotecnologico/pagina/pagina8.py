from pagina import paginaSemplice

class pagina8 ( paginaSemplice ) :
	def __init__ ( self , parent , grandParent , index ) :
		paginaSemplice.__init__ ( self, parent , grandParent , index )
		self.caricaImmagineDiSfondo ("08_facce/schermo.png")
		
		self.caricaImmagine("08_facce/cornice8.png",0);
		self.caricaImmagine("08_facce/cornice10.png",1);
		self.caricaImmagine("08_facce/cornice7.png",2);
		self.caricaImmagine("08_facce/cornice9.png",3);
		self.caricaImmagine("08_facce/cornice11.png",4);
		self.caricaImmagine("08_facce/cornice3.png",5);
		self.caricaImmagine("08_facce/cornice6.png",6);
		self.caricaImmagine("08_facce/cornice1.png",7);
		self.caricaImmagine("08_facce/cornice4.png",8);
		self.caricaImmagine("08_facce/cornice2.png",9);
		self.caricaImmagine("08_facce/cornice5.png",10);

		#associazioni.append ( (idVideo,linguetta,timeout=0) )
		self.associazioni.append((5,2,30000))
		self.associazioni.append((6,5,30000))
		self.associazioni.append((7,8,30000))
		self.associazioni.append((8,11,30000))
		self.associazioni.append((9,15,30000))
		self.associazioni.append((0,1,30000))
		self.associazioni.append((1,3,30000))
		self.associazioni.append((2,6,30000))
		self.associazioni.append((3,9,30000))
		self.associazioni.append((4,12,30000))
		self.associazioni.append((10,0,30000))
