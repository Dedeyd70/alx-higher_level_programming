#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	while (ptr2 && (ptr2 = ptr2 ->next))
	{
		if (ptr2 == ptr1)
			return (1);
		ptr2 = ptr2->next;
		ptr1 = ptr1->next;
	}
	return (0);
}
