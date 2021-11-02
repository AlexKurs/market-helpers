# Klassik Methode
# Pivot Point

o = input()
h = input()
l = input()
c = input()

kp = (h+l+c)/3

# Widerstand

kr1 = ((2*kp)-l)
kr2 = kp+h-l
kr3 = h+2*(kp-l)

# Unterstützung

ks1 = (2*kp)-h
ks2 = kp-h+l
ks3 = l-2*(h-kp)

# Woody Methode
# Pivot Point

wp = (h+l+2*c)/4

# Widerstand

wr1 = 2*wp-l
wr2 = wp+h-l

# Unterstützung

ws1 = 2*wp-h
ws2 = wp-h+l

# Camarilla Methode
# Unterstützung

cr1 = (h-l)*1.1/12+c
cr2 = (h-l)*1.1/6+c
cr3 = (h-l)*1.1/4+c
cr4 = (h-l)*1.1/2+c

# Widerstand

cs1 = c-(h-l)*1.1/12
cs2 = c-(h-l)*1.1/6
cs3 = c-(h-l)*1.1/4
cs4 = c-(h-l)*1.1/2

# DeMark Methode

if c < o:
    x = h+2*l+c
elif c > o:
    x = 2*h+l+c
elif c == o:
    x = h+l+2*c

nh = x/2-l
nl = x/2-h

# Durchschnittliche Werte

p = (kp+wp)/2

r1 = (kr1+wr1+cr1)/3
r2 = (kr2+wr2+cr2)/3
r3 = (kr3+cr3)/2
r4 = cr4

s1 = (ks1+ws1+cs1)/3
s2 = (ks2+ws2+cs2)/3
s3 = (ks3+cs3)/2
s4  = cs4

print('Pivot:', '%.2f' % p)
print('------------------')

print('R1:', '%.2f' % r1)
print('R2:', '%.2f' % r2)
print('R3:', '%.2f' % r3)
print('R4:', '%.2f' % r3)
print('------------------')
print('S1:', '%.2f' % s1)
print('S2:', '%.2f' % s2)
print('S3:', '%.2f' % s3)
print('S4:', '%.2f' % s3)
print('------------------')
print('DeMark Methode - Max & Min')
print('------------------')
print('New High:', '%.2f' % nh)
print('New Low:', '%.2f' % nl)