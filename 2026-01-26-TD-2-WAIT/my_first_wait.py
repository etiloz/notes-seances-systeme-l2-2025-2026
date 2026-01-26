import os, sys
fork_result = os.fork()

if fork_result == 0:
    # fils
    mon_pid = os.getpid()
    pid_de_mon_pere_processus_initial = os.getppid()
    print(f"[fils] {mon_pid=} {pid_de_mon_pere_processus_initial=}")
    print("mon pere est", os.getppid() )
    exit_code = input("choisissez le code de sortie: ")
    print("bye")
    sys.exit(int(exit_code))

# suite du père
pid_du_fils = fork_result
mon_pid = os.getpid()
pid_de_mon_pere_shell = os.getppid()
print(f"[père] {mon_pid=} {pid_de_mon_pere_shell=} {pid_du_fils=}")
_pid_du_fils, status = os.waitpid(fork_result, 0)
exit_code = os.WEXITSTATUS(status)
print(f'le fils {fork_result} est terminé avec le code {exit_code}')