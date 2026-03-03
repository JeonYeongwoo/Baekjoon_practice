# 지피티 힌트 참고해서 품.. 다시 풀이
    # 힌트:
    #     백준 1654번이면 👉 랜선 자르기 문제지?
    # (이분 탐색 문제)

    # 힌트만 단계적으로 줄게 👇

    # 🔹 1단계: 완전탐색은 왜 안될까?

    # 랜선 길이가 최대 2³¹-1 (약 21억) 까지 가능해.

    # 모든 길이를 1부터 하나씩 다 잘라보는 건 ❌ 절대 불가능.

    # → 길이에 대해 이분 탐색 해야 함.

    # 🔹 2단계: 무엇을 이분 탐색할까?

    # 보통 이분 탐색은 "인덱스"에 쓰지만
    # 이 문제는 랜선의 길이를 탐색하는 거야.

    # 즉:

    # 가능한 랜선 길이 L을 가정했을 때
    # N개 이상 만들 수 있는가?

    # 이걸 기준으로 탐색.

    # 🔹 3단계: 판별 함수 생각해보기

    # 어떤 길이 mid가 주어졌을 때

    # 각 랜선에서 만들 수 있는 개수는?

    # 랜선길이 // mid

    # 그걸 전부 더해서

    # 총 개수 >= N ?

    # 이면 그 길이는 가능한 길이

    # 🔹 4단계: 탐색 방향

    # 만들 수 있는 개수 ≥ N → 더 길게 잘라도 될 수도 있음
    # → left = mid + 1

    # 만들 수 있는 개수 < N → 너무 길게 자름
    # → right = mid - 1

    # 🔥 핵심 포인트 (많이 틀리는 부분)

    # mid = (left + right) // 2

    # 정답은 최대 길이를 구하는 것

    # 그래서 조건 만족하면 result = mid 저장해둬야 함

    # while 조건은 보통 left <= right

    # 💡 사고 흐름 정리
    # 1 ~ max(랜선길이) 범위에서
    # "이 길이로 N개 이상 만들 수 있는가?"를 기준으로
    # 최대 길이를 찾는다.

import sys

K, N = map(int, input().split())

inp = []

for _ in range(K):
    inp.append(int(sys.stdin.readline()))

inp.sort()

total_count = 0
left = 1
right= inp[len(inp) -1] # 최대값
mid = (left + right) // 2

while(left <= right):
    for l in inp:
        if (mid == 0):
            mid = 1
        total_count += l // mid
    
    if(total_count >= N):
        left = mid + 1
    else:
        right = mid -1
        
    mid = (left + right) // 2
    total_count = 0
    
# for l in inp:
#     total_count += l // mid
print(mid)