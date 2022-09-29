#第一題

def calculate(min, max, step):

   
    a = 0
    numbers = list(range(min, max+1, step))
    a = a + sum(numbers)
    return a


calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

print(calculate(1, 3, 1))
print(calculate(4, 8, 2))
print(calculate(-1, 2, 2))

#第二題

def avg(data):
    
# 請用你的程式補完這個函式的區塊

    avg({
    "employees":[
    {
    "name":"John",
    "salary":30000,
    "manager":False
    },
    {
    "name":"Bob",
    "salary":60000,
    "manager":True
    },
    {
    "name":"Jenny",
    "salary":50000,
    "manager":False
    },
    {
    "name":"Tony",
    "salary":40000,
    "manager":False
    }
    ]
    }) # 呼叫 avg 函



