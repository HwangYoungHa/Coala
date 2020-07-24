players = ["황의조", "황희찬", "구자철", "이재성", "기성용"]

print("현재 경기 중인 선수 : ")
for name in players:
    print(name)

print("-" * 40)

getout = int(input("OUT 시킬 선수 번호: "))
getin = input("IN 할 선수 이름 : ")

del players[getout]
players.append(getin)

print("-"*40)
print("교체 결과:")
for name in players:
    print(name)
