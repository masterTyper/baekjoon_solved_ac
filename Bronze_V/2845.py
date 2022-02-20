L, P = map(int, input().split())
participants = list(map(int, input().split()))
loss = [participant - L*P for participant in participants]
print(" ".join(map(str, loss)))