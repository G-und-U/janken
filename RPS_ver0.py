import random

hand=["ぐー","ちょき","ぱー"]
print("最初はぐー！！じゃんけん...")
you=input("ぐーちょきぱーを入力してね:")

com=random.choice(hand)

print(f"相手：{com}")
print(f"あなた：{you}")




#勝敗判定
if com==you:
    print("あいこ")
elif(com=="ぐー"and you=="ぱー") or \
    (com=="ちょき"and you=="ぐー") or \
    (com=="ぱー"and you=="ちょき"):
    print("かち！")

elif(you=="ぐー"and com=="ぱー") or \
    (you=="ちょき"and com=="ぐー") or \
    (you=="ぱー"and com=="ちょき"):
    print("まけ；；")

else:
    print("なにこれ、、、？")





