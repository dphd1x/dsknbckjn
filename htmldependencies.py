print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

print "<html><head></head><body><pre>"
a = ['f','d','s','a']
x = -1
scope = vars()
for i in a:
    scope['x']+=1
    print a[x]
print "</pre></body></html>"
