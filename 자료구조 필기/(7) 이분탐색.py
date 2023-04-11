# 이분탐색 (Binary Search)
"""
- 탐색 전 반드시 정렬된 상태로 시작
- 살펴보는 범위를 절반씩 줄여나가며 답을 찾기
- 1회가 아닌, 여러 번 탐색해야 할 때는 선형탐색보다 유리함


시간복잡도
정렬 과정: O(NlogN)
이진탐색: O(NlogN)
O(NlogN) + O(NlogN) = O(2NlogN) => O(NlogN)
"""

# bisect_left/right
from bisect import bisect_left, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 9)

three = bisect_right(v, 3) - bisect_left(v, 3) # index(4) - index(2) => 2
print(f'number of 3: {three}') # 2


# 매개변수 탐색 (Parametric Search)
"""최적화 문제를 결정 문제로 바꿔서 이진탐색으로 푸는 방법"""

# 최적화 문제 (Optimization Problem)
"""문제 상황을 만족하는 변수의 최댓값, 최솟값을 구하는 문제"""

# 결정 문제 (Decision Problem)
"""맞다/아니다, Yes/No, True/False를 구하는 문제"""

"""Parametric Search의 예시
시험 참가자 중 상위 10%가 합격일 때, 몇 점 이상이면 합격인가?
-> 참가자들의 성적을 일렬로 나열 후, 합격과 불합격의 임계 점수를 구하는 문제로 바꿀 수 있다

최적화 문제: 합격(문제 상황)인 점수(변수)의 최댓값, 최솟값을 구하는 문제
결정 문제: 몇 점이 합격의 최솟값인가
"""

# Parametric Search의 특징
"""
- 매개변수가 주어지면 true/false가 결정되어야 한다
- 가능한 해의 영역이 연속적이어야 한다
- 범위를 반씩 줄여나가면서 true/false를 구한다
- 이진탐색과 똑같은 원리
"""