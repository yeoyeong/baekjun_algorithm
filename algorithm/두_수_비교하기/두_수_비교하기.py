A,B = map(int,input().split())

def compare_values(a, b):
    if a > b:
        return ">"
    if a < b:
        return "<"
    if a == b:
        return "=="
    

result = compare_values(A,B)

print(result)