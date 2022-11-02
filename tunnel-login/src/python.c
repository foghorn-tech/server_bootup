#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include "./pyscript.h"

int main(int argc, char *argv[], char *envp[]){
	unsigned i = 0;
	for (i = 0;i < tunnel_login_py_len;++i) putchar(tunnel_login_py[i]);
	puts("");
	int err = setuid(0);
	if (err) {
		printf("err=%d\n", err);
		return err;
	}

	char **it = argv;
	for( ; *it != NULL; ++it)
		printf("%s ", *it);
	puts("");
	it = envp;
	for( ; *it != NULL; ++it)
		printf("%s ", *it);
	puts("");

	argv[0] = "python3";

	char **new_argv = (char**) malloc((argc + 2) * sizeof(char*));

	memcpy(new_argv, argv, argc);
	new_argv[0] = "/usr/bin/python3";
	new_argv[argc] = "-c";
	new_argv[argc+1] = (char*) tunnel_login_py;

	execve("/usr/bin/python3", new_argv, envp);

	return errno;
}

