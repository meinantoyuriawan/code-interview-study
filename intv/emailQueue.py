from collections import deque

# pak budi menerima email
# setiap R detik akan membuka inbox
# membaca E email terbaru
# diatur sehingga inbox hanya menyimpan M buah email terbaru saja
# diatur sehingga selalu menghapus email yang sudah lebih dari X detik
# diberikan N email, tentukan berapa email yang dibaca
# diberikan n buah email T yang menyatakan detik kedatangan email

def readEmail(R, E, M, X, N, T):
    q = deque()
    i = R
    # loop through T and add to q
    t_temp = T[0:R]
    t_remain = T[R:]
    # q.append(t_temp)
    for t in t_temp:
        q.append(t)
    count_read = 0
    while q:
        # print("init", q)
        i += R
        pop_amount = min(len(q), E)
        for j in range(pop_amount):
            # print("first pop", q)
            count_read+=1
            q.pop()
            # print(count_read)

        t_temp = t_remain[0:i]
        t_remain = t_remain[i:]
        
        if len(q) + len(t_temp) > M:
            # popleft_amount = min(len(q)+len(t_temp)-M, len(q))
            popleft_amount = len(q)+len(t_temp)-M
            # print(popleft_amount)
            for j in range(popleft_amount):
                # print("second pop", q)
                q.popleft()

        # check expiry
        expiry_pop = 0
        for j in range(len(q)):
            if i-q[j] > X:
                expiry_pop += 1
        
        for j in range(expiry_pop):
            q.popleft()

        # print('q', q)

        for t in t_temp:
            q.append(t)

    return count_read

def run():
    # this works
    R = 4
    E = 2
    M = 5
    X = 6
    N = 8
    T = [1,2,3,4,5,6,7,8]
    result = readEmail(R, E, M, X, N, T)
    print(result)

    R = 10000
    E = 1
    M = 10
    X = 100000
    N = 10
    T = [1,1,1,1,1,1,1,1,1,1]

    result = readEmail(R, E, M, X, N, T)
    print(result)
    R = 1
    E = 5
    M = 10
    X = 100
    N = 10
    T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = readEmail(R, E, M, X, N, T)
    print(result)

    R = 100   # Pak Budi checks every 100 seconds
    E = 10
    M = 50    # Inbox can hold 50 emails
    X = 1000
    N = 5
    T = [1, 1, 1, 1, 1]
    result = readEmail(R, E, M, X, N, T)
    print(result)

    R = 2
    E = 1
    M = 10
    X = 100
    N = 10
    T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = readEmail(R, E, M, X, N, T)
    print(result)

run()