def triangles2():

    p = [1]

    while True:

        yield p

        p = [1] + [p[n]+p[n+1] for n in range(len(p)-1)] + [1]

n = 0

results = []

for t in triangles2():

    print(t)

    results.append(t)

    n = n + 1

    if n == 10:

        break
