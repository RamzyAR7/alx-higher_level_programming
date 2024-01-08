#include <Python.h>
/**
 * print_python_list_info - Prints information about a Python list.
 * @p: The Python list object.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, allocated, i;
	PyObject *item;

	list = (PyListObject *)p;
	size = PyList_Size(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
