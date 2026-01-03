import random #랜덤 기능 가져오기

print("===가위 바위 보 게임===")

# 1. 컴퓨터가 먼저 뽑습니다 (리스트 사용)
options = ["가위", "바위", "보"]
computer = random.choice(options)
#options 리스트 에서 하나를 랜덤으로 뽑아서 computer 변수에 저장

# 2. 내 선택 입력 받기 
user = input("가위, 바위, 보 중에 하나를 입력하세요:")

print("--------------------------------")
print(f"나:{user} vs 컴퓨터{computer}")
print("--------------------------------")

# 3. 승패 판단 
if user == computer:
    print("비겼습니다")
elif user == "가위":
    if computer == "보":
        print("승리")
    else:
        print("패배")
elif user == "바위":
    if computer == "가위":
        print("승리")
    else:
        print("패배")
elif user == "보":
    if computer == "바위":
        print("승리")
    else:
        print("패배")    
else: 
    print("잘못된 입력 입니다. 가위 바위 보 중 하나를 입력해주세요")            
