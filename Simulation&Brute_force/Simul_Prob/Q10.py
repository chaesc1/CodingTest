#자물쇠와 열쇠
#프로그래머스 60059

#90도 회전 알고리즘

def rotation90(arr):
    #행길이
    n = len(arr)
    #열길이
    m = len(arr[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length,lock_length * 2):
        for j in range(lock_length,lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key,lock):
    answer = True
    n = len(lock)
    m = len(key)

    new = [[0] * (n * 3) for _ in range(n * 3)]#3배 확장시켜 0으로 초기화

    #확장시킨 맵에다가 자물쇠를 중앙에 배치
    for i in range(n):
        for j in range(n):
            new[i+n][j+n] = lock[i][j]

    #4가지 방향에 대해서 탐색
    for i in range(4):
        key = rotation90(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new[x + i][y + j] += key[i][j]
                #새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if check(new) == True:
                    return True
                #자물쇠에서 열쇠를 다시 빼야해
                for i in range(m):
                    for j in range(m):
                         new[x + i][y + j] -= key[i][j]
    return False

print(solution(([0,0,0],[1,0,0],[0,1,1]),([1,1,1],[1,1,0],[1,0,1])))