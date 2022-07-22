score_list = []
for _ in range(6):
    score = int(input())
    score_list.append(score)

JOI_one = sorted(score_list[:4], reverse=True)
JOI_two = sorted(score_list[4:], reverse=True)

print(sum(JOI_one[:3]) + JOI_two[0])