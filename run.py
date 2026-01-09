import platform

platform_ = platform.system().lower()

if platform_ == "linux":
    __import__('starlink')
else:
    print('Your Device Not Support!')
