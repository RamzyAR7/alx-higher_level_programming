#include <stdio.h>
#include <Python.h>


/**
 * write_python - Writes Python object information.
 *
 * @python: Python object to write information about.
 */
void write_python(PyObject *python)
{
	char *str;
	long int s, i, lmt;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(python))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = ((PyVarObject *)(python))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		lmt = 10;
	else
		lmt = s + 1;

	printf("  first %ld bytes:", lmt);

	for (i = 0; i < lmt; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}


/**
 * write_python_l - Writes information about a Python object.
 *
 * @python: Python object to write information about.
 */
void write_python_l(PyObject *python)
{
	long int s, i;
	PyListObject *list;
	PyObject *obj;

	s = ((PyVarObject *)(python))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < s; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			write_python(obj);
	}
}
