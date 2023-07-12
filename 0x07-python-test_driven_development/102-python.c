#include "Python.h"

/**
 * print_python_string - Print information about a Python string object
 * @p: PyObject pointer to the string object
 */
void print_python_string(PyObject *p)
{
	PyUnicodeObject *str_obj = (PyUnicodeObject *) p;
	Py_ssize_t length;
	wchar_t *wide_str;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(str_obj);
	wide_str = PyUnicode_AsWideCharString(str_obj, &length);
	if (wide_str == NULL)
	{
		printf("  [ERROR] Failed to get wide char string\n");
		return;
	}

	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(str_obj) ? "compact ascii" : "compact unicode object");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", wide_str);

	PyMem_Free(wide_str);
}
