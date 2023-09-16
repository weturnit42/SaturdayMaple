import cv2
import random
import tkinter

MAX = 65
DIV = 7

global checkIdx
checkIdx = []

global next
next = 0

def quizCheck(num, count=3):
    print(num)
    cv2.destroyAllWindows()
    # src = player[num]
    blanksrc = cv2.imread("blank" + ".jpg" , cv2.IMREAD_COLOR)
    src=cv2.imread("test (" + str(num) +").png" , cv2.IMREAD_COLOR)
    # src=cv2.imread("ami" +".jpg" , cv2.IMREAD_COLOR)
    # src=cv2.imread("mano.png" , cv2.IMREAD_COLOR)
    sh, sw, sc = src.shape

    if(sh > sw):
        # src = cv2.resize(src, dsize=(540, 960), interpolation=cv2.INTER_AREA)
        src = cv2.resize(src, dsize=(0, 0), fx=450/sw, fy=450/sw, interpolation=cv2.INTER_AREA)
    else:
        # src = cv2.resize(src, dsize=(960, 540), interpolation=cv2.INTER_AREA)
        src = cv2.resize(src, dsize=(0, 0), fx=800/sh, fy=800/sh, interpolation=cv2.INTER_AREA)
    
    face=src.copy()
    h, w, c = face.shape
    face=src[0:h, 0:w] #size:h. size:w
    blank=blanksrc.copy()
    blank=blanksrc[0:5000, 0:5000]

    # cv2.imshow("face", face)

    hStep = h // DIV
    wStep = w // DIV

    blankFaces = []
    realFaces = []

    for i in list(range(DIV)):
        for j in list(range(DIV)):
            blankFaces.append(blank[1+i*hStep:(i+1)*hStep, 1+j*wStep:(j+1)*wStep])
            realFaces.append(face[1+i*hStep:(i+1)*hStep, 1+j*wStep:(j+1)*wStep])

    idx = list(range(DIV*DIV))
    
    temp = 0
    threshold = 0
    if(tryCount == 3):
        threshold = 3
    else:
        threshold = 1
    while(temp < threshold):
        rand = random.randint(0, DIV*DIV-1)

        if(rand in checkIdx):
            continue
        elif(rand not in checkIdx):
            checkIdx.append(rand)
            temp = temp+1
    print(checkIdx)
    checkFaces = []

    for i in list(range(DIV*DIV)):
        if(i in checkIdx):
            checkFaces.append(realFaces[i])
        else:
            checkFaces.append(blankFaces[i])

    imgCon = []
    for i in list(range(DIV)):
        temp = cv2.hconcat([checkFaces[i*DIV+0], checkFaces[i*DIV+1]])
        for j in list(range(2, DIV)):
            temp = cv2.hconcat([temp, checkFaces[i*DIV+j]])
        imgCon.append(temp)

    dst = cv2.vconcat([imgCon[0], imgCon[1]])
    for i in list(range(2, DIV)):
        dst = cv2.vconcat([dst, imgCon[i]])

    winname = str(num)
    cv2.namedWindow(winname)   # create a named window
    cv2.moveWindow(winname, 40, 30)   # Move it to (40, 30)
    cv2.imshow(str(num), dst)

win = tkinter.Tk()

btn = tkinter.Button(win, text = 'btn', background='white')

ent = tkinter.Entry(win)
ent.pack()

btn.config(width=5, height=2)
btn.config(text = "button")
btn.pack()

global tryCount
tryCount = 3
global answer
global answerList
answerList = []

