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
	listint_t *head_n;
	int len = 0, idx = 0;
	int i, x;
	int *arr;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	head_n = *head;

	while (head_n != NULL)
	{
		head_n = head_n->next;
		len++;
	}
	arr = malloc(sizeof(int) * len);

	head_n = *head;
	while (head_n != NULL)
	{
		arr[idx] = head_n->n;
		head_n = head_n->next;
		idx++;
	}
	for (i = 0, x = len - 1; i < x; i++, x--)
	{
		if (arr[i] != arr[x])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
