#coding:UTF8

import sys
import time
import threading
from threading import Thread


lock = threading.Lock()
D_E_F_start = 0
K_start = 0

def F1():
	lock.acquire()
	A.M_arr.append(0)
	time.sleep(0.3)
	B.R1_arr.append(False)
	C.R2_arr = C.R2_arr + B.R1_arr
	lock.release()
	return

def F2():
	lock.acquire()
	A.M_arr.append(9)
	time.sleep(0.5)
	B.R1_arr.append(C.R2_arr.pop(0))
	C.R2_arr.append(False)
	lock.release()
	return

def F3():
	lock.acquire()
	A.M_arr[0] = 4
	time.sleep(0.1)
	B.R1_arr[0] = False
	C.R2_arr.pop(0)
	lock.release()
	return

def F4():
	F1()
	return

def F5():
	F2()
	return

def F6():
	F3()
	F4()
	F5()
	return


def A():
	A.M_arr = [[1,2,3,4],[5,6,7,8]]
	time.sleep(0.2)
	print("исходное состояние массива M: ", A.M_arr)
	lock.acquire()
	global D_E_F_start
	D_E_F_start+=1
	print('A() -', D_E_F_start)
	if D_E_F_start == 3:
		print("A завершила работу последней..")
		_d = Thread(target=D, args=())
		_e = Thread(target=E, args=())
		_f = Thread(target=F, args=())
		_d.daemon = True
		_e.daemon = True
		_f.daemon = True
		_d.start()
		_e.start()
		_f.start()
	lock.release()
	return

def B():
	B.R1_arr = [True, False, False, True]
	time.sleep(0.4)
	print("исходное состояние массива R1: ",B.R1_arr)
	lock.acquire()
	global D_E_F_start
	D_E_F_start+=1
	print('B() -', D_E_F_start)
	if D_E_F_start == 3:
		print("B завершила работу последней..")
		_d = Thread(target=D, args=())
		_e = Thread(target=E, args=())
		_f = Thread(target=F, args=())
		_d.daemon = True
		_e.daemon = True
		_f.daemon = True
		_d.start()
		_e.start()
		_f.start()
	lock.release()
	return

def C():
	C.R2_arr = [False, False, True, True]
	time.sleep(0.1)
	print("исходное состояние массива R2: ", C.R2_arr)
	lock.acquire()
	global D_E_F_start
	D_E_F_start+=1
	print('C() -', D_E_F_start)
	if D_E_F_start == 3:
		print("C завершила работу последней..")
		_d = Thread(target=D, args=())
		_e = Thread(target=E, args=())
		_f = Thread(target=F, args=())
		_d.daemon = True
		_e.daemon = True
		_f.daemon = True
		_d.start()
		_e.start()
		_f.start()
	lock.release()
	return

def D():
	F1()
	print("активация процесса G")
	G()
	return

def E():
	F2()
	print("активация процесса H")
	H()
	return

def F():
	F3()
	lock.acquire()
	global K_start
	K_start+=1
	print('F() -', K_start)
	if K_start == 3:
		print("F завершила работу последней..")
		_k = Thread(target=K, args=())
		_k.daemon = True
		_k.start()
	lock.release()
	return

def G():
	F4()
	lock.acquire()
	global K_start
	K_start+=1
	print('G() -', K_start)
	if K_start == 3:
		print("G завершила работу последней..")
		_k = Thread(target=K, args=())
		_k.daemon = True
		_k.start()
	lock.release()
	return

def H():
	F5()
	lock.acquire()
	global K_start
	K_start+=1
	print('H() -', K_start)
	if K_start == 3:
		print("H завершила работу последней..")
		_k = Thread(target=K, args=())
		_k.daemon = True
		_k.start()
	lock.release()
	return

def K():
	F6()
	print("процесс K завершен, результат:")
	print_result()
	return

def print_result():
	print(" конечное состояние массива M: ", A.M_arr, '\n',
	 "конечное состояние массива R1: ", B.R1_arr, '\n', "конечное состояние массива R2: ", C.R2_arr )



def main():
	t1 = Thread(target=A, args=())
	t2 = Thread(target=B, args=())
	t3 = Thread(target=C, args=())
	t1.daemon = True
	t2.daemon = True
	t3.daemon = True
	t1.start()
	t2.start()
	t3.start()


if __name__=="__main__":
	main()
