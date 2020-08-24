# If there is no await in the async code its of no use
# Developer or User needs to tell python (with await) where to context switch
# Async is concurrent not parallel...
# An awaitable object needs to be passed to await
# As soon as you put async infront of the function you make it a coroutine
# There's a specific way to call a coroutine, cannot be called like a normal function
# Use asyncio.run(coroutine()) --> Newer way does the same thing as creating, passing tasks and closing event loop


import time
import asyncio


# ----- Example 1 ----- #
async def main():
    print("Hello")
    await asyncio.sleep(0.50)
    print("World")

# # This way (older way)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()

# Or this way (newer way python 3.7+)
asyncio.run(main())





# ----- Example 2 ----- #
# For better use there always has to be a main co-routine
# And from the main co-routing you await all the other tasks.....
import asyncio
import time

async def printnum(num_start):
    while True:
        print("Num: {}".format(num_start))
        num_start +=1
        await asyncio.sleep(0.5)

async def time_passed():
    start_time = time.time()
    while True:
        current_time = time.time() - start_time
        print("Current Time: {}".format(current_time))
        await asyncio.sleep(0.5)

async def main():
    task1 = asyncio.create_task(printnum(1))
    task2 = asyncio.create_task(time_passed())
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    asyncio.run(main())





# ----- Example 3 ----- #
async def highest_num_divisible_by_8(num):
    print("Finding highest number below {}".format(num))
    print("Which is divisible by 8")
    #time.sleep(0.01)
    await asyncio.sleep(0.01)
    for i in range(num-1, 0, -1):
        if i % 8 == 0:
            return i
    return None

async def starter():
    t0 = time.time()
    await asyncio.wait([highest_num_divisible_by_8(100000),
                        highest_num_divisible_by_8(10000),
                        highest_num_divisible_by_8(1000)
                        ])
    t1 = time.time()
    print("Time taken: {} ms".format((t1-t0)*1000))

# All the three steps below are for python 3.6- (before)
loop = asyncio.get_event_loop()
loop.run_until_complete(starter())
loop.close()

# Python 3.7+ use this,
asyncio.run(starter())
