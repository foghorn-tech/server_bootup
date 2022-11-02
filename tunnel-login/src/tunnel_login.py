#!/bin/python3
import sys, os, time, argparse

os_dir = "/tmp/tunnel_login"
if not os.path.exists(os_dir):
    os.makedirs(os_dir)


def execCmd(cmd):
    r = os.system(cmd)
    #text = r.read()
    #r.close()
    return ""
    return text

with open(f"{os_dir}/tunnel-out.txt", "a+") as f:
    def fprint(*args, **kwargs):
        print("[{}]:".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())), *args, **kwargs, file=f)

    def handleCommand(commands):
        parser = argparse.ArgumentParser(description="")
        parser.add_argument('command', type=str)
        parser.add_argument('-n', '--name', type=str)
        parser.add_argument('-p', '--port', type=int)

        args = parser.parse_args(commands)

        fprint("args=", args)

        cmd = f"lsof -i tcp:{args.port}"
        cmd = "who"
        cmd = "netstat -tln"
        cmd = f"lsof -i tcp"
        fprint("cmd=", cmd)
        res = execCmd(cmd)
        fprint("res=", res.split('\n'))
        
    # handleCommand

    fprint(repr(os.environ))
    fprint("argv=" + repr(sys.argv))

    # os.system("lsof -i tcp")
    # os.system("/bin/sh")

    if len(sys.argv) > 2 and sys.argv[1] == '-c':
        for c in sys.argv[2:]:
            handleCommand(c.split(' '))

    # print(os.system("nginx -s reload"))

# sys.exit(0)
