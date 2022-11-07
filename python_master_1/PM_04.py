# URL에서 퀴리 문자열 추출하기
url = "https://post.naver.com/viewer/postView.nhn?volumeNo=27174949&memberNo=37451778&navigationType=push"

url = url.split("?")
url = url[1].split("&")

for i in url:
    print(i)