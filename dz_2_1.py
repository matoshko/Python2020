import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a

def insert(A):
    for i in range(len(A)):
        v = A[i]
        j = i;
        while (A[j - 1] > v) and (j > 0):
            A[j] = A[j - 1]
            j = j - 1
        A[j] = v

def select(A): ## сотрировка не работает, не понимаю почему....
    for i in range(len(A)-1):
        m = i
        j = i+1
        while j<len(A):
            if A[j] < A[m]:
                m = j
            j = j+1
        A[i], A[m] = A[m], A[i]


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время Insert", "Время Select"])
x=[]
y1=[]
y2=[]
y3=[]


for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    # print(B)

    # BubbleSort(A)
    #print("---")
    # print(A)

    C = A.copy()
    #insert(C)
    #print(C)

    D = A.copy()
    #select(D)
   # print(D)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    insert (B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Insert   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    select(D)
    t6 = datetime.datetime.now()
    y2.append((t6 - t5).total_seconds())
    print("Select   " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds()), str((t6-t5).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.show()
