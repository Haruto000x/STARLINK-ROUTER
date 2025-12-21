import platform

platform_ = platform.system().lower()

if platform_ == "linux":
    __import__('starlink_linux')
elif platform == "windows":
    __import__('starlink_window')
else:
    print('Your Device Not Support!')
