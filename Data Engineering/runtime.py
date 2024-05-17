# To check the runtime of a program

import time

# Get the current time before running the code

def runtime():

    start_time = time.time()
    for _ in range(1000000):
        pass

    # Get the current time after running the code
    end_time = time.time()

    # Calculate the difference to get the runtime
    run_time = end_time - start_time

    print("\nRuntime of this program is ", run_time, "seconds")
