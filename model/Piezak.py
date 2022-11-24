from controller.konexioa import Konexioa
erabiltzailea=""

class Pieza:
	def __init__(self, forma, kolorea):
		self.forma = forma
		self.kolorea = kolorea


	def get_kolorea(self):
		return self.kolorea
	def get_x(self, i):
		return self.forma[i][0]
	def get_y(self, i):
		return self.forma[i][1]

	def set_x(self, i,b):
		self.forma[i][0] = b
	def set_y(self, i,b):
		self.forma[i][1] = b


	def biratuEzkerrera(self):
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)

			self.set_x(i, aurr_y)
			self.set_y(i, -aurr_x)

	def biratuEskuinera(self):
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)

			self.set_x(i, -aurr_y)
			self.set_y(i, aurr_x)

	def min_x(self):
		return min([x[0] for x in self.forma])
	def min_y(self):
		return min([x[1] for x in self.forma])


class Laukia(Pieza):
	def __init__(self, kolorea=None):
		koloreKodea=Konexioa.getAdreiluak(Konexioa(),erabiltzailea)

		if(koloreKodea=='1'):
			kolorea2='#ADFF2F'
		elif(koloreKodea=='2'):
			kolorea2='#4169E1'
		else:
			kolorea2 = 'yellow'
		super(Laukia, self).__init__([[0, 0], [0, 1], [1, 0], [1, 1]], kolorea=kolorea2)


class Zutabea(Pieza):
	def __init__(self, kolorea=None):
		koloreKodea = Konexioa.getAdreiluak(Konexioa(), erabiltzailea)

		if (koloreKodea == '1'):
			kolorea2 = '#F5DEB3'
		elif (koloreKodea == '2'):
			kolorea2 = '#9B30FF'
		else:
			kolorea2 = 'cyan'
		super(Zutabea, self).__init__([[0,-1],[0,0],[0,1],[0,2]], kolorea=kolorea2)



class Lforma(Pieza):
	def __init__(self, kolorea=None):
		koloreKodea = Konexioa.getAdreiluak(Konexioa(), erabiltzailea)

		if (koloreKodea == '1'):
			kolorea2 = '#FF8000'
		elif (koloreKodea == '2'):
			kolorea2 = '#87CEEB'
		else:
			kolorea2 = 'blue'
		super(Lforma, self).__init__([[-1,-1],[0,-1],[0,0],[0,1]], kolorea=kolorea2)

class LformaAlderantzizko(Pieza):

	def __init__(self, kolorea=None):
		koloreKodea = Konexioa.getAdreiluak(Konexioa(), erabiltzailea)

		if (koloreKodea == '1'):
			kolorea2 = '#FF4500'
		elif (koloreKodea == '2'):
			kolorea2 = '#40E0D0'
		else:
			kolorea2 = 'orange'
		super(LformaAlderantzizko, self).__init__([[1,-1],[0,-1],[0,0],[0,1]], kolorea=kolorea2)


class Zforma(Pieza):
	def __init__(self, kolorea=None):
		koloreKodea = Konexioa.getAdreiluak(Konexioa(), erabiltzailea)

		if (koloreKodea == '1'):
			kolorea2 = '#DA70D6'
		elif (koloreKodea == '2'):
			kolorea2 = '#872657'
		else:
			kolorea2 = 'green'
		super(Zforma, self).__init__([[0,-1],[0,0],[-1,0],[-1,1]], kolorea=kolorea2)

class ZformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None):
		koloreKodea = Konexioa.getAdreiluak(Konexioa(), erabiltzailea)

		if (koloreKodea == '1'):
			kolorea2 = '#FFC0CB'
		elif (koloreKodea == '2'):
			kolorea2 = '#00008B'
		else:
			kolorea2 = 'red'
		super(ZformaAlderantzizko, self).__init__([[0,-1],[0,0],[1,0],[1,1]], kolorea=kolorea2)

class Tforma(Pieza):
	def __init__(self, kolorea=None):
		koloreKodea = Konexioa.getAdreiluak(Konexioa(), erabiltzailea)

		if (koloreKodea == '1'):
			kolorea2 = '#8B3626'
		elif (koloreKodea == '2'):
			kolorea2 = '#006400'
		else:
			kolorea2 = 'purple'
		super(Tforma, self).__init__([[-1,0],[0,0],[1,0],[0,1]], kolorea=kolorea2)