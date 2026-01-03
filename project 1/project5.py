#메이플 인벤토리라고 생각해보기
inventory = ["빨간 포션", "파랑 포션", "엘릭서", "귀환주문서"]

# 1.전체 출력
print(inventory)

# 2.하나만 꺼내기
print(inventory[0])
print(inventory[2])

# 3.추가하기
inventory.append("황금사과")
print("아이템 추가 후:", inventory)

# 4.삭제하기
inventory.remove("파랑 포션")
print("아이템 삭제 후:", inventory)