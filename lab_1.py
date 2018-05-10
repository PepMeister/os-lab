class Task:
	def __init__(self, taskName, actTime, execTime):
		self.name = taskName
		self.actTime = actTime
		self.execTime = execTime
		self.endOfExecutionTime = 0


class Dispatcher:
	def __init__(self, tasks):
		self.time = 0
		self.task_list = tasks
		self.currentTask = self.task_list.pop(0)
		self.currentTask.endOfExecutionTime = self.currentTask.execTime
		self.outOfTasks = False

	def inc_time(self):
		self.time += 1



	def skip(self, num):
		for i in range(num):
			print(str(self.time) + " " + "-")
			self.time += 1



	def check_current_task(self):
		if self.currentTask.endOfExecutionTime == self.time:
			if not self.task_list:
				self.outOfTasks = True
				return

			string = ""


			cur_task = self.task_list.pop(0)
			

			for task in self.task_list:
				if task.actTime <= self.time and not (cur_task.name == task.name):
					string = string + " " + task.name
				#print(string, " -в очереди")
				try:
					self.task_list.remove(cur_task)
				except ValueError:
					num = cur_task.actTime - self.time
					self.skip(num)
				self.currentTask = cur_task
				self.currentTask.endOfExecutionTime = self.time + self.currentTask.execTime


			print(self.time, "-task start time, ", cur_task.name, "-name of currenr task, ", "    ", string )



def print_task_list(taskList):
	for task in taskList:
		print("Имя: " + str(task.name) + " " + " Время активизации: " + str(task.actTime) +
			" Время выполнения: " + str(task.execTime))

def run_modeling(tasks):
	print('Время' + (" ")*len("-task start time, ") + "Задача" + (" ")*len( "-name of currenr task, ") + " Очередь")

	run = True
	print(0, "-task start time, ", str(tasks[0].name),  "-name of currenr task, ")
	dispatcher = Dispatcher(tasks)
	while run:
		dispatcher.check_current_task()
		dispatcher.inc_time()
		if dispatcher.outOfTasks:
			run = False



file = open("input", 'r')
tasks = []
for line in file:
	data = line.split()
	taskName = data[0]
	actTime = int(data[1])
	execTime = int(data[2])
	tasks.append(Task(taskName, actTime, execTime,))


tasks = sorted(tasks, key=lambda x: x.actTime)
print_task_list(tasks)
run_modeling(tasks)

