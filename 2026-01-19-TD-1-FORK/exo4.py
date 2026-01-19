import os, sys
print(f"{sys.argv}")
mon_pid = os.getpid()
pid_de_mon_pere = os.getppid()
print(f"{mon_pid=}, {pid_de_mon_pere=}")