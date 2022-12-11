colors = {'black': 0, 'brown': 1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
res = 0
res += 10 * colors[input()]
res += colors[input()]
res *= 10 ** colors[input()]
print(res)