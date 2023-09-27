#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>
#include <errno.h>

/************************
 * 参数cmd: 存放要被执行的命令
 * 参数commandNum: 命令的个数
 * 案例: cmd = {"ls", "touch testFile"}   commandNum = 2
*************************/
void RShell(char *cmd[], int commandNum)
{
	/********** BEGIN **********/
  char input[100];

    /*while (1) {
        printf(">> ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        if (strcmp(input, "exit") == 0) {
            break;
        }
        int i;
        for (i = 0; i < commandNum; i++) {
            if (strcasecmp(input, cmd[i]) == 0) {
                system(cmd[i]);
                break;
            }
        
      
    }
    }*/
    cmd = ["ls","sb"];
    printf(cmd[1]);
	
	/********** END **********/
}

