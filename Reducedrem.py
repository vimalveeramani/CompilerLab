def rem(gram):
    c = 1
    conv = {}
    gramA = {}
    revconv = {}

    for j in gram:
        conv[j] = f"A{c}"
        gramA[f"A{c}"] = []
        c += 1

    for i in gram:
        for j in gram[i]:
            temp = [conv.get(k, k) for k in j]
            gramA[conv[i]].append(temp)

    for i in range(c-1, 0, -1):
        ai = f"A{i}"
        for j in range(i):
            aj = gramA[ai][0][0]
            if ai != aj and aj in gramA and checkForIndirect(gramA, ai, aj):
                gramA = rep(gramA, ai)

    for i in range(1, c):
        ai = f"A{i}"
        for j in gramA[ai]:
            if ai == j[0]:
                gramA = removeDirectLR(gramA, ai)
                break

    for i in gramA:
        a = str(i)
        for j in conv:
            a = a.replace(conv[j], j)
        revconv[i] = a

    op = {revconv[i]: [[revconv.get(k, k) for k in j] for j in gramA[i]] for i in gramA}

    return op
