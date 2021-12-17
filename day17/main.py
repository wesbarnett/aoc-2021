
tx1, tx2, ty1, ty2 = 211, 232, -124, -69
maxy = count = 0
for vxi in range(1, tx2+1):
    for vyi in range(ty1, abs(ty1)):
        x, y, vx, vy = 0, 0, vxi, vyi
        maxy_tmp = 0
        while x <= tx2 and ty1 <= y and (vx > 0 or x > tx1):
            x, y, vx, vy = x + vx, y + vy, vx - 1 if vx > 0 else vx, vy - 1
            maxy_tmp = max(y, maxy_tmp)
            if tx1 <= x <= tx2 and ty1 <= y <= ty2:
                maxy = max(maxy, maxy_tmp)
                count += 1
                break

print(maxy)
print(count)
