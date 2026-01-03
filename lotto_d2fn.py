import random

print("인생 역전 로또 번호 생성기")
print("--------------------------")

#5번까지 반복합니다.
for i in range(5):
    # 1. 1부터 45까지의 숫자 통 만들기
    #range(1,46)은 1부터 45까지의 숫자를 만들어줌 (끝숫자 포함 안됨)
    number_pool = list(range(1,46))

    # 2. 6개 뽑기 (range.sample은 중복없이 뽑아줌)
    lotto = random.sample(number_pool,6)

    # 3. 정렬하기
    lotto.sort()

    # 4. 결과 출력
    # i는 0부터 시작하기 때문에 +1을 해줌
    print(f"{i+1}회차 자동 번호: {lotto}")
          
print("--------------------------")
print("행운을 빕니다")
