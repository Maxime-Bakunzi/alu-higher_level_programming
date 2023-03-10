#include "lists.h"

/**
 * is_palindome - Checks if a singly linked list is a palindrome
 * @head: pointer to pointer head of the list
 * Return: 0 if is not a palindrome
 * otherwise: 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int num[9999], count = 0, i = 0;

	if ((!head) || (!*head))
		return (1);

	node = *head;
	if (!node->next)
		return (1);

	while (node)
	{
		num[count] = node->n;
		node = node->next;
		count++;
	}
	count--;

	while (count >= 0 && i <= count)
	{
		if (num[count] != num[i])
			return (1);
		count--;
		i--;
	}
	return (0);
}
