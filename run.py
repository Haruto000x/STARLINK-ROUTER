import platform

platform_ = platform.system().lower()

if platform_ == "linux":
    __import__('starlink_linux')
else:
    print('Your Device Not Support!')
