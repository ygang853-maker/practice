import tkinter as tk #tkinter를 tk라는 별명으로 가져오기

# 1. 기능을 만드는 곳 (함수 정의)

def pull_pin():
    
    # 버튼을 눌렀을 때 실행될 함수
    # 평소의 모습에서 변화를 주는 기능
    
    print("내 이름은 레제!") # 터미널에서 확인용

    #[핵심기술] .config() : 설정을 바꾸는 기능
    # label_img에게 이미지를 바꾸라고 지시
    label_img.config(image=bomb_image)

    label_text.config(text="밤!", fg = "red")

# 2. 화면 만드는 곳

#  (1) 윈도우 만들기
root= tk.Tk()
root.title("폭탄의 악마 레제") # 창 제목
root.geometry("300x400") # 창 크기

# (2) 이미지 불러오기
# 주의: 파일 이름을 틀리면 오류 발생
try:
    normal_image = tk.PhotoImage(file="reze_normal.png") # 평소 모습
    bomb_image = tk.PhotoImage(file="reze_bomb.png") # 변신 모습
except Exception as e:
    print("이미지 파일을 불러오지 못했습니다")
    print(f"오류 내용: {e}")
    # 이미지가 없어도 프로그램 실행
    normal_image = None
    bomb_image = None

# (3) 이미지 보여주기 (label 위젯)
# Label: 글자나 이미지를 보여주는 부품
label_img = tk.Label(root, image=normal_image)
label_img.pack() # .pack() : 화면에 배치하는 기능

# (4) 안내 문구 넣기
label_text = tk.Label(root, text="시골쥐와 도시쥐 중에 뭐가 더 좋아?", font=("맑은 고딕", 15, "bold"))
label_text.pack(pady=20) # pady: 위 아래 여백

#(5) 버튼 만들기
# command = pull pin : 버튼이 눌렸을 때 pull_pin 함수를 실행
# 괄호를 적지 않고 이름만 적기
btn = tk.Button(root, text = "핑! (CLICK)", font=("Arial",20), bg="red", command=pull_pin)
btn.pack(pady=10)

# 3. 프로그램 계속 실행

root.mainloop()
