#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main()
{
    pid_t pid = fork();

    if (pid < 0)
    {
        printf("No fue posible crear el proceso.\n");
        return 1;
    }
    else if (pid == 0)
        printf("Hijo\n");
    else
        printf("Padre\n");

    return 0;
}
