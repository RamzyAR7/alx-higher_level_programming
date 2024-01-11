#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	unsigned long size, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);

	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; ++i)
	{
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Print information about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; ++i)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %ld: ", i);
		if (PyBytes_Check(element))
			print_python_bytes(element);

		else if (PyLong_Check(element))
			printf("int\n");

		else if (PyFloat_Check(element))
			printf("float\n");

		else if (PyTuple_Check(element))
			printf("tuple\n");

		else if (PyList_Check(element))
			printf("list\n");

		else if (PyUnicode_Check(element))
			printf("str\n");
		else
			printf("[ERROR] Unsupported Element Type\n");
	}
}

/**
 * main - Example usage
 * Return: Always 0
 */
int main(void)
{
	Py_Initialize();

	PyObject *s = PyBytes_FromString("Hello");

	print_python_bytes(s);

	PyObject *b = PyBytes_FromStringAndSize("\xff
										\xf8\x00\x00\x00\x00\x00\x00", 8);
	print_python_bytes(b);

	PyObject *l = PyList_New(2);

	PyList_SetItem(l, 0, s);
	PyList_SetItem(l, 1, PyBytes_FromString("World"));
	print_python_list(l);

	Py_DECREF(l);
	Py_DECREF(s);
	Py_DECREF(b);

	Py_Finalize();
	return (0);
}
