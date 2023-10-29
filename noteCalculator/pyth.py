amount = int(input("enter amount "))
n500 = amount // 500 
amount-=n500 * 500
n100 = amount // 100
amount-=n100 * 100
n50 = amount // 50
amount-=n50 * 50
n20 = amount//20
amount-=n20 * 20
n10 = amount//10
amount-=n10*10
n5 = amount//5
amount -= n5*5
n1 = amount // 1
print("n500 ", n500)
print("n100", n100)
print("n50", n50)
print("n20", n20)
print("n10", n10)
print("n5 ", n5)
print("n1", n1)





''' another method for same programe'''
print("-----------------------another way------------------------")

amount = int(input("enter amount "))
n500 = amount // 500 
amount = amount%500
n100 = amount // 100
amount = amount%100
n50 = amount // 50
amount = amount%50
n20 = amount//20
amount = amount%20
n10 = amount//10
amount%=10
n5 = amount//5
amount %=5
n1 = amount//1
print("n500 ", n500)
print("n100", n100)
print("n50", n50)
print("n20", n20)
print("n10", n10)
print("n5 ", n5)
print("n1", n1)