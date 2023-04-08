import sys
# 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력 -> 딕셔너리형 자료 사용

input = sys.stdin.readline
books = {}
for _ in range(int(input())):
    x = input()
    if x in books:
        books[x] += 1
    else:
        books[x] = 1

best = max(books.values())
books = dict(sorted(books.items()))
for k, v in books.items():
    if best==v:
        print(k)
        break


"""
perfect!
강의에서와 똑같이 풀었다.
"""