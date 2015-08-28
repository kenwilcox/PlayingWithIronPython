from System.Collections import *

print('Hello world')

h = Hashtable()
h['a'] = 'IronPython'
h['b'] = 'Tutorial'

for e in h:
    print e.Key, ':', e.Value
