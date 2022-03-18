# Замер лишнего веса:

name=input("напиши свое имя:")
h=input("рост (м) =  (например: 1.77)")
h=float (h)
if h==0: h=1.77
w=input("вес = (кг), (например: 70)")
w=int(w)
if w==0: w=70

bmi=w/(h**2)
print("индекс массы тела: " + str(bmi))
if bmi<25:
    print("результат - у "+name+ " лишний вес не обнаружен")
else:
    print("результат - у "+name+ " есть лишний вес ...")

print(" ")
input ("for quit - press ENTER")
    
