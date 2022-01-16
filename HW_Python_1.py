a = 'Igor'
b = 31
c = 3.14
d = b'Ne4kov'
e = [8, 9, 0]
q = (7, 6, 5)
w = set('vitebsk')
r = frozenset('frozen')
t = dict(short='dict', long='dictionary')


print('a = ', type(a))
print('b = ', type(b))
print('c = ', type(c))
print('d = ', type(d))
print('e = ', type(e))
print('q = ', type(q))
print('w = ', type(w))
print('r = ', type(r))
print('t = ', type(t))

aa = '"Lord of'
bb = ' the Rings"'
like = aa + bb
print('I like', like)

print('I am', a, b)

print('Hello', a+str(b))