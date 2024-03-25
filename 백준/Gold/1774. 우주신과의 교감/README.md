# [Gold III] 우주신과의 교감 - 1774 

[문제 링크](https://www.acmicpc.net/problem/1774) 

### 성능 요약

메모리: 239680 KB, 시간: 3552 ms

### 분류

그래프 이론, 최소 스패닝 트리

### 제출 일자

2024년 3월 25일 12:54:08

### 문제 설명

<p>Farmer John had just acquired several new farms! He wants to connect the farms with roads so that he can travel from any farm to any other farm via a sequence of roads; roads already connect some of the farms.</p>

<p>Each of the N (1 <= N <= 1,000) farms (conveniently numbered 1..N) is represented by a position (X_i, Y_i) on the plane (0 <= X_i <= 1,000,000; 0 <= Y_i <= 1,000,000).  Given the preexisting M roads (1 <= M <= 1,000) as pairs of connected farms, help Farmer John determine the smallest length of additional roads he must build to connect all his farms.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and M</li>
	<li>Lines 2..N+1: Two space-separated integers: X_i and Y_i</li>
	<li>Lines N+2..N+M+2: Two space-separated integers: i and j, indicating that there is already a road connecting the farm i and farm j.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: Smallest length of additional roads required to connect all farms, printed rounding to two decimal places. Be sure to calculate distances as 64-bit floating point numbers.</li>
</ul>

