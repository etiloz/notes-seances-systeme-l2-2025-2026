# voir enonce sur la feuille de TD

import os, sys
try:
    idx1 = sys.argv.index("--then")
    idx2 = sys.argv.index("--else")
    idx3 = sys.argv.index("--fi")
    assert(idx1 < idx2 < idx3 == len(sys.argv)-1)
    args1 = sys.argv[1:idx1]
    args2 = sys.argv[idx1+1:idx2]
    args3 = sys.argv[idx2+1:idx3]
    cmd1 = args1[0]
    cmd2 = args2[0]
    cmd3 = args3[0]
except (ValueError, AssertionError, IndexError):
    print("Usage: python myif.py cmd1 [arg1 ...] --then cmd2 [arg2 ...] --else cmd3 [arg3 ...] --fi", file=sys.stderr)
    sys.exit(1)

if os.fork() == 0:
    os.execvp(cmd1, args1)
else:
    pid,status = os.wait()
    if os.WIFEXITED(status) and os.WEXITSTATUS(status) == 0:
        if os.fork()==0:
            os.execvp(cmd2, args2)
        else:
            os.wait()

    else:
        if os.fork()==0:
            os.execvp(cmd3, args3)
        else:
            os.wait()

