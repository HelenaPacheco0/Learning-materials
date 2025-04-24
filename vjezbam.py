print("Unesi milimetre, da bi ih pretvorili u cm, m i kilometre")
mili=int(input("Unesi broj milimetara: "))

centi=mili//10
mili1=mili%10
centi1=centi%10
met=centi//100
met1=met%1000
km=met//1000

print(centi1, "centimetara")
print(met1,"metara")
print(km, "kilometara")
