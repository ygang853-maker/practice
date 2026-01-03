score = int(input("점수를 입력하세요 (0~100):"))

if score >= 90:
    print(f"점수: {score}")
    print("학점: A")
elif score >= 80:
    print(f"점수: {score}")
    print("학점:B")
elif score >= 70:
    print(f"점수:{score}")
    print("학점: C")
else:
    print(f"점수{score}")
    print("등급:F (재수강 필요)")

print("학점 처리 완료되었습니다.")

  