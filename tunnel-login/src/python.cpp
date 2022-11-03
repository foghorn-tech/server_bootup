#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <pyscript.h>
#include <string>

int printArgs(const char * const name, const char * const args[], FILE *f){
	fprintf(f, "%s = [ ", name);
	const char * const * it = args;
	for( ; *it != NULL; ++it)
		fprintf(f, "\"%s\" ", *it);
	fprintf(f, "]\n");
	return 0;
}

int main(int argc, char *argv[], char *envp[]){
	unsigned i = 0;
	// for (i = 0;i < pycode_len;++i) putchar(pycode[i]);
	// puts("");
	int err = setuid(0);
	fprintf(stderr, "err=%d\n", err);
	if (err) {
		return err;
	}

	// fprintf(stderr, "argc = %d\n", argc);
	// printArgs("args", (const char**) argv, stderr);
	// printArgs("envp", (const char**) envp, stderr);

	size_t len = 0;

	const char ** new_argv = (const char**) malloc((argc + 4) * sizeof(char *));

	new_argv[0] = "python3";
	new_argv[1] = "-c";
	new_argv[2] = (char*) pycode;
	memcpy((void **) new_argv + 3, argv, (argc) * sizeof(char *));
	new_argv[argc+3] = NULL;

	// args:
	// fprintf(stderr, "argc = %d\n", argc);
	// printArgs("args", new_argv, stderr);
	// printArgs("envp", (const char**) envp, stderr);

	err = execve("/usr/bin/python3", (char *const*) new_argv, envp);
	if (err) {
		fprintf(stderr, "execve error: err: %d", err);
	}

	free(new_argv);

	return errno;
}

