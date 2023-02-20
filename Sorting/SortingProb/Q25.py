#실패율
#실패율은 다음과 같이 정의한다.
#스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

#스테이지의 개수N, 스테이지의 번호가 담긴 배열 stages
def solution(N, stages):
    answer = []
    length = len(stages) #도전자의 수 ex) 8
    
    for i in range(1,N+1):
        count = stages.count(i)

        if length == 0: #도전자 없으면 
            fail = 0 #실패율 0 간주
        else:
            fail = count / length #아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
        
        #answer리스트에 (스테이지번호,실패율) 로 넣어
        answer.append((i,fail))
        length -= count
    #실패율 기준으로 내림차순 정렬
    answer = sorted(answer,key=lambda x:x[1],reverse=True)


    #정렬된 번호 반환
    answer = [i[0] for i in answer]
    return answer