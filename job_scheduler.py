import time;
import threading;

class TaskScheduler:
    def __init__(self):
        self.tasks = [];
        self.pollingThread = threading.Thread(target = self.poll)

    def start(self):
        self.pollingThread.start();
    def poll(self):

        while True and self.tasks:
            now = time.time() * 1000;

            for index in range(len(self.tasks)):
                task = self.tasks[index];
                startTime = task[1];
                if now >= startTime:
                    fn = task[0];
                    fn();
            self.tasks = [_ for _ in self.tasks if _[1] > now ]
            time.sleep(0.1);
        print('end schedule');




    def addTask(self,fn,delay):
        startTime = (time.time() * 1000) + delay;
        task = (fn,startTime);
        self.tasks.append(task);


def printWord():
    print('hello world');



scheduler = TaskScheduler();
scheduler.addTask(printWord,3000);
scheduler.addTask(printWord,6000);
scheduler.addTask(printWord,8000);
scheduler.start();


























# import time
# import threading
#
#
#
# class Scheduler:
#     def __init__(self):
#         self.fns = [] # tuple of (fn, time)
#         self.t = threading.Thread(target=self.poll)
#     def start(self):
#         self.t.start();
#
#     def poll(self):
#         while True and self.fns:
#             # print('polling' + str(<time class="tim"></time>e()));
#             now = time.time()*1000
#             for fn, due in self.fns:
#                 if now >= due:
#                     fn()
#             self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
#             time.sleep(0.01)
#
#     def delay(self, f, n):
#
#         self.fns.append((f, (time.time()*1000) + n))
#
#
#
#
# def printTime():
#     print('1 I am task No.' + str(time.time()));
#
# def printTime2():
#     print('2 I am task No.' + str(time.time()));
#
#
#
# sch = Scheduler();
# sch.delay(printTime,3500);
# sch.start();
