from pagina import pagina
import subprocess as sp
import os
import time

#per avviare ed uccidere un processo

#import subprocess as sp
#import signal
#
#child = sp.Popen( cmd , preexec_fn = os.setsid )


class pagina7 ( pagina ) :
	def __init__ ( self, parent , grandParent , index ) :
		pagina.__init__ ( self, parent , grandParent , index )
		
		self.puntiToccatiPrecedentemente=[]
		for i in range (0,19):
			self.puntiToccatiPrecedentemente.append(0)
		
		#se esiste, il software della lampada si interrompe
		self.fileChiusura="/tmp/chiudi.txt"
		#se esiste, la lampada scatta una foto
		self.fileScatta="/tmp/scattaFoto.txt"
		#la foto scattata finisce in questo file
		self.fotoScattata="/tmp/foto.png"
		#linea di comando per attivare la lampada
		self.comandoPerAttivareLaLampada="/home/arazzo/Lampada/bin/LampadaArazzoV1"
		
		#se toccata, la lampada scatta una foto
		self.linguettaScatta=12
		#se toccata, la lampada si avvia/si chiude
		self.linguettaAvvia=16
		self.lampadaAccesa=False
		self.controllaSeEsisteLaFoto=False
		
		self.caricaImmagineDiSfondo ("07_lampada/schermo.png")

	#todo: ne accende due
	def routineVisibile (self, puntiToccati):
		#print ("accesa: "+str(self.lampadaAccesa))
		#print ("linguette [a]: "+str(puntiToccati[self.linguettaAvvia])+" [s]: "+str(puntiToccati[self.linguettaScatta]))
		#print ("file esiste: "+str(os.path.isfile(self.fileChiusura)))
		if self.lampadaAccesa:
			if puntiToccati[self.linguettaAvvia] == 1 and self.puntiToccatiPrecedentemente[self.linguettaAvvia] == 0:
	                        print("PRIMA APERTURA TELECAMERA")
				f=open (self.fileChiusura, "wb")
				print("DOPO APERTURA TELECAMERA")
				f.close()
				#assert os.path.isfile (self.fileChiusura)
				self.lampadaAccesa=False
			if puntiToccati[self.linguettaScatta] == 1 and self.puntiToccatiPrecedentemente[self.linguettaScatta] == 0 and not self.controllaSeEsisteLaFoto:
				f=open (self.fileScatta, "wb")
				f.close()
				#assert os.path.isfile (self.fileScatta)
				self.controllaSeEsisteLaFoto=True
			if self.controllaSeEsisteLaFoto and os.path.isfile (self.fotoScattata):
				try:
					self.controllaSeEsisteLaFoto=False
					time.sleep(1)
					self.lampadaAccesa=False
					f=open (self.fileChiusura, "wb")
					f.close()
					self.caricaImmagine(self.fotoScattata,0,0,0,False,True)
					self.mostraImmagine(0,5000)
				except:
					print "Errore caricamento immagine."
		else: #lampada spenta
			if puntiToccati[self.linguettaAvvia] == 1 and self.puntiToccatiPrecedentemente[self.linguettaAvvia] == 0:
				child = sp.Popen( self.comandoPerAttivareLaLampada , preexec_fn = os.setsid )
				self.lampadaAccesa=True
		self.puntiToccatiPrecedentemente=puntiToccati

	def hide (self):
		if self.lampadaAccesa:
			self.lampadaAccesa=False
			f=open (self.fileChiusura, "wb")
			f.close()

