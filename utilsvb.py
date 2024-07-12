def matchpc(r1, g1, b1, r2, g2, b2):
    r = abs(r1 - r2)
    print(r)
    g = abs(g1 - g2)
    print(g)
    b = abs(b1 - b2)
    print(b)
    m = (r + g + b) / 3
    print(m)
    p = (255 - m) / 255
    print(p)
    return p * 100
