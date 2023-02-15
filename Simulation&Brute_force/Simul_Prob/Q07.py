#럭키 스트레이트

#특정조건에서 나가는 스킬 럭키스트레이트다.
#특정 조건이란 현재 캐릭터의 점수를 n이라고 할 때 자릿수를 기준으로
#점수 n을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과/ 오른쪽 부분의 각 자릿수 합을 더한값이 동일한 상황이다.

#해결방안 -> 왼쪽합 - 오른쪽합 = 0 --> 스킬 발동

n = input()
length = len(n)
sum = 0

for i in range(length//2):
    sum += int(n[i])

for i in range(length//2 , length):
    sum -= int(n[i])

if sum == 0:
    print("LUCKY")
else:
    print("READY")