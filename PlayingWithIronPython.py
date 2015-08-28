from System.Collections import *

print('Hello world')

h = Hashtable()
h['a'] = 'IronPython'
h['b'] = 'Tutorial'

for e in h:
    print e.Key, ':', e.Value

l = ArrayList([1,2,3])
for i in l:
    print i

s = Stack((1,2,3))
while s.Count:
    print s.Pop()