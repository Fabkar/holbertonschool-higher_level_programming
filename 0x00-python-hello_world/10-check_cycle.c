#include "lists.h"
/**
 * check_cycle - function to check if cycle.
 * @list: Pointer to head.
 * Return: 1 if there is a cycle else 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *current_list, *n_list;

	current_list = list;
	n_list = current_list->next;
	while (current_list != NULL)
	{
		while (n_list != NULL)
		{
			if (current_list == n_list->next)
				return (1);
			n_list = n_list->next;
		}
		if (n_list == NULL)
			return (0);
		current_list = current_list->next;
	}
	return (0);
}
