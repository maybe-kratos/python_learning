# fruits = eval(input( " tu bata:"))
fruits = ["Apple", "Banana", "Desi_Ghee"]


def make_pie(index):
    fruit = fruits[index]
    print("Your order is "+fruit + " pie")


try:
    index = int(input("Enter the index :"))
    make_pie(index)
except IndexError as e:
    print("Your order is Fruit Pie")
else:
    pass
finally:
    print("Do visit again😀.")