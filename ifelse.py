Scissor = '가위'
Rock = '바위'
Paper = '보'

Win = '이겼다'
Draw = '비겼다'
Lose = '졌다'

mine = '가위'
yours = '바위'

if mine == yours:
    result = Draw
else:
    if mine == Scissor:
        if yours == Rock:
            result = Lose
        else:
            result = Win
    else:
        if mine == Rock:
            if yours == Paper:
                result = Lose
            else:
                result = Win
        else:
            if mine == Paper:
                if yours == Scissor:
                    result = Lose
                else:
                    result = Win
            else:
                print('이상해요')
print(result)

#위의 코드를 elif로 수정
if mine == yours:
    result = Draw
else:
    if mine == Scissor:
        if yours == Rock:
            result = Lose
        else:
            result = Win
    elif mine == Rock:
        if yours == Paper:
            result = Lose
        else:
            result = Win
    elif mine == Paper:
        if yours == Scissor:
            result = Lose
        else:
            result = Win
    else:
        print('이상해요')
print(result)
# 코드의 가독성을 위해 else 뒤 나오는 if가 있을 시 elif로 정리해주는게 좋다