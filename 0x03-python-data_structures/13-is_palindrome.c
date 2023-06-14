#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reChk - Check values of head and tail in a linked list recursively
 * @h: arg
 * @t: arg1
 * Return: 1 if palidrome or 0 if otherwise
 */
int reChk(listint_t **h, listint_t *t)
{
	if (t == NULL)
		return (1);

	if (reChk(h, t->next) && (*h)->n == t->n)
	{
		*h = (*h)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - Check list if palindrome
 * @head: arg
 * Return: 1 if true or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	return (reChk(head, *head));
}
