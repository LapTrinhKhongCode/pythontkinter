from typing import Dict, Any
import re
import subprocess

class USBDeviceAPI: 
    def get_usb_devices(self):
        #regex phân tích output của lệnh lsusb
        device_regex = re.compile(r"Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
        df = subprocess.check_output("lsusb").decode('utf-8')
        devices = []
        for i in df.split('\n'):
            if i:
                info = device_regex.match(i)
                if info:
                    dinfo = info.groupdict()
                    dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                    devices.append(dinfo)
        return devices