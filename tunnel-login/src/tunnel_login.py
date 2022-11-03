#!/bin/python3
import sys, os, time, argparse

os_dir = "/tmp/tunnel_login"

def error(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)
    
error(os.system("who"))
try:
    if not os.path.exists(os_dir):
        os.makedirs(os_dir)
except Exception as e:
    error(e.with_traceback())   

def execCmd(cmd):
    # r = os.system(cmd)
    r = os.popen(cmd)
    text = r.read()
    r.close()
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

        cmd = f"lsof -i tcp:{args.port} | grep tunnel | grep localhost:{args.port}"
        res = execCmd(cmd)
        if res != "":
            handleConfig(args.name, args.port)
    
    def handleConfig(hostname: str, port: int):
        if not os.path.exists('/etc/nginx/hosts'):
            os.makedirs('/etc/nginx/hosts')
        with open(f'/etc/nginx/hosts/{hostname}.loc', 'w') as f:
            f.write(f"""location /{hostname}/ \u007b
                include proxy_params;
                proxy_pass http://localhost:{port}/;
            \u007d""")
        os.system('nginx -s reload')

    fprint(repr(os.environ))
    fprint("argv=" + repr(sys.argv))
    
    if sys.argv[1][0] == '-': # disconnect
        fprint(f"disconnected from {os.environ['SSH_CLIENT']}")
        # TODO
    else: # connect
        if len(sys.argv) > 2:
            parser = argparse.ArgumentParser(description="")
            parser.add_argument('-c', type=str)
            commond = parser.parse_args(sys.argv[2:])
            if commond.c is not None:
                handleCommand(commond.c.split(' '))

    # os.system("lsof -i tcp")
    # os.system("/bin/sh")

    # print(os.system("nginx -s reload"))

sys.exit(0)
