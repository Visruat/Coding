import time
import concurrent.futures 

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    # print(f'Done Sleeping for {seconds}')
    return f'Done Sleeping for {seconds} second(s)...'

secs = [_ for _ in range(100,0,-10)]

with concurrent.futures.ThreadPoolExecutor() as exe:
    threads= [exe.submit(do_something, sec) for sec in secs]
    
    for f in concurrent.futures.as_completed(threads):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start,5)} second(s)')
