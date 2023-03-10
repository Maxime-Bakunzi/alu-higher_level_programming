#include <python3.4/Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: PyObject
 * Return: nothing.
 */
void print_python_list_info(__attribute((unused)) PyObject *p)
{
	int count;

	printf("[*] Size of the Python List = %ld\n",Py_SIZE(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (count = 0; count < Py_SIZE(p); count++)
		printf("Element %d: %s\n", count, Py_TYPE(PyList_GetItem(p, count))->tp_name);
}
