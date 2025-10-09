import machine
import time
import aioble
import asyncio

print(machine.freq())

led = machine.Pin("LED", machine.Pin.OUT)


async def bt_scan_print():
  async with aioble.scan(duration_ms=5000) as scanner:
    async for result in scanner:
      print(result, result.name(), result.rssi, result.services())

async def bt_scan():
  results = []
  seen_addr = set()
  async with aioble.scan(duration_ms=5000, interval_us=30000, window_us=30000, active=True) as scanner:
    async for result in scanner: 
      if result.name() is not None and result.name() != "Seos" and result.device.addr not in seen_addr:
        results.append(result)
        seen_addr.add(result.device.addr)

  return results

async def main():
  while True:
    results = await bt_scan()
    print("\nScan Complete, Results: ")
    for res in results:
      print(res.name(), res.device.addr_hex())
    time.sleep(10)


asyncio.run(main())
