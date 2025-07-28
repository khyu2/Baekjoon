# [Silver V] 줄세우기 - 10431 

[문제 링크](https://www.acmicpc.net/problem/10431) 

### 성능 요약

메모리: 111484 KB, 시간: 116 ms

### 분류

구현, 정렬, 시뮬레이션

### 제출 일자

2025년 7월 28일 23:09:30

### 문제 설명

<p>Mrs. Chambers always has her class line up in height order (shortest at the front of the line). Every September a new class of exactly 20 3rd graders arrive, all of different height. For the first few days it takes a long time to get the kids in height order, since no one knows where they should be in the line. Needless to say, there is quite a bit of jockeying around. This year Mrs. Chambers decided to try a new method to minimize this ordering chaos. One student would be selected to be the first person in line. Then, another student is selected and would find the first person in the line that is taller than him, and stand in front of that person, thereby causing all the students behind him to step back to make room. If there is no student that is taller, then he would stand at the end of the line. This process continues, one student at-a-time, until all the students are in line, at which point the students will be lined up in height order.</p>

<p>For this problem, you will write a program that calculates the total number of steps taken back during the ordering process for a given class of students.</p>

### 입력 

 <p>The first line of input contains a single integer P, (1 ≤ P ≤ 1000), which is the number of data sets that follow. Each data set should be processed identically and independently.</p>

<p>Each data set consists of a single line of input. It contains the data set number, K, followed by 20 non-negative unique integers separated by a single space. The 20 integers represent the height (in millimeters) of each student in the class.</p>

### 출력 

 <p>For each data set there is one line of output. The single output line consists of the data set number, K, followed by a single space followed by total number of steps taken back.</p>

