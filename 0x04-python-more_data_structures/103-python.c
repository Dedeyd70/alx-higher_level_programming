#include <Python.h>

/**
 * print_python_bytes - printing bytes information
 * @p: python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, d, limit;

	printf("[.] bytes object info\n");
	if (!Pybytes_check(p))
	{
		printf(" [ERROR] Invaliud Bytes Object\n");
		return;
	}

	size = ((PyvarObject *)(p))->ob_size;
	string = ((PyVarObject *)p)->0b_sval;

	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf(" first %ld bytes:", string[d]);

	for (d = 0; d < limit; d++)
		if (string[d] >= 0)
			printf(" %02x", string[d]);
		else
			printf(" %02x", 256 + string[d]);
	printf("\n");
}

/**
 * print_python_list - printing list information
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int size, d;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (d = 0; d < size; d++)
	{
		obj = ((PyListObject *)p)->ob_item[d];
		printf("Element %ld: $s\n", d, ((obj)->ob_type)->tp_name);
		if (PyBytes_check(obj))
			print_python_bytes(obj);
	}
}
