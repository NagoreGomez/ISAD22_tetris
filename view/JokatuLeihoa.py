import random
import sys
import tkinter as tk

import view.ongietorrileioa
from model.Tableroa import Tableroa
from model.Piezak import *
from controller.konexioa import Konexioa


abiadura=0
tamainax=0
tamainay=0

class JokatuLeihoa(object):
	"""docstring for JokatuLeioa"""

	def __init__(self,abiadura2,tamainax2,tamainay2,erab, puntuak, partida):
		super(JokatuLeihoa, self).__init__()



		self.window = tk.Tk()
		self.window.geometry('600x700') #LEHIOAREN TAMAINA
		self.window.title("Tetris jokoa")

		self.erabiltzailea = erab
		global erabiltzailea
		erabiltzailea=self.erabiltzailea


		#koloreaLortu
		fondoa=Konexioa.getAtzekoKolorea(Konexioa(), self.erabiltzailea)
		print(fondoa)
		#kolorea ezarri
		self.window['bg'] = fondoa

		#adreilu koloreak
		#Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma
		adreiluak = Konexioa.getAdreiluak(Konexioa(), self.erabiltzailea)
		print(adreiluak)
		if(adreiluak==1):
			self.laukiKol='blue'
			zutabeKol= 'blue'
			lForma= 'blue'
			lFormaAlderantzizkoKol= 'blue'
			zFormaKol= 'blue'
			zFormaAlderantzizkoKol= 'blue'
			tFormaKol='blue'
		elif(adreiluak==2):
			laukiKol = 'blue'
		else:
			laukiKol = 'blue'


		#soinua



		self.abiadura = abiadura2
		self.tamainax = tamainax2
		self.tamainay = tamainay2
		global abiadura
		global tamainax
		global tamainay
		abiadura = self.abiadura
		tamainax = self.tamainax
		tamainay = self.tamainay


		button = tk.Button(self.window, text="Partida hasi")
		button.pack()


		puntuazioa = tk.StringVar()
		puntuazioa.set(f"Puntuazioa: {puntuak}")

		puntuazioalabel = tk.Label(self.window, textvariable=puntuazioa, bg=fondoa)
		puntuazioalabel.pack()

		print(tamainax)
		print(tamainay)
		print(abiadura)
		print("aaaaaaaaaaaaaaaaaaaaaaaaaa")

		self.canvas = TableroaPanela(master=self.window, puntuazioalabel = puntuazioa, tamaina=(tamainax,tamainay), partida=partida)

		button.configure(command=self.canvas.jolastu)
		self.canvas.pack()

		#botonnnnnnnnnnnnnnnnnnnnnnnn
		if self.erabiltzailea is not None:
			button2 = tk.Button(self.window, text="Partida gorde", command=self.partidaGorde)
			button2.pack()

		self.window.bind("<Up>", self.canvas.joku_kontrola)
		self.window.bind("<Down>", self.canvas.joku_kontrola)
		self.window.bind("<Right>", self.canvas.joku_kontrola)
		self.window.bind("<Left>", self.canvas.joku_kontrola)

		# lehioa ondo ixteko
		self.window.protocol("WM_DELETE_WINDOW", sys.exit)
		self.window.mainloop()

	def partidaGorde (self):
		self.canvas.after_cancel(self.canvas.jokatzen)
		matrizea = self.canvas.tab
		gorde = str(matrizea.puntuazioa) + "#" + str(tamainax) + "#" + str(tamainay) + "#" + str(self.abiadura) + "#"
		for i in range(matrizea.tamaina[1]):
			for j in range(matrizea.tamaina[0]):

				if matrizea.tab[i][j] is None:
					gorde = gorde + "None#"
				else:
					gorde = gorde + matrizea.tab[i][j] + "#"
		Konexioa.partidaGorde(Konexioa(), self.erabiltzailea, gorde, self.canvas.tab.puntuazioa)
		self.window.destroy()

		view.erabiltzaileLeihoa.erabiltzaileLeihoa(self.erabiltzailea).__init__()

