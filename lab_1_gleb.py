class Task:
	def __init__(self, taskName, actTime, execTime, priority):
		self.name = taskName
		self.actTime = actTime
		self.execTime = execTime
		self.endOfExecutionTime = 0
		self.priority = priority

class Dispatcher:
	def __init__(self, tasks):
		self.time = 0
		self.task_list = tasks
		self.queue = []
		self.currentTask = self.task_list.pop(0)
		self.currentTask.endOfExecutionTime = self.currentTask.execTime
		self.outOfTasks = False

	def inc_time(self):
		self.time += 1


	def print_info(self): 
		for task in self.task_list:


			if task.actTime == self.time:
				self.queue.append(task.name)
		out = "" 
		for sym in self.queue: 
			out += sym + " " 
		print(str(self.time) + " " + self.currentTask.name + " " + out)


	def skip(self, num): 
		for i in range(num): 
			print(str(self.time) + " " + "-") 
			self.time += 1


	def check_current_task(self): 
		if self.currentTask.endOfExecutionTime == self.time: 
			if not self.task_list: 
				self.outOfTasks = True 
				return

			cur_task = self.task_list[0] 
			for task in self.task_list:
				if cur_task.priority < task.priority and task.name in self.queue:
					cur_task = task
			try:
				self.task_list.remove(cur_task)
				self.queue.remove(cur_task.name)
			except ValueError:
			    num = cur_task.actTime - self.time 
			    self.skip(num)

			self.currentTask = cur_task 
			self.currentTask.endOfExecutionTime = self.time + self.currentTask.execTime


def print_task_list(taskList): 
	for task in taskList:
	    print("Имя: " + str(task.name) + " " + " Время активизации: " + str(task.actTime) + " Время выполнения: " + str(task.execTime) + " Приоритет: " + str(task.priority))



def run_modeling(tasks):
    print('t' + " " + "Задача" + " Очередь") 
    run = True 
    dispatcher = Dispatcher(tasks) 
    while run:
    	dispatcher.print_info() 
    	dispatcher.inc_time() 
    	dispatcher.check_current_task() 
    	if dispatcher.outOfTasks: 
    	    run = False



file = open("input_", 'r') 
tasks = [] 
for line in file: 
	data = line.split() 
	taskName = data[0] 
	actTime = int(data[1])
	execTime = int(data[2])
	priority = int(data[3])
	tasks.append(Task(taskName, actTime, execTime, priority))


tasks = sorted(tasks, key=lambda x: x.execTime)
print_task_list(tasks) 
run_modeling(tasks)
