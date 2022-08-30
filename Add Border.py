def solution(picture):
    L = len(picture)
    l = 0
    for i in picture:
        if (l < len(i)):
            l = len(i)
    L += 2
    l += 2
    tab = [i for i in range(L)]
    tab[0] = '*' * l
    tab[L - 1] = '*' * l
    print(tab)
    for i in range(L - 2):
        a=int((l-len(picture[i]))/2)
        tab[i + 1] = '*'*a + picture[i] + '*'*a
    return tab


print(solution(["abc", "ded"]))
