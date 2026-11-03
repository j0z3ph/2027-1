#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main()
{
    pid_t hijito;

    for (int i = 0; i < 3; i++)
    {
        hijito = fork();

        if (hijito == 0)
        {
            // Yo soy un hijo
            printf("[%i] [%i] Soy tu hijo\n", getpid(), hijito);
            break; // Cuidado con la llamada recursiva de forks()
        }
        else
            printf("[%i] Soy el papa\n", getpid());
    }

    return 0;
}
