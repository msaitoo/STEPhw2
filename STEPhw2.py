import numpy, sys, time, matplotlib.pyplot as pyplot

if (len(sys.argv) != 2):
    print "usage: python %s N" % sys.argv[0]
    sys.exit()

def initiate(z):
    '''
    Initiates square matrices to be multiplied.
            z = dimension
    '''
    a = numpy.zeros((z,z))     # Matrix A
    b = numpy.zeros((z,z))     # Matrix B
    c = numpy.zeros((z,z))     # Matrix C (result of multiplication)
    
    for i in xrange(z):        #Initialise the matrices to some values.
        for j in xrange(z):
            a[i,j] = i * z + j
            b[i,j] = j * z + i
            c[i,j] = 0
    return (a,b,c)

#Initiate matrices with given dimension.
n       = int(sys.argv[1])

def matrix(q):
    '''
    Multiplies two square matrices.
            q = dimension
    Gives:
            c = Resultant matrix
            t = time taken for calculation
    '''
    a, b, c = initiate(q)[0], initiate(q)[1], initiate(q)[2]
    begin = time.time()                      #Initial time
    for i in range(q):
        for j in range(q):
            elements = numpy.zeros(q)
            for k in range(q):               #Sigma summation
                elements[k] = a[i,k]*b[k,j]
            c[i,j] = sum(elements)           #Elements in c
    end = time.time()                        #End time
    t = end - begin                          #Get time difference in time
    return (c,t)

#Result of multiplication
c = matrix(n)[0]
print "time: %.6f sec" % (matrix(n)[1])

#Sum of elements in c
total = 0
for i in xrange(n):
    for j in xrange(n):
        #print c[i,j]
        total += c[i,j]
print "sum: %.6f" % total

###########################Graphing###########################
def graph(x):
    pyplot.figure()
    pyplot.title("time vs N")
    pyplot.ylabel('time')
    pyplot.xlabel('N')
    X, Y = numpy.zeros(x), numpy.zeros(x)
    
    for y in range(x):
        t = matrix(y)[1]
        X[y], Y[y] = y, t
    
    pyplot.plot(X,Y)
    pyplot.tight_layout()
    return pyplot.show()