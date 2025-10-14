import machine
import time

from radiacode import RadiaCode
from radiacode.transports.bluetooth import DeviceNotFound as DeviceNotFoundBT

BLUETOOTH_MAC = "52:43:06:60:17:dd"

print(f'Connecting to Radiacode via Bluetooth (MAC address: {BLUETOOTH_MAC})')

while True: 
  try: 
    rc = RadiaCode(bluetooth_mac=BLUETOOTH_MAC)
  except DeviceNotFoundBT as e:
    print(e)
    continue 

  serial = rc.serial_number()
  print(f'### Serial number: {serial}')
  print('--------')

  fw_version = rc.fw_version()
  print(f'### Firmware: {fw_version}')
  print('--------')

  spectrum = rc.spectrum()
  print(f'### Spectrum: {spectrum}')
  print('--------')

  print('### DataBuf:')
  while True:
      for v in rc.data_buf():
          print(v.dt.isoformat(), v)
      time.sleep(2)