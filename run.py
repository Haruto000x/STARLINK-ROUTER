#Only work on arm64 bit device and in termux app
#Only for Ruijie Network Router
import os

os.system('git pull --quiet')

if __name__ == '__main__':
    __import__('starlink')
