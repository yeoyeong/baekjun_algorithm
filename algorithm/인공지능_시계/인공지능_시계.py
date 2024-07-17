
t, m, s = map(int, input().split())
n_s = int(input())

# 전체 시간을 초 단위로 계산
total_seconds = (t * 3600 + m * 60 + s) + n_s

hours = (total_seconds // 3600) % 24
min = (total_seconds % 3600) // 60
seconds = ((total_seconds % 3600) % 60)

# if time>23:
#     time -= 24

print(hours, min, seconds)

    






