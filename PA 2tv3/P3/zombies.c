#include <sys/types.h>
#include <unistd.h>

int main()
{
    pid_t pid = fork();

    if(pid != 0) {
        // Soy el papa
        sleep(30);
    }
    
    return 0;
}
