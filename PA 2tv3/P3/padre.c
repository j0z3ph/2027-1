#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main()
{
    pid_t pid = fork();
    int status;

    if (pid == 0)
    {
        // Soy el hijo
        //execlp("ls", "ls", "-al", NULL);
        execl("./a.out", "a.out", NULL);
    }
    else
    {
        // Soy el padre
        waitpid(pid, &status, 0);
        printf("%d\n", status);
        if (WIFEXITED(status))
        {
            printf("El programa termino con estatus: %d\n", WEXITSTATUS(status));
        }
        else
        {
            printf("El programa termino abruptamente\n");
        }
    }

    return 0;
}
