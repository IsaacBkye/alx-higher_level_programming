#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - Insides a node
 * @head: arg 1
 * @number: arg 2
 * Return: A list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *a, *b;

	a = malloc(sizeof(listint_t));
	if (a == NULL)
		return (NULL);
	a->n = number;
	a->next = NULL;
	if (*head == NULL)
	{
		*head = a;
		a->next = NULL;
		return (a);
	}
	b = *head;
	while (b->next != NULL)
	{
		if (number < b->n)
		{
			a->next = b;
			*head = a;
			return (a);
		}
		if (number <= b->next->n)
		{
			a->next = b->next;
			b->next = a;
			return (a);
		}
		b = b->next;
	}
	a->next = NULL;
	b->next = a;
	return (a);
}
