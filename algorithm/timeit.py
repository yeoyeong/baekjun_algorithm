import timeit

## 속도 측정


# 첫 번째 방법: 함수 사용

setup_code = """
A, B = 1, 2

def compare_values(a, b):
    if a > b:
        return ">"
    elif a < b:
        return "<"
    else:
        return "=="
"""

test_code_function = """
result = compare_values(A, B)
"""

time_function = timeit.timeit(setup=setup_code, stmt=test_code_function, number=1000000)
print(f"Function call time: {time_function}")

# 두 번째 방법: 직접 조건문 사용
test_code_direct = """
A, B = 1, 2

if A > B:
    result = '>'
elif A < B:
    result = '<'
else:
    result = '=='
"""

time_direct = timeit.timeit(stmt=test_code_direct, number=1000000)
print(f"Direct condition time: {time_direct}")
