# 1. tkinter 모듈 가져오기
# tkinter라는 도구를 가져오는데 이름이 기니 "tk"라고 줄임
import tkinter as tk

# 2. 창 만들기
# 모든 화면 구성요소를 담을 틀을 만듦
# 보통 변수 이름으로 'root' 와 'win'을 많이 사용
root = tk.Tk()

# 3. 창 제목 설정
# 윈도우 창 맨위 뜨는 글자
root.title("나의 첫 GUI 프로그램")

# 4. 창 크기 설정
root.geometry("400x300")

# 5. 창 꺼지지 않도록 계속 실행
root.mainloop()