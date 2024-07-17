a,b,c,d,e = map(int,input().split())
result = 0

for square in [a,b,c,d,e]:
    result += square**2

print(result%10)