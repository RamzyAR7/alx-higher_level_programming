#include "lists.h"
/**
 * insert_node - Inserts a node into a sorted linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The value to be inserted.
 *
 * Return: The address of the newly inserted node, or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	current = *head;
	prev = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = current;
	}

	return (new);
}