global ANSWER
ANSWER = []
ANSWER.append((0, "칼리"))
# ANSWER.append((1, "MR.판쵸"))
# ANSWER.append((2, "가시덤불"))
# ANSWER.append((3, "각성의 비약"))
ANSWER.append((1, "관조자"))
ANSWER.append((2, "극한 성장의 비약"))
ANSWER.append((3, "근원에 다다른 기사"))
ANSWER.append((4, "세글자"))
ANSWER.append((5, "김창섭"))
ANSWER.append((6, "난폭한 원시멧돼지"))
ANSWER.append((7, "날치"))
ANSWER.append((8, "니오라 병원"))
ANSWER.append((9, "다크 엑스텀프"))
ANSWER.append((10, "다크나이트"))
ANSWER.append((11, "돼지"))
ANSWER.append((12, "라라"))
ANSWER.append((13, "랑"))
ANSWER.append((14, "레이스"))
# ANSWER.append((15, "세피"))
ANSWER.append((15, "리스항구"))
ANSWER.append((16, "오즈")) 
ANSWER.append((17, "초보자"))
ANSWER.append((18, "무릉"))
ANSWER.append((19, "묵그림자 두루미"))
ANSWER.append((20, "미하일"))
ANSWER.append((21, "베릴")) 
ANSWER.append((22, "분노의 에르다스"))
# ANSWER.append((27, "분노한 고스텀프"))
ANSWER.append((23, "블러디 퀸"))
ANSWER.append((24, "비숍"))
ANSWER.append((25, "강원기"))
ANSWER.append((26, "빨간달팽이"))
ANSWER.append((27, "슈피겔만"))
ANSWER.append((28, "스톤골렘"))
ANSWER.append((29, "슬라임"))
ANSWER.append((30, "슬라임"))
ANSWER.append((31, "시간의 눈"))
ANSWER.append((32, "아델"))
ANSWER.append((33, "아란"))
ANSWER.append((34, "아르카누스"))
ANSWER.append((35, "아리안트"))
ANSWER.append((36, "암시장"))
ANSWER.append((37, "앵글러 로봇 C형"))
# ANSWER.append((43, "에릭손"))
ANSWER.append((38, "엔젤릭버스터"))
ANSWER.append((39, "예티와 페페"))
ANSWER.append((40, "오한별"))
# ANSWER.append((47, "우두머리 괴물 갈매기"))
ANSWER.append((41, "우르스"))
# ANSWER.append((49, "위협적인물"))
ANSWER.append((42, "유령 스탄"))
ANSWER.append((43, "유타"))
ANSWER.append((44, "이름 없는 마을"))
ANSWER.append((45, "이피아"))
# ANSWER.append((54, "잊힌 고향"))
# ANSWER.append((55, "장로스탄의 집"))
ANSWER.append((46, "제논"))
ANSWER.append((47, "좀비버섯"))
ANSWER.append((48, "주니어 발록"))
ANSWER.append((49, "주인잃은 왓치독"))
ANSWER.append((50, "주황버섯"))
# ANSWER.append((61, "철이"))
ANSWER.append((51, "콜드샤크"))
ANSWER.append((52, "쿠스코"))
ANSWER.append((53, "클랑"))
ANSWER.append((54, "키르스턴"))
ANSWER.append((55, "타락마족 이글라이더"))
ANSWER.append((56, "T-boy"))
ANSWER.append((57, "파풀라투스"))
ANSWER.append((58, "판타스틱 테마파크"))
ANSWER.append((59, "평화로운 잠수정"))
ANSWER.append((60, "피그미"))
ANSWER.append((61, "핑크빈"))
ANSWER.append((62, "하이레프 기갑병"))
ANSWER.append((63, "하프"))
ANSWER.append((64, "흙의 정령"))

    
def testCheck():
    # ent.set(" ")
    global tryCount
    # global answer
    global checkIdx
    global next
    # print(next)
    # print(ANSWER[next][1].replace(" ", ''))
    
    if(ent.get() == 'quit'):
        cv2.destroyAllWindows()
        exit(0)

    # if(ent.get() == "ok"):
    #     cv2.destroyAllWindows()
    #     # next = random.randint(0, MAX)
    #     # while(next in answerList):
    #     #     next = random.randint(0, MAX)
    #     # answer = next
    #     # answerList.append(answer)

        # next = next + 1

        # checkIdx = []
        # tryCount = 1

        # quizCheck(next, 1)

    if(ent.get() == 'pass'):
        # next = random.randint(0, MAX)
        # while(next in answerList):
        #     next = random.randint(0, MAX)
        # answer = next
        # answerList.append(answer)
        next = next + 1

        # if(sorted(answerList) == list(range(MAX+1))):
        if(next == MAX):
            print("end")
            cv2.destroyAllWindows()
            exit(0)

        checkIdx = []
        tryCount = 3

        print(next)
        quizCheck(next, 3)

    elif (ent.get().replace(" ", '') == ANSWER[next][1].replace(" ", '')):
        cv2.destroyAllWindows()
        src=cv2.imread("test (" + str(next) +").png" , cv2.IMREAD_COLOR)
        # src=cv2.imread("test " + str(next) +".png" , cv2.IMREAD_COLOR)
        sh, sw, sc = src.shape
        
        if(sh > sw):
            src = cv2.resize(src, dsize=(0, 0), fx=450/sw, fy=450/sw, interpolation=cv2.INTER_AREA)
        else:# src = cv2.resize(src, dsize=(960, 540), interpolation=cv2.INTER_AREA)
            src = cv2.resize(src, dsize=(0, 0), fx=800/sh, fy=800/sh, interpolation=cv2.INTER_AREA)

        winname = "THE ANSWER IS..!!!"
        cv2.namedWindow(winname)   # create a named window
        cv2.moveWindow(winname, 40, 30)   # Move it to (40, 30)
        cv2.imshow(winname, src)
        cv2.waitKeyEx()
        next = next + 1

        # if(sorted(answerList) == list(range(MAX+1))):
        if(next == MAX):
            print("end")
            cv2.destroyAllWindows()
            exit(0)

        print("congrats")

        checkIdx = []
        tryCount = 3

        quizCheck(next, 3)

    elif (ent.get().replace(" ", '') != ANSWER[next][1].replace(" ", '')):
        tryCount = tryCount + 1
        if(tryCount == 40):
            print("fail")
            cv2.destroyAllWindows()
            exit(0)
        else:
            print("error")
            quizCheck(next, count=tryCount)

    else:
        print("비상")

flag = "check"
# next = 0
# next = random.randint(0, MAX)
# answer = next
answerList.append(next)

# if(flag != "check"):
#     quiz(start)
#     btn.config(command=test)
if(flag == "check"):
    quizCheck(next)
    btn.config(command=testCheck)

win.mainloop()