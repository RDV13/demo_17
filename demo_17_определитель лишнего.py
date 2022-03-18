# Замер лишнего веса:

name=input("напиши свое имя:")
h=input("рост (м) =  (например: 1.77)")
h=float (h)
w=input("вес = (кг), (например: 75)")
w=int(w)

bmi=w/(h**2)
print("индекс массы тела: " + str(bmi))
if bmi<25:
    print("результат - у "+name+ " лишний вес не обнаружен")
else:
    print("результат - у "+name+ " есть лишний вес ...")

print(" ")
input ("for quit - press ENTER")
    
