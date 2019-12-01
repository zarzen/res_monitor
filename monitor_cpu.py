import psutil
import time
from datetime import datetime
import os


def create_cpu_logfile():
    log_folder = "./logs/cpu"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    dt = datetime.fromtimestamp(time.time())
    timestamp = dt.strftime("%Y%m%d-%H%M%S")
    logfile = timestamp + '-cpu.log'
    return os.path.join(log_folder, logfile)

def main():
    cpu_interval = 1

    logfile = create_cpu_logfile()
    with open(logfile, 'w') as cpu_log:
        
        while True:
            print("{}, {}".format(time.time(), 
                psutil.cpu_percent(interval=cpu_interval, percpu=True)))
            cpu_log.write("{}, {}\n".format(time.time(), 
                psutil.cpu_percent(interval=cpu_interval, percpu=True)))


if __name__ == "__main__":
    main()