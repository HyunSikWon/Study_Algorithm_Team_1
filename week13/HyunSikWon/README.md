
# 13주차
이번주에 cpp로 코테를 봐야해서 압축을 제외하고는 cpp로 문제를 풀었습니다.

## 압축
조건에 따라 문제를 풀면 됩니다. 조금 헷갈려서 시간이 좀 걸리긴 했습니다.

## 점프와 순간 이동
최대한 많은 순간 이동을 해야 최소한의 에너지를 사용할 수 있습니다.
순간이동은 (현재까지 온거리)*2 만큼 이동하기 때문에, 역으로 최종 목적지에서 2를 나누어 가는 방식을 통해 결과를 구했습니다. 2로 나누어지지 않는다면 즉, 홀수라면 -1을 하여 짝수를 만들고, 이때는 점프를 한 것이므로 에너지를 소모하게 됩니다.


## 순위
floyd warshall 알고리즘을 통해서 i선수와 j선수의 경기 결과를 구했습니다.
i선수가 k선수를 이기고, k선수가 j 선수를 이겼다면, i 선수는 언제나 j선수를 이깁니다.
반대로 i선수가 k선수에게 지고, j선수가 k 선수를 이긴다면, i선수는 언제나 j선수에게 패배합니다.

이 과정을 거쳤을 때, 모든 선수와 경기를 마친 선수는 순위가 결정됩니다. 
