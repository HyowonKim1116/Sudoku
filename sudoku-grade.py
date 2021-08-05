# 1. 채점 함수 정의
def horizontal(board): #가로줄 채점 함수
    for i in range(9):
        s = set(board[i]) #가로줄 리스트를 집합으로 변환
        if len(s) < 9:    #집합 s에 중복값이 있을 경우
            return False  #False 반환
    return True #모든 가로줄에 중복이 없다면 True 반환

def vertical(board): #세로줄 채점 함수
    for i in range(9):
        s = set() #집합 s 선언 및 초기화
        for j in range(9):
            s.add(board[j][i])
        if len(s) < 9:   #집합 s에 중복값이 있을 경우
            return False #False 반환
    return True #모든 세로줄에 중복이 없다면 True 반환

def square(board): #3×3칸 채점 함수
    i, j = 0, 0 #인덱스 변수 선언 및 초기화
    while i < 9:
        while j < 9:
            s = set() #집합 s 선언 및 초기화
            for a in range(i, i + 3):
                for b in range(j, j + 3):
                    s.add(board[a][b])
            if len(s) < 9:   #집합 s에 중복값이 있을 경우
                return False #False 반환
            j += 3           #j값 3 증가
        i += 3 #i값 3 증가
        j = 0  #j값 초기화
    return True #모든 3×3칸에 중복이 없다면 True 반환

# 2. 스도쿠판 입력
print("< 스도쿠 채점 프로그램 >")
print("채점할 스도쿠 판을 입력하세요.")
sudoku = [] #스도쿠 판 리스트
for i in range(9):
    h = list(map(int, input().split())) #가로줄 리스트
    sudoku.append(h)

# 3. 스도쿠 채점 결과 출력
if not horizontal(sudoku): #가로줄 채점 반환값이 False일 경우
    result = "오답"
elif not vertical(sudoku): #세로줄 채점 반환값이 False일 경우
    result = "오답"
elif not square(sudoku):   #3×3칸 채점 반환값이 False일 경우
    result = "오답"
else:                      #모든 채점 반환값이 True일 경우
    result = "정답"

print(f"=> 입력하신 스도쿠는 {result}입니다.") #결과 출력