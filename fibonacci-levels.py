# Fibonacci Levels

h = float(input('High: '))
l = float(input('Low: '))

d = h-l

# Gerade Rechnung

gf0 = round(d * 0 + l, 2)
gf23 = round(d * 0.236 + l, 2)
gf38 = round(d * 0.382 + l, 2)
gf50 = round(d * 0.50 + l, 2)
gf61 = round(d * 0.618 + l, 2)
gf100 = round(d * 1 + l, 2)
gf138 = round(d * 1.382 + l, 2)
gf161 = round(d * 1.618 + l, 2)
gf200 = round(d * 2 + l, 2)
gf261 = round(d * 2.618 + l, 2)

# Zurück Rechnung

zf0 = round(h - (d * 0), 2)
zf23 = round(h - (d * 0.236), 2)
zf38 = round(h - (d * 0.382), 2)
zf50 = round(h - (d * 0.50), 2)
zf61 = round(h - (d * 0.618), 2)
zf100 = round(h - (d * 1), 2)
zf138 = round(h - (d * 1.382), 2)
zf161 = round(h - (d * 1.618), 2)
zf200 = round(h - (d * 2), 2)
zf261 = round(h - (d * 2.618), 2)



print('%.2f' % d)
print('------------')
print('%.2f' % gf0)
print('%.2f' % gf23)
print('%.2f' % gf38)
print('%.2f' % gf50)
print('%.2f' % gf61)
print('%.2f' % gf100)
print('%.2f' % gf161)
print('%.2f' % gf200)
print('%.2f' % gf261)
print('------------')
print('%.2f' % zf0)
print('%.2f' % zf23)
print('%.2f' % zf38)
print('%.2f' % zf50)
print('%.2f' % zf61)
print('%.2f' % zf61)
print('%.2f' % zf100)
print('%.2f' % zf138)
print('%.2f' % zf161)
print('%.2f' % zf200)
print('%.2f' % zf261)
