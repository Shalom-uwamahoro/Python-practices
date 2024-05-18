# arithmetic questions

# question1
a=15
b=7
sum=a+b
print(sum)

#question2
prod=4*9
print(prod)

#question3
x=20
y=6
div=x/y
print(div)

#question4
mod=17%4
print(mod)

#question5
power=2 ** 3
print(power)

 #question6
sub=12 - 30
print(sub)

#question7
floordiv= 25//4
print(floordiv)

#question 8
addneg=5 + -8
print(addneg)

#question 9
neg=-(-15)
print(neg)

#question 10
multi=10 * 0
print(multi)

#Assignment operators

#question 1
x=5
print(x)

#question 2

y=15
y +=10
print(y)

#question3

z=8
z -= 3

#question 4

a=7
a *=4
print(a)

#question 5

b=20
b /=2
print(b)

#question 6

c=16
c %= 5
print(c)

#question 7
d=2
d **=3
print(d)

# question 8

e=25
e //=3
print(e)

#question 9

f=100
f |=25
print(f)

#question10

g=12
g ^= 7
print(g)

# Comparison Operators

# qstn1

k=10
l=5
print(k>l)

# qstn2

x=15
y=15
w=x==y
print(w)

# qstn3

x=20
y=25
print(x!=y)

# qstn4

x=8
y=12
print(x<y)

# qstn5

x=10
y=10
print(x>=y)

# qstn6

x=7
y=6
print(x<=y)

# qstn7

x='Hello'
y='World'
print(x!=y)

# qstn8

x=True
y=False
print(x==y)

# qstn9

x='apple'
y='apple'

print(x==y)

# qstn10

x=True
y=1
print(x==y)

print(True and False ==True)

print(True or False == True)

print(not True)

h= 10 >5 and 20 <15
print(h)

print(8 == 8 or 7 != 7)

print(not 15 <= 10)

print("Hello" and "Word" != " ")

print(not 10 >= 15)

print(True and 1 == True )


#Identity operators

# Question 1

x = "car"
y = "airplane"

if (x is y):
    print







class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)

root = Node(5)
root.left = Node(7)
root.right = Node(10)
root.left.left = Node(11)
root.left.right = Node(13)
root.right.right = Node(15)

print("inorderTraversal:")
inorderTraversal(root)