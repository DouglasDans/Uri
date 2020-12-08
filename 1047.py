list = input().split(" ")
h1, m1, h2, m2 = list
h1 = int(h1)
h2 = int(h2)
m1 = int(m1)
m2 = int(m2)
hora, minutos = 0
if h1 < h2:
    hora = h2 - h1
    if m1 < m2:
        minutos = m2 - m1
    if m1 > m2:
        hora = hora - 1
        minutos = (60 - m1) + m2
    if m1 == m2:
        minutos = 0
if h1 > h2:
    hora = (24 - h1) + h2
    if m1 < m2:
        minutos = m2 - m1
    if m1 > m2:
        hora = hora - 1
        minutos = (60 - m1) + m2
    if m1 == m2:
        minutos = 0
if h1 == h2:
    if m1 < m2:
        minutos = m2 - m1
        hora = 0
    if m1 > m2:
        minutos = (60 - m1) + m2
        hora = 23
    if m1 == m2:
        hora = 24
        minutos = 0

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora,minutos))
