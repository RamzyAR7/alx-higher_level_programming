#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - Write a function in C that checks if
 * a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 * Return: 1 if the linked list is a palindrome, 0 if it not palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slw, *fst, *prv, *cur, *next, *front, *back;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /* Empty list or single node list is a palindrome */

	/* Use two pointers to find the middle of the list */
	slw = *head;
	fst = *head;

	while (fst != NULL && fst->next != NULL)
	{
		slw = slw->next;
		fst = fst->next->next;
	}

	/* Reverse the second half of the list */
	prv = NULL;
	cur = slw;
	next;

	while (cur != NULL)
	{
		next = cur->next;
		cur->next = prv;
		prv = cur;
		cur = next;
	}

	/* Compare values in the first and reversed second halves */
	front = *head;
	back = prv;

	while (back != NULL)
	{
		if (front->n != back->n)
			return (0); /* Not a palindrome */
		front = front->next;
		back = back->next;
	}
	return (1); /* It's a palindrome */
}
