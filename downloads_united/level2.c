#include <sys/mman.h>
#include <seccomp.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>

int main() {
    printf("%d", __NR_getcpu);

    return EXIT_SUCCESS;
}