class TableroaPanela(tk.Frame):
	# EL TAMAINA DEL DEF NO EZARRITUA
	def __init__(self, tamaina=(tamainax,tamainay), gelazka_tamaina=20,puntuazioalabel=None, master=None, partida=None):
		tk.Frame.__init__(self, master)
		tamaina = (tamainax,tamainay)
		self.puntuazio_panela = puntuazioalabel
		self.tamaina = tamaina
		self.gelazka_tamaina = gelazka_tamaina
		self.partida=partida



		self.canvas = tk.Canvas(
			width=self.tamaina[0]  * self.gelazka_tamaina+1,
			height=self.tamaina[1] * self.gelazka_tamaina+1,
			bg='#eee', borderwidth=0, highlightthickness=0
		)
		self.canvas.pack(expand=tk.YES, fill=None)
		#print(tamaina)
		self.tab = Tableroa(tamaina)
		self.jokatzen = None
		self.tableroa_ezabatu()


	def marratu_gelazka(self, x,y,color):
		self.canvas.create_rectangle(x*self.gelazka_tamaina, y*self.gelazka_tamaina,
									(x+1)*self.gelazka_tamaina, (y+1)*self.gelazka_tamaina, fill=color)

	def tableroa_ezabatu(self):
		self.canvas.delete("all")
		self.canvas.create_rectangle(0, 0, self.tamaina[0] * self.gelazka_tamaina, self.tamaina[1] * self.gelazka_tamaina, fill='#eee')

	def marraztu_tableroa(self):
		self.tableroa_ezabatu()
		for i in range(self.tab.tamaina[1]):
			for j in range(self.tab.tamaina[0]):
				if self.tab.tab[i][j]:
					print(self.tab.tab[i][j])
					self.marratu_gelazka(j,i,self.tab.tab[i][j])
		if self.tab.pieza:
			for i in range(4):
				x = self.tab.posizioa[0] + self.tab.pieza.get_x(i)
				y = self.tab.posizioa[1] + self.tab.pieza.get_y(i)
				self.marratu_gelazka(y,x,self.tab.pieza.get_kolorea())
		self.puntuazioa_eguneratu()


	def pausu_bat(self):
		self.erabiltzailea=erabiltzailea
		try:
			self.tab.betetako_lerroak_ezabatu()
			self.tab.mugitu_behera()
		except Exception as error:
			try:
				self.tab.pieza_finkotu(self.tab.posizioa)
				pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
				self.tab.sartu_pieza(random.choice(pieza_posibleak)())
			except Exception as e:
				print("GAMEOVER")
				self.tab.hasieratu_tableroa()

				return
		self.jokatzen = self.after(abiadura, self.pausu_bat) #ABIADURA
		self.marraztu_tableroa()

	def puntuazioa_eguneratu(self):
		if self.puntuazio_panela:
			self.puntuazio_panela.set(f"Puntuazioa: {self.tab.puntuazioa}")



	def joku_kontrola(self, event):
		try:
			if event.keysym == 'Up':
				self.tab.biratu_pieza()
			if event.keysym == 'Down':
				self.tab.pieza_kokatu_behean()
			if event.keysym == 'Right':
				self.tab.mugitu_eskumara()
			if event.keysym == 'Left':
				self.tab.mugitu_ezkerrera()
		except Exception as error:
			pass
		finally:
			self.marraztu_tableroa()

	def jolastu(self):
		if self.jokatzen:
			self.after_cancel(self.jokatzen)
		if self.partida is not None:
			self.tab.kargatu_partida(self.partida)
		else:
			self.tab.hasieratu_tableroa()
		pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
		self.tab.sartu_pieza(random.choice(pieza_posibleak)())
		self.marraztu_tableroa()
		self.jokatzen = self.after(abiadura, self.pausu_bat)

