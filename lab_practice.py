def words(S=''):
    """List of words"""
    L = S.split()
    return L
def sortedwords(S=''):
    """Sorted words"""
    L = words(S)
    L.sort()
    return ' '.join(L)

### S = '23.5 34.6 77.9' -> calculate the sum => test
def str2sum(S):
    """sum..."""
    numbers = S.split()
    total = 0
    for n in numbers:
        total += float(n)
    return total
TESTING = True
if TESTING:
    print(str2sum('1 1 2 3'))

### plot 50 diff. circles with random coord., areas, colors; 2. x and y follows an uniform dist and normal dist.