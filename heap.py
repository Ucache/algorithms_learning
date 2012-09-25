## MAX_HEAPIFY 用来使以i为跟节点的树建堆
## BUILD_MAX_HEAP is for building the heap
## HEAP_SORT is for sorting a given list A


import sys


### get right and left child of pos i
def Right(i):   
    return 2*i+1

def Left(i):
    return 2*i

def MAX_HEAPIFY(A,i):
    left = Left(i)
    right = Right(i)
    length = A[0]
    #print 'i is ',i,'left is ',left,'right is ',right
    if(left <= length and A[i] < A[left]):
        largest = left
    else:
        largest = i

    if(right <= length and A[largest] < A[right]):
        largest = right 
    #print 'largest pos is ',largest
    if(largest != i):
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
    #    print 'exchange ',A[i],' and ',A[largest]
        MAX_HEAPIFY(A,largest)

def BUILD_MAX_HEAP(A):
    length = A[0]
    #print 'length is ',length
    start = length/2
    #print 'start is ',start
    while(start):
        MAX_HEAPIFY(A,start)
        start-=1

def HEAP_SORT(A):
    #print 'befor sort a is ',A
    BUILD_MAX_HEAP(A)
    #print 'after building a is ',A
    temp = A[1]
    A[1] = A[A[0]]
    A[A[0]] = temp
    A[0]-=1
    #print 'the largest ',temp,'length is ',A[0],'\n'
    if(A[0]>0):
        HEAP_SORT(A)


#def PRINT_TREE(A):
#    length = A[0]
#    step=1
#    i=1
#    pos = 1
#    while(i<=step and pos <= length):
#        if(i!=step):
#            print A[pos],
#            i += 1
#        else:
#            print A[pos]
#            step *= 2
#            i = 1
#        pos+=1


#a = [5,17,27,10,16,13]
a = [10,51,29,23,64,85,66,77,28,49,10]
print "original:",a
#PRINT_TREE(a)
#BUILD_MAX_HEAP(a)
#print "\nafter build",a
#PRINT_TREE(a)

HEAP_SORT(a)
print "after sort",a
