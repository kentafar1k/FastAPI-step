import asyncio

async def my_task():
    print("Start task")
    await asyncio.sleep(1)
    print("End task")

asyncio.run(my_task())

# без асинхронки
import time

def task():
    print("Start task")
    time.sleep(2)
    print("End task")

task()