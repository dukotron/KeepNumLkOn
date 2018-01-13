import time
import ctypes

winDll = ctypes.WinDLL('User32.dll')
NUMLK = 0X90

while (True):
    if not winDll.GetKeyState(NUMLK):
        #NUMLK down and up, otherwise constantly pressed
        ctypes.windll.user32.keybd_event(NUMLK, 0, 0, 0)
        ctypes.windll.user32.keybd_event(NUMLK, 0, 0x0002, 0)

    time.sleep(5)
