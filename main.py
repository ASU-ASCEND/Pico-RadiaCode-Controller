import machine
import time
import aioble
import asyncio

print(machine.freq())

led = machine.Pin("LED", machine.Pin.OUT)


async def bt_scan():
  async with aioble.scan(duration_ms=5000) as scanner:
    async for result in scanner:
      print(result, result.name(), result.rssi, result.services())


async def main():
  while True:
    await bt_scan()
    time.sleep(10)


asyncio.run(main())
