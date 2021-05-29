# 12주차

## 게임 맵 최단 거리
BFS를 사용해 푼 문제입니다. 이동 거리가 모두 1로 같기 때문에 먼저 방문한 곳이 최단 거리가 됩니다.
cpp은 오랜만에 사용하는데 사용하는 자료구조에 따라 시간 초과가 뜨기도 하네요ㅠㅠ 이 부분은 더 공부해야 할 것 같습니다.

## 다음 큰 숫자
간단한 문제고 AND 연산을 사용해 2진수의 1의 개수를 구했습니다.
이 방식은 이번에 처음 알게 되었네요.... 덕분에 쉽게 풀 수 있었습니다.

## 단속카메라
방법이 쉽게 떠오르지 않아 질문하기를 참고하여 문제를 풀었습니다.
차가 고속도로에서 빠져나가는 시점을 고려하는 것이 포인트인 것 같습니다.
고속도로를 빠져 나가는 순으로 routes 배열을 정렬한 뒤 나간 시점에 카메라가 잡을 수 있는 차들을 bool 배열을 사용하여 기록해두었습니다.