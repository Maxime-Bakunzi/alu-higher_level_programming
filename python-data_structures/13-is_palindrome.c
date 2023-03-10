#include "lists.h"

/**
 * reverse_listint - Reverses a linked list
 * @head: Pointer to address of a list
 *
 * Return: Pointer to the first node of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp, *current, *rev;

	tmp = current = *head;
	rev = NULL;
	while (current)
	{
		tmp = tmp->next;
		current->next = rev;
		rev = current;
		current = tmp;
	}
	return (rev);
}

/**
 * is_palindrome - Checks if singly linked list is palindrome
 * @head: Pointer to the first node
 *
 * Return: 1 if palindrome
 * otherwise: 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *rev, *current;

	fast = slow = current = *head;
	if (*head)
	{
		while (fast && fast->next)
		{
			slow = slow->next;
			fast = (fast->next)->next;
		}
		rev = slow = reverse_listint(&slow);
		while (rev)
		{
			if (current->n != rev->n)
				return (0);
			current = current->next;
			rev = rev->next;
		}
		reverse_listint(&slow);
	}
	return (1);
}
