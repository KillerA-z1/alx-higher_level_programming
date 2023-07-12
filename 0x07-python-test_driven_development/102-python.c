#include "Python.h"

/**
 * print_python_string - Print information about a Python string object
 * @p: PyObject pointer to the string object
 */
void print_python_string(PyObject *p)
{
	PyUnicodeObject *str_obj = (PyUnicodeObject *) p;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(str_obj) ? "compact ascii" :
	"compact unicode object");
	printf("  length: %ld\n", PyUnicode_GET_LENGTH(str_obj));
	printf("  value: %ls\n", PyUnicode_AsWideCharString(str_obj, NULL));
}
