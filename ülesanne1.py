def r(h, p):
    if not h:
        return []
    
    h.sort(reverse=True)
    
    a = 0
    b = []

    while h:
        järgmine_raamat = h[0]
        if (a + järgmine_raamat) <= riiuli_pikkus:
            b.append(järgmine_raamat)
            a += järgmine_raamat
            h.pop(0)
        else:
            return b
    
    return b
