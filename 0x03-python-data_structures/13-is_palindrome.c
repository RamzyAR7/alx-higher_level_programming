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
	listint_t *head1 = *head;
	listint_t *head2 = *head;

	if (*head == NULL)
		return (1);

	while (head2 && head2->next && head2->next->next)
	{
		head1 = head1->next;
		head2 = head2->next->next;
	}

	head1 = list_rev(&head1);
	head2 = *head;
	while (head1 && head2)
	{
		if (head1->n != head2->n)
			return (0);
		head1 = head1->next;
		head2 = head2->next;
	}

	return (1);
}

/**
 * list_rev - Reverse a linked list
 * @head: The list pointer
 * Return: Pointer to the new head
 */
listint_t *list_rev(listint_t **head)
{
	listint_t *prv = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prv;
		prv = *head;
		*head = next;
	}

	*head = prv;
	return (*head);
}
