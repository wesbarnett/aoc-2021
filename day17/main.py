
tx1, tx2, ty1, ty2 = 211, 232, -124, -69

maxy = 0

result = []
for vxi in range(1, tx2+1):
    for vyi in range(ty1, abs(ty1)):
        x, y = 0, 0
        vx, vy = vxi, vyi
        maxy_tmp = 0
        while x <= tx2 and ty1 <= y and (vx > 0 or x > -tx1):
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1
            if y > maxy_tmp:
                maxy_tmp = y
            if tx1 <= x <= tx2 and ty1 <= y <= ty2:
                if maxy_tmp > maxy:
                    maxy = maxy_tmp
                result.append((vxi, vyi))
                break

print(maxy)
print(len(result))
