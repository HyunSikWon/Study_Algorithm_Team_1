def solution(number, k):
    stack = []

    for n in number:
        # k 가 양수이고, 스택이 남아있으며, 스택의 마지막 값이 현재 숫자보다 작다면 반복
        while k > 0 and len(stack) > 0 and int(stack[-1]) < int(n):
            del stack[-1]  # pop
            k -= 1
        stack.append(n)

    # k가 남아있을 경우 뒷 자리를 남은만큼 잘라낸다.
    if k > 0:
        stack = stack[:-k]

    answer = ''.join(stack)
    return answer

# 처음 문제를 접했을 때는 조합으로 풀면 되겠지 해서 그렇게 접근했다.
# k 수 만큼 조합을 뽑아내고, 조합에 해당하는 숫자를 모두 추출해서 최댓값을 구하는 식으로
# 풀이 자체는 유효하나, 시간초과가 났다..
#
# 풀이를 참고한 결과, 숫자의 순서는 어짜피 정해져 있기 때문에, 숫자 첫 번째 부터 스택을 사용하면 될 일이었다.
# 숫자 첫 번째부터 시작하면서, 스택에 push하는데, 이때 맨 마지막 숫자 비교해서 신규 숫자가 더 클 경우에는 pop 연산을 수행한다.
# 이때 감소해야 할 숫자인 k를 하나 감소시킨다.
# 만약 k가 남아있다면, 그 만큼의 분량을 뒤에서부터 잘라낸다.
# 순서가 중요한 문제에서는 그 중요한 순서에 맞는 자료구조를 선택을 고민하는 것이 맞는 것 같다.