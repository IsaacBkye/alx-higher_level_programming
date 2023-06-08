#include "lists.h"
/**
 * check_cycle - Singly list cycle checker
 * @list: arg
 * Return: 0 if not else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	a = list;
	b = list;
	while (a != NULL && b != NULL && b->next != NULL)
	{
		b = b->next->next;
		a = a->next;
		if (a == b)
			return (1);
	}
	return (0);
}
