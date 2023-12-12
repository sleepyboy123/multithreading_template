import threading
import time

# Shared array among threads
shared_array = []

# Function that each thread will run
def thread_function(thread_id):
    global shared_array
    time.sleep(5)
    print(f"Thread {thread_id}")

# Number of threads to create
num_threads = 3

# Create and start threads
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=thread_function, args=(i,))
    thread.start()
    threads.append(thread)

# Main thread can continue to execute code here
print("Main thread")

# Wait for all threads to finish before continuing with main thread
for thread in threads:
    thread.join()
