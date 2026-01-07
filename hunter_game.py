import tkinter as tk
import random 

# 1. 게임 데이터(변수 & 리스트) - 데이터 창고

my_name = " " # 헌터 이름
level = 1 # 레벨(정수)
power = 10 # 공격력(정수)
inventory = ["주먹"] # 아이템 목록 (리스트)

# 2. 기능을 만드는 곳 (함수 - def

# [기능 1] 게임 시작 및 이름 설정(input 대용)
def start_game():
    global my_name # 함수 밖의 변수를 수정하기 위해서 global을 써야함
    
    #Entry(입력창)에 적힌 글자를 가져옴(.get())
    input_text = entry_name.get()

    #[if 문] 이름이 비어 있으면 경고
    if input_text == "":
        label_message.config(text="이름을 입력하면 모험이 시작됩니다", fg= "red")
    else: 
        my_name = input_text
        label_message.config(text=f"환영한다. 모험가 '{my_name} 이제 너의 모험은 시작이야", fg="blue")

        #이름 입력창과 버튼은 이제 필요 없으니 안 보이게 숨김
        entry_name.pack_forget()
        btn_start.pack_forget()

        #게임 버튼들을 화면에 보여줌
        frame_game.pack(pady=20)
        update_status() # 상태창 갱신

# [기능 2] 훈련하기 (Random + IF/ELIF/ELSE)
def train():
    global level, power

    # 1부터 10까지 주사위 돌리기
    dice = random.randint(1,10)
    
    #[IF/ELIF/ELSE] 확률 로직
    if dice >=8: #8,9,10 (대성공)
        level = level + 1
        power = power + 5
        msg = "대성공 레벨업을 했습니다.(공격력 +5)"
    elif dice >= 5: #4,5,6,7(성공)
        power = power + 2
        msg = "훈련 성공 근육량이 늘었습니다.(공격력 +2)"
    else: #1,2,3 (실패)
        msg = "아무일도 일어나지 않았습니다.(변화 없음)"

    label_message.config(text=msg, fg="black")
    update_status() # 상태창 갱신

# [기능 3] 무기 뽑기 (List + Random + For)
def gacha():
    # 뽑을 수 있는 아이템 목록 (리스트)
    shop_items = ["나무검", "녹슨칼", "황금도끼", "엑스칼리버", "꽝"]

    #Random 리스트에서 하나 뽑기(.choice)
    item = random.choice(shop_items)

    if item == "꽝":
        label_message.config(text="정말 아쉽습니다", fg="red")
    else:
        #[List] 인벤토리에 추가(.append)
        inventory.append(item)
        label_message.config(text=f"축하합니다 [{item}]확득", fg= "green")

    update_inventory() # 인벤토리 화면 갱신

#[기능 4] 화면 갱신 (f-string + config)
def update_status():
    # 상태 라벨을 바꿈
    label_status.config(text=f"Lv.{level}{my_name}(공격력: {power})")

#[기능 5] 인벤토리 보여주기(for문 활용)
def update_inventory():
    item_text = "가방: "

    #[For 문] 리스트에 있는 걸 하나씩 꺼내서 글자로 합침
    for i in inventory:
        items_text = items_text + f"[{i}]"

    label_inventory.config(text=items_text)


#3. 화면 꾸미기(GUI - Tkinter)

root = tk.Tk()
root.title("전설의 헌터 키우기")
root.geometry("400x500")

#(1) 타이틀 라벨
tk.Label(root, text="Hunter Game",font=("Arial",20,"bold")).pack(pady=10)

#(2) 상태창 & 메시지창
label_status = tk.Label(root, text="캐릭터를 생성하십시오", font=("맑은 고딕",15))
label_status.pack()

label_message=tk.Label(root,text="이름을 입력하고 시작하세요", fg="gray")
label_message.pack(pady=5)

label_inventory = tk.Label(root, text="가방: [주먹]", fg="blue")
label_inventory.pack(pady=5)

#(3) 시작화면 (입력창 + 버튼)
entry_name = tk.Entry(root,font=("맑은 고딕", 12))
entry_name.pack(pady=10)

btn_start = tk.Button(root, text="게임 시작", command=start_game, bg="yellow")
btn_start.pack()

# (4) 게임 버튼들 (처음엔 숨겨둠 -> Frame으로 묶음)
frame_game = tk.Frame(root) #버튼들을 담을 바구니

# 훈련 버튼
btn_train = tk.Button(frame_game, text="훈련하기", command=train,width=20, heigh=2)
btn_train.pack(pady=5)

# 뽑기 버튼
btn_gacha = tk.Button(frame_game, text="랜덤 무기 뽑기", command=gacha,width=20, heigh=2)
btn_gacha.pack(pady=5)

#4. 실행
root.mainloop()



        
 