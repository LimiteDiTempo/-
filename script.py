import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.google.com/" # https://www.instagram.com/sew00k/webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["white", "black"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "윤세욱")
write("description", "")
write("button", "Instagram")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "나이": "16살",
  "학교": "왕선중학교",
  "좋아하는 것": "게임(롤)",
  "MBTI": "INTP"
}
information(informations)