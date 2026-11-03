#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>


int main()
{
    int cont = 1;
    pid_t pid = fork();

    if(pid == 0) printf("Hijo: %i\n", ++cont);
    else printf("Padre: %i\n", --cont);
    
    return 0;
}
