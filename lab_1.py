import time 


class Task:
	def __init__(self, taskName, actTime, execTime):
		self.name = taskName
		self.actTime = actTime
		self.execTime = execTime
		self.endOfExecutionTime = 0


class Dispatcher(): #Task):
	def __init__(self, tasks):
		self.time = 0
		self.task_list = tasks
		self.currentTask =  Task("",0, self.task_list[0].actTime)
		self.currentTask.endOfExecutionTime = self.currentTask.execTime
		self.outOfTasks = False


	def inc_time(self):
		self.time += 1


	def skip(self, num):
		for i in range(num):
			print(str(self.time) + " " + "-")
			self.time += 1


	def print_task_state(self):
		string = ""
		for task in self.task_list:
				if task.actTime <= self.time and not (self.currentTask.name == task.name):
					string = string + " " + task.name
		print(self.time, (" ")*(7+len("Имя")), self.currentTask.name, (" ")*(7+len("Задача")), string)



	def check_current_task(self):

		if self.currentTask.endOfExecutionTime == self.time:

			if len(self.task_list) == 0:
				self.outOfTasks = True
				return

			self.currentTask = self.task_list.pop(0)

			for task in self.task_list:
				try:
					self.task_list.remove(self.currentTask)
				except ValueError:
					num = self.currentTask.actTime - self.time
					self.skip(num)
			self.currentTask.endOfExecutionTime = self.time + self.currentTask.execTime


def print_task_list(taskList):
	for task in taskList:
		print("Имя: " + str(task.name) + " " + " Время активизации: " + str(task.actTime) +
			" Время выполнения: " + str(task.execTime))


def run_modeling(tasks):
	print('Время' + (" ")*7 + "Задача" + (" ")*7 + " Очередь")

	dispatcher = Dispatcher(tasks)
	while not dispatcher.outOfTasks:

		dispatcher.check_current_task()
		dispatcher.print_task_state()
		dispatcher.inc_time()




file = open("input", 'r')
tasks = []
for line in file:
	data = line.split()
	taskName = data[0]
	actTime = int(data[1])
	execTime = int(data[2])
	tasks.append(Task(taskName, actTime, execTime))

tasks = sorted(tasks, key=lambda x: x.actTime)
print_task_list(tasks)
run_modeling(tasks)

