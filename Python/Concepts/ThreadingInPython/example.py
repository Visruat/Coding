import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping for {seconds}'

a = do_something(1)
b = do_something(2)

finish = time.perf_counter()

print(f'Finished in {round(finish-start,5)} second(s)')
