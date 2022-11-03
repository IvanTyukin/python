"""
Описать функцию min(X) для определения минимального элемента линейного массива X, 
введя вспомогательную рекурсивную функцию minl(k), находящую минимум среди последних 
элементов массива X, начиная с k-го.
"""

def minX(X):
    k = 0 
    def min1(k):
        if k == n - 1:
            mn = X[k]
            return mn
        else:
            if X[k] < min1(k+1):
                mn = X[k]
            else:
                mn = min1(k+1)
            return mn
    minii = min1(k)
    return minii


n = int(input())
arr1 = []
for i in range(n):
    arr1.append(int(input()))

mini = minX(arr1)
print("Минимальный элемент: ",mini)