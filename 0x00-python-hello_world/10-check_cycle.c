#include "lists.h"
/**
 * check_cycle - function to check if cycle.
 * @list: Pointer to head.
 * Return: 1 if there is a cycle else 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *tort, *c;

	tort = c = list;
	while (tort && c && c->next)
	{
		c = c->next->next;
		tort = tort->next;
		if (tort == c)
		return (1);
	}
	return (0);
}
