#include <Python.h>

#include "libprime.h"

static PyObject* wrap_primes(PyObject* self, PyObject* args)
{
    unsigned int l, i;
    if (!PyArg_ParseTuple(args, "I", &l))
        return NULL;
    int *data = create_primes(l);
    PyObject *lst = PyList_New(l);
    for (i = 0; i < l; i++)
        PyList_SET_ITEM(lst, i, PyInt_FromLong(data[i]));
    free(data);
    return lst;
}
 
static PyMethodDef ModuleMethods[] =
{
     {"primes", wrap_primes, METH_VARARGS, "Get a string of variable length"},
     {NULL, NULL, 0, NULL},
};
 
PyMODINIT_FUNC
 
initpyprime(void)
{
     (void) Py_InitModule("pyprime", ModuleMethods);
}
