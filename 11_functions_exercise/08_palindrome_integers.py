user_input = list(input().split(", "))


def is_palindrome(n):
    return n == n[::-1]


for b in user_input:
    ans = is_palindrome(b)
    if ans:
        print("True")
    else:
        print("False")
