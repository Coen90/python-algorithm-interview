# 팰린드롬(Palindrome) 이란 앞으로 읽어도 거꾸로 읽어도 같은 말이 되는 단어 또는 문장이라고 한다. 우영우, 역삼역, 소주 만 병만 주소 등
import re
from typing import Deque
from collections import deque

palindrome = "A man, a plan, a canal: Panama"
palindrome_kor = "소주 만 병만 주소"
not_palindrome = "Apple piel ppl"
not_palindrome_kor = "우영원"

# 풀이1 - list로 변환
print("list로 변환한 풀이")
def isPalindromeList(s: str) -> bool:
    strs = []

    print("method name: isPalindromeList, testing string: ", s)

    for char in s:
        if char.isalpha(): # isalpha() - 영어, 한글일 경우 True, isalnum() - 영어, 한글, 숫자일 경우 True
            strs.append(char.lower())

    print(strs) # ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']
    while len(strs) > 1:
        if strs.pop() != strs.pop(0):
            return False

    return True


print(isPalindromeList(palindrome))
print(isPalindromeList(palindrome_kor))
print(isPalindromeList(not_palindrome))
print(isPalindromeList(not_palindrome_kor))

# 풀이2 - Deque 자료형을 이용한 최적화
print("Deque를 사용한 풀이")
def isPalindromeDeque(s: str) -> bool:
    # Deque 자료형 선언
    strs: Deque = deque()

    print("method name: isPalindromeDeque, testing string: ", s, "\nresult:", end=' ')

    for char in s:
        if char.isalpha():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


print(isPalindromeDeque(palindrome))
print(isPalindromeDeque(palindrome_kor))
print(isPalindromeDeque(not_palindrome))
print(isPalindromeDeque(not_palindrome_kor))


# 풀이3 list slicing 을 이용
print()
print()
print("list slicing 을 사용한 풀이")
def isPalindromeListSlicing(s: str) -> bool:
    print("method name: isPalindromeListSlicing, testing string: ", s, "\nreverse:", end=' ')

    s = s.lower()

    # 정규식으로 불필요한 문자 필터링
    s = re.sub("[^a-z0-9가-힣]", "", s)

    print(s[::1])
    return s == s[::-1]


print(isPalindromeListSlicing(palindrome))
print(isPalindromeListSlicing(palindrome_kor))
print(isPalindromeListSlicing(not_palindrome))
print(isPalindromeListSlicing(not_palindrome_kor))