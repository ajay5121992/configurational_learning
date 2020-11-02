import psutil
# To get non "virtual" hyperthreaded cpus, need to pass logical = False
psutil.cpu_count(logical = False)
