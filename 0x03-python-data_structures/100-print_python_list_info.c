#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - print python lists
 * @p: pyobject.
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0;
	PyObject *item = NULL;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("Allocated = %ld\n", ((PyListObject *)(p))->allocated);
	for (; i < (Py_ssize_t)PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %i: %s\n", (int)i, item->ob_type->tp_name);
	}
}
