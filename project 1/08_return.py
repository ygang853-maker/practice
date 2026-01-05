# 더하기 기계 (값을 도출하는 함수)
def add(a,b):
    result = a + b
    return result # 계산된 return를 밖으로 던저줌

# 함수 쓰기
# add(3,5)가 실행되면 그 자리의 숫자가 8로 바뀐다고 보면 됨
sum_value = add(3,5)

print(f"계산 결과: {sum_value}")
print(f"여기에 10을 더하면: {sum_value + 10}")


