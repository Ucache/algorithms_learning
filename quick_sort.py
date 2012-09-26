def exchange(a,b):
    temp = a
    a = b
    b = temp
    print 'exchange ',a,' and ',b


def PARTITION(A,p,r):
    stand = A[r]
    i = p - 1
    for pos in range(p,r):
        if(A[pos] <= stand):
            i += 1
            temp = A[i]
            A[i] = A[pos]
            A[pos] = temp
#exchange(A[r],A[i+1])
    temp = A[r]
    A[r] = A[i+1]
    A[i+1] = temp
    print 'find mid ',A[i+1]
    print A[p:i+1],A[i+2:r+1]

    return i+1

def QUICK_SORT(A,start,end):
    i = PARTITION(A,start,end)
    if(i>start and i<end):
        QUICK_SORT(A,start,i-1)
        QUICK_SORT(A,i+1,end)


a = [21,5,6,47,9,23,56,87,23,8,35,86]
print a
length = len(a) - 1
QUICK_SORT(a,0,length)
print a
