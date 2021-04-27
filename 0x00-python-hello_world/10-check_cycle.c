#include "lists.h"

/**
 * check_cycle - function to determine if there is a cycle in a linked list
 * @list: linked list to check
 * Return: 0 if no cycle and 1 if cycle exists
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list, *tail = list;

	while (head && tail && tail->next)
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
			return (1);
	}
	return (0);
}
