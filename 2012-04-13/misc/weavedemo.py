import scipy.weave as weave

def ramp(result, size, start, end):
    step = (end-start)/(size-1)
    for i in xrange(size):
        result[i] = start + step*i

def ramp_numeric1(result,start,end):
    code = """
           const int size = Nresult[0];
           const double step = (end-start)/(size-1);
           double val = start;
           for (int i = 0; i < size; i++)
               *result++ = start + step*i;
           """
    weave.inline(code,['result','start','end'],compiler='gcc')


