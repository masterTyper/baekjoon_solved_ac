D, H, W = map(int, input().split())

height = int((H * D) / (((H ** 2) + (W ** 2)) ** 0.5))
width = int((W * D) / (((H ** 2) + (W ** 2)) ** 0.5))
print(height, width)