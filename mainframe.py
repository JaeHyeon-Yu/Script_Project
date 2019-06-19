from tkinter import *
from tkinter import font
from openapi import LoadXML2API
import kakaomap
locData = [0]*25
def InitMainframe(window):
    global mainframe

    mainframe = Frame(window)
    mainframe.pack()
    InitTopText(window)
    InitInputLabel(window)
    InitSearchButton(window)
    InitNameText(window)
    InitInfoText(window)
    InitMap(window)
    InitGmail(window)
    InitTeleButton(window)
    InitGraphButton(window)

def InitTopText(window):
    # 타이틀 문장 출력
    TempFont = font.Font(window, size=20, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="[서울시 문화재 검색]", fg="red").place(x=50, y=10)

def InitInputLabel(window):
    # 키값 입력창 삽입
    global inputLabel

    TempFont = font.Font(window, size=17, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="이름").place(x=10, y=60)
    inputLabel = Entry(window, font=TempFont, width=15, borderwidth=5, relief='ridge')
    inputLabel.place(x=70, y=55)

def InitSearchButton(window):
    # 검색버튼 삽입
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    searchButton = Button(window, font=TempFont, text="검색", borderwidth=3, command= lambda :SearchAction(window))
    searchButton.place(x=285, y=53)


def SearchAction(window):
    # 검색 실행
    NameText.configure(state='normal')
    NameText.delete(0.0, END)
    InfoText.configure(state='normal')
    InfoText.delete(0.0, END)
    LoadXML2API()
    InitDrawMap(window)

def InitNameText(window):
    # 검색 결과 출력창
    global NameText
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="명칭").place(x=13, y=110)

    NameText = Text(window, font=TempFont, width=30, height=2, borderwidth=5, relief='ridge')
    NameText.place(x=13, y=140)

    NameText.configure(state='disable')

def InitInfoText(window):
    global InfoText
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="정보").place(x=13, y=220)

    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    InfoText = Text(window, font=TempFont, width=37, height=17, borderwidth=5, relief='ridge')
    InfoText.place(x=13, y=250)

    InfoText.configure(state='disable')

def InitMap(window):
    global mapCanvas
    TempFont = font.Font(mainframe, size=15, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="지도").place(x=390, y=10)
    mapCanvas = Canvas(window, relief="solid", bd=2, height=300)
    mapCanvas.place(x=390, y=50)
def InitDrawMap(window):
    import Map
    global Image_RestArea

    x, y = kakaomap.SearchPos()
    Image_RestArea = Map.Draw_MapImage(x, y)
    mapCanvas.create_image(160, 100, image=Image_RestArea)
def InitGmail(window):
    TempFont = font.Font(mainframe, size=15, weight='bold', family='Consolas')
    Label(window, font=TempFont, text="메일").place(x=390, y=400)

    global mailLabel
    mailLabel = Entry(window, font=TempFont, width=25, borderwidth=5, relief='ridge')
    mailLabel.place(x=390, y=430)

    mailButton = Button(window, font=TempFont, text="보내기", command=SendGmail)
    mailButton.place(x=687, y=427)

def SendGmail():
    import gmail
    destination = mailLabel.get()
    gmail.SendMail(destination)

def InitTeleButton(window):
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    teleButton = Button(window, font=TempFont, text="텔레그램", borderwidth=3, command=ExcuteTele)
    teleButton.place(x=390, y=500)

def InitSpam(window):
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    # Label(window, font=TempFont, text="정보").place(x=130, y=220)
    pass

def ExcuteTele():
    from teller import Excute
    Excute()

def InitGraphButton(window):
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    teleButton = Button(window, font=TempFont, text="그래프", borderwidth=3, command=DrawGraph)
    teleButton.place(x=510, y=500)

def DrawGraph():
    global subwin
    subwin = Tk()
    subwin.title("소재지 그래프")
    w, h = 1200, 300
    canvas = Canvas(subwin, width=w, height=h)
    canvas.pack()

    max_count = int(max(locData))
    canvas.create_line(10, h - 10, w - 10, h - 10)
    ww = (w - 25) / 25
    for i in reversed(range(25)):
        canvas.create_rectangle(i * ww + 10, h - locData[i] * (h - 20) / max_count,
                                         (i + 1) * ww + 10, h - 10, tags='grim')

        if locData[i] != 0:
            canvas.create_text(i * ww + 30, h - locData[i] * (h - 20) / max_count - 5,
                                    text=str(locData[i]), tags="grim")
        canvas.create_text(i * ww + 30, h - 10 + 5, text=LocText(i), tags="grim")
def LocText(n):
    if n == 0:
        return "강남구"
    elif n == 1:
        return "강동구"
    elif n == 2:
        return "강북구"
    elif n == 3:
        return "강서구"
    elif n == 4:
        return "관악구"
    elif n == 5:
        return "광진구"
    elif n == 6:
        return "구로구"
    elif n == 7:
        return "금천구"
    elif n == 8:
        return "노원구"
    elif n == 9:
        return "도봉구"
    elif n == 10:
        return "동대문구"
    elif n == 11:
        return "동작구"
    elif n == 12:
        return "마포구"
    elif n == 13:
        return "서대문구"
    elif n == 14:
        return "서초구"
    elif n == 15:
        return "성동구"
    elif n == 16:
        return "성북구"
    elif n == 17:
        return "송파구"
    elif n == 18:
        return "양천구"
    elif n == 19:
        return "영등포구"
    elif n == 20:
        return "용산구"
    elif n == 21:
        return "은평구"
    elif n == 22:
        return "종로구"
    elif n == 23:
        return "중구"
    elif n == 24:
        return "중랑구"