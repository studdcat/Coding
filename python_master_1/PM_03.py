# 문자 코드 구하기
char = input('문자 1개를 입력하세요 : ')



print("문자 : {}\t코드값 : {}[{}]"  .format(char, ord(char), hex(ord(char))))