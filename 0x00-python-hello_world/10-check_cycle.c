#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *currentNode = list;
	listint_t *nextNode = list;

	if (list == NULL)
	return (0);

	while (1)
	{
		if (nextNode->next && nextNode->next->next)
		{
			currentNode = currentNode->next;
			nextNode = (nextNode->next)->next;

		if (currentNode == nextNode)
			return (1);
		}
		else
		return (0);
	}
}
