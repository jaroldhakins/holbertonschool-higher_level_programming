#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: it's a struct
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *i;

	for (i = list; list != NULL;)
	{
		while (i != NULL)
		{
			i = i->next;
			if (i == list)
			{
				return (1);
			}
		}
		list = list->next;
	}
	return (0);
}
