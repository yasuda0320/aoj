w, h, x, y, r = map(int, input().split())
print('Yes' if x - r >= 0 and y - r >= 0 and x + r <= w and y + r <= h else 'No')
