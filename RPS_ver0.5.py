import random

hands=["ぐー","ちょき","ちょき"]
win={"ぐー":"ちょき","ちょき":"ぱー","ぱー":"ぐー",}

you_score=0
com_score=0

print("3回勝負!!!")
print("同点だったら勝ちが決まるまでサドンデス！")

#--------3回戦---------
for i in range(1,4):
    print(f"\n--- {i}回戦 ---")
    you=input("ぐー / ちょき / ぱー を入力(qで終了)：").strip()
    if you=="q":
     print("終了")
     exit()
     if you not in hands:print("正しく入力してね")

     com=random.choice(hands)
     
     print(f"あなた:{you}")
     print(f"相手:{com}")

     if you==com:
        print("あいこ")

     elif win[you] == com:
        print("勝ち")
        you_score +=1

     else:
        print("負け")
        com_score +=1

print("\n=== 3回戦の結果 ===")
if you_score >= com_score:
      print("3回戦の結果、勝ち!")
elif you_score <= com_score:
      print("3回戦の結果、負け。")
else:
    print("3回戦の結果、同点!")
    print("サドンデス開始!!!")


while True:
    you=input("ぐー / ちょき / ぱー を入力(qで終了)：").strip()
    if you=="q":
     print("終了")
     exit()
     if you not in hands:print("正しく入力してね")

     com=random.choice(hands)
     
     print(f"あなた:{you}")
     print(f"相手:{com}")

     if you==com:
        print("あいこ!もう一回！")
        continue
     
     elif win[you] == com:
        print("あなたの勝ち！！！")
        break

     else:
        print("あなたの負け。。。")
        break
     


      


