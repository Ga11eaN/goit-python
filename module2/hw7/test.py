from time import sleep
import sys
import asyncio
from aioconsole import ainput

async def print_text(text):
    while True:
        inp = await ainput()
        print(text, inp)

async def async_read_stdin():
    while True:
        inp = await ainput()
        print('got ' + inp)


async def main():
    await asyncio.gather(print_text('aaa'), async_read_stdin())
        
    
asyncio.run(main())