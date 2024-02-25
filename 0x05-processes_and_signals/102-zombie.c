#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int create_zombie(void);
int infinite_while(void);

/**
 * infinite_while - function to continuously create zombie processes
 *
 * Return: Always 0 (success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * create_zombie - function that create zombie processes
 *
 * Return: Always 0 (success)
 */

int create_zombie(void)
{
	pid_t child_pid;
	int count = 0;

	while (count < 5)
	{
		child_pid = fork();

		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else if (child_pid == 0)
		{
			exit(0);
		}
		else
		{
			fprintf(stderr, "Fork failed\n");
			return (1);
		}
		count++;
	}
	return (0);
}

/**
 * main - the entry to a program that creates 5 zombie processes
 *
 * Return: Always 0 (success)
 */
int main(void)
{
	create_zombie();
	infinite_while();
	return (0);
}
