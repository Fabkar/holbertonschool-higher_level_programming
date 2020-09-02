#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - function to insert a number to a linked list .
 * @head: Double Pointer to head.
 * @number: number to insert.
 * Return: new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *back, *current, *new;

	back = *head;
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
        new->n = number;
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current != NULL && current->n < number)
	{
		back = current;
		current = current->next;
	}
	new->next = current;
	back->next = new;
	return (new);
}
