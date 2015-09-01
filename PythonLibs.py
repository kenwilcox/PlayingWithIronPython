import clr
import xmlutil

clr.AddReference('System.Xml')
from System.Xml import *

d = XmlDocument()
d.Load('C:\Program Files (x86)\IronPython 2.7\Tutorial\load.xml')
n = d.SelectNodes('//Puzzle/SavedGames/Game/@caption')

for e in n:
    print e.Value

for e in xmlutil.Walk(d):
    print e.Name, e.Value
