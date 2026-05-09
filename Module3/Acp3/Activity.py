import os

shutdown = input("Do you wish to shutdown your computer ? (y / n): ")

if shutdown == 'n':
    exit()
else:
    os.system("shutdown /s /t 1")