from pagina import pagina


#TODO: scrivere
class pagina15 ( pagina ) :
	def __init__ ( self , parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		
		self.puntiToccatiPrecedentemente=[]
		for i in range (0,19):
			self.puntiToccatiPrecedentemente.append(0)
		
		#sfondo
		self.caricaImmagineDiSfondo ("15_pianoforte/schermo.png")
		
		#tasti normali
		self.caricaImmagine ("15_pianoforte/t0n.png",0,213,352,False)
		self.caricaImmagine ("15_pianoforte/t1n.png",1,283,349,False)
		self.caricaImmagine ("15_pianoforte/t2n.png",2,346,345,False)
		self.caricaImmagine ("15_pianoforte/t3n.png",3,431,340,False)
		self.caricaImmagine ("15_pianoforte/t4n.png",4,494,337,False)
		self.caricaImmagine ("15_pianoforte/t5n.png",5,594,332,False)
		self.caricaImmagine ("15_pianoforte/t6n.png",6,658,336,False)
		self.caricaImmagine ("15_pianoforte/t7n.png",7,778,323,False)
		self.caricaImmagine ("15_pianoforte/t8n.png",8,859,318,False)
		self.caricaImmagine ("15_pianoforte/t9n.png",9,986,311,False)
		self.caricaImmagine ("15_pianoforte/t10n.png",10,1100,303,False)
		
		#tasti pigiati
		self.caricaImmagine ("15_pianoforte/t0p.png",11,208,351)
		self.caricaImmagine ("15_pianoforte/t1p.png",12,279,348)
		self.caricaImmagine ("15_pianoforte/t2p.png",13,343,345)
		self.caricaImmagine ("15_pianoforte/t3p.png",14,429,340)
		self.caricaImmagine ("15_pianoforte/t4p.png",15,494,336)
		self.caricaImmagine ("15_pianoforte/t5p.png",16,595,331)
		self.caricaImmagine ("15_pianoforte/t6p.png",17,659,336)
		self.caricaImmagine ("15_pianoforte/t7p.png",18,780,323)
		self.caricaImmagine ("15_pianoforte/t8p.png",19,861,318)
		self.caricaImmagine ("15_pianoforte/t9p.png",20,989,310)
		self.caricaImmagine ("15_pianoforte/t10p.png",21,1101,302)
		
		#suoni
		
		#self.caricaVideo ("15_pianoforte/00_si.ogg",22,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/01_do.ogg",23,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/02_re.ogg",24,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/03_mi.ogg",25,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/04_fa.ogg",26,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/05_sol.ogg",27,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/06_la.ogg",28,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/07_si.ogg",29,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/08_do.ogg",30,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/09_re.ogg",31,0,0,0,0)
		#self.caricaVideo ("15_pianoforte/10_mi.ogg",32,0,0,0,0)
		
		self.numeroNote=11

		
	def show ( self ) :
		pass
			
	def routineVisibile (self, puntiToccati) :
		for i in range (self.numeroNote):
			if puntiToccati[i] != self.puntiToccatiPrecedentemente[i]:
				if puntiToccati[i] == 1:
					self.playVideo (i+self.numeroNote*2)
					self.mostraTastoPigiato (i)
				else:
					self.stopVideo (i+self.numeroNote*2)
					self.mostraTastoNormale (i)
		self.puntiToccatiPrecedentemente=puntiToccati
				
	def routineInvisibile (self) :
		pass

	def mostraTastoPigiato (self, i):
		self.nascondiImmagine (i)
		self.mostraImmagine (i+self.numeroNote)
		
	def mostraTastoNormale (self, i):
		self.nascondiImmagine (i+self.numeroNote)
		self.mostraImmagine (i)
