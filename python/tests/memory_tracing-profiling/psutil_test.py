'''
Total memory used by Python process:

https://stackoverflow.com/questions/938733/total-memory-used-by-python-process?noredirect=1&lq=1

do pip install psutil if it is not installed yet

handy one-liner if you quickly want to know how many MiB your process takes:
import os, psutil; print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

'''

import os, psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss) # in bytes 




