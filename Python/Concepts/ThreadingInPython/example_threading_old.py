import time
from threading import Thread

class ThreadWithReturnValue(Thread):
    def __init__(self, group = None, target = None, name = None, args = ..., kwargs = None, *, daemon = None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self._return= None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, timeout= None):
        super().join(timeout= timeout)
        return self._return
        
'''
How did I create this subclass? (shortcut checked a link)

Reading up on documentation.
looking into necessary variables and functions from the parent class.
overriding the necessary variables and functions in the subclass to tweak my needs.

Note: the link gave me the flow and the documentaion gave me clarity as to why its being done
'''   

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping for {seconds} second(s)...'

secs = [100,1]
threads = []

for sec in secs:
    t= ThreadWithReturnValue(target= do_something, args= [sec])
    t.start()
    threads.append(t)

for thread in threads:
    print(f"{thread.join()}") 

'''
To make threading.Thread return a value, a subclass that overrides the run() and join() functions need to be created and used.
'''

finish = time.perf_counter()

print(f'Finished in {round(finish-start,5)} second(s)')
