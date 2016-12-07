from pagina import paginaSemplice

#CREATED BY ALESSIO FALAI & LORENZO PRATESI

class pagina3 ( paginaSemplice ) :
	def __init__ ( self , parent , grandParent , index ) :
		paginaSemplice.__init__ ( self, parent , grandParent , index )
		
		self.caricaImmagineDiSfondo ("03_elettronica/schermo.png")
		
		#caricaImmagine (nome, id, posX, posY, invisibile=True)
		self.caricaImmagine ("03_elettronica/alunni/1.png",0,177,0)
		self.caricaImmagine ("03_elettronica/alunni/2.png",1,191,0)
		self.caricaImmagine ("03_elettronica/alunni/3.png",2,247,0)
		self.caricaImmagine ("03_elettronica/alunni/4.png",3,295,0)
		self.caricaImmagine ("03_elettronica/alunni/5.png",4,355,0)
		self.caricaImmagine ("03_elettronica/alunni/6.png",5,256,0)
		self.caricaImmagine ("03_elettronica/alunni/7.png",6,136,0)
		self.caricaImmagine ("03_elettronica/alunni/8.png",7,217,0)
		self.caricaImmagine ("03_elettronica/alunni/9.png",8,0,0)
		
		#associazioni.append ( (idImmagine,linguetta,timeout=0) )
		self.associazioni.append((0,15,5000))
		self.associazioni.append((1,10,5000))
		self.associazioni.append((2,12,5000))
		self.associazioni.append((3,7,5000))
		self.associazioni.append((4,1,5000))
		self.associazioni.append((5,2,5000))
		self.associazioni.append((6,4,5000))
		self.associazioni.append((7,5,5000))
		self.associazioni.append((8,8,5000))
