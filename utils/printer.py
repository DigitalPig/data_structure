'''
Utilization of Queue for Printer cases
'''

from ds import Queue
import random

class pjob():
    '''
    Printing job
    '''

    def __init__(self, pages):
        self.pages = pages
        self.wait_time = 0
        self._done = False

    def get_pages(self):
        return self.pages

    def printing(self, delta):
        self.pages -= delta
        return self.pages

    def add_wait_time(self):
        self.wait_time += 1

    def get_wait_time(self):
        return self.wait_time

class printer_q():
    '''
    Printer Queue
    '''

    def __init__(self, speed=20):
        self._queue = Queue()
        self._finish = []
        self.speed = speed
        self.t_time = 0
        self.current_job = None
        self._done = False

    def add_job(self,job):
        print('add printing job with pages: ', job.get_pages())
        self._queue.enqueue(job)

    def work(self):
        '''
        Work function
        Start to work until the queue is empty
        '''
        if self._done:
            return self._done
        elif self._queue.isEmpty:
            self._done = True
            return self._done

        # We need to do work
        if self.current_job is None:
            if self._queue.isEmpty:
                self._done = True
                return True
            else:
                self._done = False
                self.current_job = self._queue.dequeue()

        if (self.current_job.printing(self.speed) <= 0):
            # Loop over all remaining queues
            for i in self._queue._contents:
                i.add_wait_time()
            self._finish.append(self.current_job)
            self.current_job = None
            self._done = False
            return self._done
        else:
            for i in self._queue._contents:
                i.add_wait_time()
            self._done = False
            return self._done

    def get_total_time(self):
        self.t_time = sum([x.get_wait_time() for x in self._finish]) / len(self._finish)
        return self.t_time

if __name__ == '__main__':
    total_jobs = 10
    cum_total = 0
    pq = printer_q()
    # Create the first job
    page = random.randint(1,20)
    pq.add_job(pjob(page))
    cum_total += 1
    while (cum_total < total_jobs):
        if_job_or_not = random.randint(1,180)
        if if_job_or_not >= 20:
            pq.add_job(pjob(random.randint(1,20)))
            cum_total += 1
        pq.work()
    while (not pq.work()) :
        pq.work()

    print('total wait time is: ', pq.get_total_time())
