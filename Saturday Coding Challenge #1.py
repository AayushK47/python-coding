def check(cookie,to_check):
    i,j = to_check[0]
    if((i-1 >= 0 and j >= 0) and (i-1 < m and j < n) and (cookie[i-1][j] == 1)):
        to_check.append((i-1,j))
    elif((i >= 0 and j-1 >= 0) and (i < m and j-1 < n) and (cookie[i][j-1] == 1)):
        to_check.append((i,j-1))
    elif((i+1 >= 0 and j >= 0) and (i+1 < m and j < n) and (cookie[i+1][j] == 1)):
        to_check.append((i+1,j))
    elif((i >= 0 and j+1 >= 0) and (i < m and j+1 < n) and (cookie[i][j+1]) == 1):
        to_check.append((i,j+1))
    cookie[i][j] = -1

def bfs(cookie, m, n, i, j):
    to_check = [(i,j)]
    l = 0
    while(len(to_check)):
        l += 1
        check(cookie, to_check)
        to_check.pop(0)
    return l

m, n = map(int,input('Enter the height and width of cookie: ').split())

cookie = []
temp_n = n

for i in range(m):
    while(temp_n != 0):
        row = list(map(int,input().split()))
        if(len(row) != n):
            print('Wrong input format, TRY AGAIN!!')
        else:
            temp_n -=1
            cookie.append(row)

lengths = []

for i in range(m):
    for j in range(n):
        if(cookie[i][j] == 1):
            lengths.append(bfs(cookie,m,n,i,j))

print(lengths)
