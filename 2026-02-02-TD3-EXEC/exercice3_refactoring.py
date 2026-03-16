import os

def run(cmd_line):
    args = cmd_line.strip().split()
    if len(args) == 0 :
        return
    if os.fork() == 0:
        try:
            os.execvp(args[0], args)
        except FileNotFoundError:
            print("command not found", file=sys.stderr)
            sys.exit(1)
        except PermissionError:
            print("command not permitted", file=sys.stderr)
            sys.exit(1)
    os.wait()

run("who")
run("pwd")
run("ls -l")