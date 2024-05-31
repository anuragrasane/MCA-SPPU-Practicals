#8.4 Write a python program for synchronizing the thread.
import threading

# This function will be run by the threads
def thread_function(name, lock):
    with lock:
        # Critical section of code
        print(f"Thread {name} is running")
        # ... perform operations

# Create a lock object
lock = threading.Lock()

# Create threads
threads = []
for i in range(5):
    thread = threading.Thread(target=thread_function, args=(i, lock))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished execution.")
