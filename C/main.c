#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    printf("STARTING\n");
    pid_t pid = fork(); // create a child process
    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // child process
        printf("Child process (PID=%d) is running\n", getpid());
        for (int i = 0; i < 3; i++){
            printf("loop %d\n",i);
            sleep(1);
        }
        printf("Child process is done\n");
        exit(EXIT_SUCCESS);
    } else {
        // parent process
        printf("Parent process (PID=%d) is waiting for child (PID=%d) to finish...\n", getpid(), pid);
        int status;
        pid_t terminated_pid = wait(&status);
        if (terminated_pid == -1) {
            perror("wait");
            exit(EXIT_FAILURE);
        }
        printf("Child process (PID=%d) finished with exit status %d\n", terminated_pid, status);
        exit(EXIT_SUCCESS);
    }
}

