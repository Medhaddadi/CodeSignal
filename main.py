def solution(inputString):
    n=inputString.count('(')
    for i in range(n):
        fist = inputString.rfind('(')
        rest = inputString[fist + 1:]
        secand = rest.index(')')
        x = inputString[fist + 1:secand + fist + 1]
        revWord = x[::-1]
        x = '(' + x + ')'
        inputString = inputString.replace(x, revWord)
    return inputString


print(solution("foo(bar)baz(blim)"))
