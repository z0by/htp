def findPrime(left,right):
    if left < right:
        for n in xrange(left, right+1):
            for x in xrange(2, n):
                if n % x == 0:
                     #print n, 'equals', x, '*', n/x
                     break
            else:
                print n
    else:
        print "Oops,bad interval"
