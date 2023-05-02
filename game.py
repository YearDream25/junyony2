def User_Input():
  while True:
   a, b, c, d = map(int, input("사용자 입력(ex. 1,2,3,4):").split(','))
   if len(set([a,b,c,d])) == 4:
     break
   print("중복된 값이 있습니다. 다시 입력해주세요") 
  return [a, b, c, d]

def Random_Input():
 print("랜덤")

def Process():
 print("처리")

if __name__ == "__main__":
 User_Input()
 Random_Input()
 Process()


