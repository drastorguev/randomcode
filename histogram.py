e = raw_input("A:\n")

def histogram(a):
       d = dict()
       for c in a:
           if c not in d:
               d[c] = 1
           else:
               d[c] += 1
       return d


h = histogram(e)

print h
