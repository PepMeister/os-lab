#coding:UTF8

import sys
import time
import threading
from threading import Thread
import random

import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QMainWindow):

	lock = threading.Lock()
	D_E_F_start = 0
	K_start = 0
	M_arr = []
	R1_arr = []
	R2_arr = []


	def __init__(self):
		super().__init__()
		self.initUI()
		self.start_thread()


	def initUI(self):
		#self.start_thread()

		central_widget = QWidget(self)
		self.setCentralWidget(central_widget)

		self.bar_A = QProgressBar(self)
		self.bar_A.setGeometry(100, 40+10, 200, 25)
		self.bar_B = QProgressBar(self)
		self.bar_B.setGeometry(100, 65+20, 200, 25)
		self.bar_C = QProgressBar(self)
		self.bar_C.setGeometry(100, 90+30, 200, 25)
		self.bar_D = QProgressBar(self)
		self.bar_D.setGeometry(100, 115+40, 200, 25)
		self.bar_E = QProgressBar(self)
		self.bar_E.setGeometry(100, 140+50, 200, 25)
		self.bar_F = QProgressBar(self)
		self.bar_F.setGeometry(100, 165+60, 200, 25)
		self.bar_G = QProgressBar(self)
		self.bar_G.setGeometry(100, 190+70, 200, 25)
		self.bar_H = QProgressBar(self)
		self.bar_H.setGeometry(100, 215+80, 200, 25)
		self.bar_K = QProgressBar(self)
		self.bar_K.setGeometry(100, 240+90, 200, 25)

		self.label0 = QLabel(self)
		self.label0.move(20, 40+10)
		self.label0.resize(200, 25)
		self.label0.setText("Process A")
		self.label1 = QLabel(self)
		self.label1.move(20, 65+20)
		self.label1.resize(200, 25)
		self.label1.setText("Process B")
		self.label2 = QLabel(self)
		self.label2.move(20, 90+30)
		self.label2.resize(200, 25)
		self.label2.setText("Process C")
		self.label3 = QLabel(self)
		self.label3.move(20, 115+40)
		self.label3.resize(200, 25)
		self.label3.setText("Process D")
		self.label4 = QLabel(self)
		self.label4.move(20, 140+50)
		self.label4.resize(200, 25)
		self.label4.setText("Process E")
		self.label5= QLabel(self)
		self.label5.move(20, 165+60)
		self.label5.resize(200, 25)
		self.label5.setText("Process F")
		self.label6 = QLabel(self)
		self.label6.move(20, 190+70)
		self.label6.resize(200, 25)
		self.label6.setText("Process G")
		self.label7 = QLabel(self)
		self.label7.move(20, 215+80)
		self.label7.resize(200, 25)
		self.label7.setText("Process H")
		self.label8 = QLabel(self)
		self.label8.move(20, 240+90)
		self.label8.resize(200, 25)
		self.label8.setText("Process K")


		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('Файл')
		exitButton = QAction('Выход', self)
		exitButton.setShortcut('Ctrl+Q')
		exitButton.triggered.connect(self.close)
		fileMenu.addAction(exitButton)

		#self.setGeometry(300, 300, 289.5, 150)
		self.setWindowTitle('лабораторная работа oc, 2')
		self.show()



	def F1(self):
		self.lock.acquire()
		self.M_arr.append(0)
		self.R1_arr.append(False)
		self.R2_arr = self.R2_arr + self.R1_arr
		self.lock.release()
		return

	def F2(self):
		self.lock.acquire()
		self.M_arr.append(9)
		self.R1_arr.append(self.R2_arr.pop(0))
		self.R2_arr.append(False)
		self.lock.release()
		return

	def F3(self):
		self.lock.acquire()
		self.M_arr[0] = 4
		self.R1_arr[0] = False
		self.R2_arr.pop(0)
		self.lock.release()
		return

	def F4(self):
		self.F1()
		return

	def F5(self):
		self.F2()
		return

	def F6(self):
		self.F3()
		self.F4()
		self.F5()
		return


	def A(self):
		if self.D_E_F_start < 3 :
			self.M_arr = [[1,2,3,4],[5,6,7,8]]

			time.sleep(1/random.randint(2, 5))
			self.bar_A.setValue(25)
			time.sleep(1/random.randint(2, 5))
			self.bar_A.setValue(50)
			time.sleep(1/random.randint(2, 5))
			self.bar_A.setValue(75)
			time.sleep(1/random.randint(2, 5))
			self.bar_A.setValue(100)

			print("исходное состояние массива M: ", self.M_arr)
			self.lock.acquire()
			self.D_E_F_start+=1

			print('A() -', self.D_E_F_start)
			if self.D_E_F_start == 3:
				print("A завершила работу последней..")
				_d = Thread(target=self.D, args=())
				_e = Thread(target=self.E, args=())
				_f = Thread(target=self.F, args=())
				_d.daemon = True
				_e.daemon = True
				_f.daemon = True
				_d.start()
				_e.start()
				_f.start()
			self.lock.release()
			return

	def B(self):
		if self.D_E_F_start < 3 :
			self.R1_arr = [True, False, False, True]

			time.sleep(1/random.randint(2, 5))
			self.bar_B.setValue(25)
			time.sleep(1/random.randint(2, 5))
			self.bar_B.setValue(50)
			time.sleep(1/random.randint(2, 5))
			self.bar_B.setValue(75)
			time.sleep(1/random.randint(2, 5))
			self.bar_B.setValue(100)

			print("исходное состояние массива R1: ", self.R1_arr)
			self.lock.acquire()
			self.D_E_F_start+=1
			print('B() -', self.D_E_F_start)

			if self.D_E_F_start == 3:
				print("B завершила работу последней..")
				_d = Thread(target=self.D, args=())
				_e = Thread(target=self.E, args=())
				_f = Thread(target=self.F, args=())
				_d.daemon = True
				_e.daemon = True
				_f.daemon = True
				_d.start()
				_e.start()
				_f.start()
			self.lock.release()
			return

	def C(self):
		if self.D_E_F_start < 3 :
			self.R2_arr = [False, False, True, True]

			time.sleep(1/random.randint(2, 5))
			self.bar_C.setValue(25)
			time.sleep(1/random.randint(2, 5))
			self.bar_C.setValue(50)
			time.sleep(1/random.randint(2, 5))
			self.bar_C.setValue(75)
			time.sleep(1/random.randint(2, 5))
			self.bar_C.setValue(100)


			print("исходное состояние массива R2: ", self.R2_arr)
			self.lock.acquire()

			self.D_E_F_start+=1
			print('C() -', self.D_E_F_start)

			if self.D_E_F_start == 3:
				print("C завершила работу последней..")
				_d = Thread(target=self.D, args=())
				_e = Thread(target=self.E, args=())
				_f = Thread(target=self.F, args=())
				_d.daemon = True
				_e.daemon = True
				_f.daemon = True
				_d.start()
				_e.start()
				_f.start()
			self.lock.release()
			return

	def D(self):
		time.sleep(1/random.randint(2, 5))
		self.bar_D.setValue(25)
		time.sleep(1/random.randint(2, 5))
		self.bar_D.setValue(50)
		time.sleep(1/random.randint(2, 5))
		self.bar_D.setValue(75)
		time.sleep(1/random.randint(2, 5))
		self.bar_D.setValue(100)
		self.F1()
		print("активация процесса G")
		self.G()
		return

	def E(self):
		time.sleep(1/random.randint(2, 5))
		self.bar_E.setValue(25)
		time.sleep(1/random.randint(2, 5))
		self.bar_E.setValue(50)
		time.sleep(1/random.randint(2, 5))
		self.bar_E.setValue(75)
		time.sleep(1/random.randint(2, 5))
		self.bar_E.setValue(100)
		self.F2()
		print("активация процесса H")
		self.H()
		return

	def F(self):
		if self.K_start < 3:
			self.F3()

			time.sleep(1/random.randint(2, 5))
			self.bar_F.setValue(25)
			time.sleep(1/random.randint(2, 5))
			self.bar_F.setValue(50)
			time.sleep(1/random.randint(2, 5))
			self.bar_F.setValue(75)
			time.sleep(1/random.randint(2, 5))
			self.bar_F.setValue(100)


			self.lock.acquire()

			self.K_start+=1
			print('F() -', self.K_start)
			if self.K_start == 3:
				print("F завершила работу последней..")
				_k = Thread(target=self.K, args=())
				_k.daemon = True
				_k.start()
			self.lock.release()
			return

	def G(self):
		if self.K_start < 3:
			self.F4()

			time.sleep(1/random.randint(2, 5))
			self.bar_G.setValue(25)
			time.sleep(1/random.randint(2, 5))
			self.bar_G.setValue(50)
			time.sleep(1/random.randint(2, 5))
			self.bar_G.setValue(75)
			time.sleep(1/random.randint(2, 5))
			self.bar_G.setValue(100)

			self.lock.acquire()


			self.K_start+=1
			print('G() -', self.K_start)
			if self.K_start == 3:
				print("G завершила работу последней..")
				_k = Thread(target=self.K, args=())
				_k.daemon = True
				_k.start()
			self.lock.release()
			return

	def H(self):
		if self.K_start < 3:
			self.F5()

			time.sleep(1/random.randint(2, 5))
			self.bar_H.setValue(25)
			time.sleep(1/random.randint(2, 5))
			self.bar_H.setValue(50)
			time.sleep(1/random.randint(2, 5))
			self.bar_H.setValue(75)
			time.sleep(1/random.randint(2, 5))
			self.bar_H.setValue(100)

			self.lock.acquire()

			self.K_start+=1
			print('H() -', self.K_start)
			if self.K_start == 3:
				print("H завершила работу последней..")
				_k = Thread(target=self.K, args=())
				_k.daemon = True
				_k.start()
			self.lock.release()
			return

	def K(self):
		time.sleep(1/random.randint(2, 5))
		self.bar_K.setValue(25)
		time.sleep(1/random.randint(2, 5))
		self.bar_K.setValue(50)
		time.sleep(1/random.randint(2, 5))
		self.bar_K.setValue(75)
		time.sleep(1/random.randint(2, 5))
		self.bar_K.setValue(100)
		self.F6()
		print("процесс K завершен, результат:")
		self.print_result()
		return

	def print_result(self):
		print(" конечное состояние массива M: ", self.M_arr, '\n',
		 "конечное состояние массива R1: ", self.R1_arr, '\n', "конечное состояние массива R2: ", self.R2_arr )


	def start_thread(self):
		t1 = Thread(target=self.A, args=())
		t2 = Thread(target=self.B, args=())
		t3 = Thread(target=self.C, args=())
		t1.daemon = True
		t2.daemon = True
		t3.daemon = True
		t1.start()
		t2.start()
		t3.start()
#		self.A()
#		self.B()
#		self.C()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
