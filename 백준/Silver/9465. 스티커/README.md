# [Silver I] 스티커 - 9465 

[문제 링크](https://www.acmicpc.net/problem/9465) 

### 성능 요약

메모리: 50068 KB, 시간: 900 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 3월 4일 13:56:38

### 문제 설명

<p>Nancy, your little sister, has a sheet of 2n stickers of rectangular shape that are arranged in 2 rows and n columns. See Figure 1(a). Nancy wants to decorate her desk with the stickers. But the quality of the stickers is poor, and tearing off one sticker from the sheet spoils the stickers sharing an edge with it. So, Nancy must lose the stickers above, below, to the left of, and to the right of the sticker she tears off. </p>

<p><img alt="" src="https://www.acmicpc.net/upload/images/sticker.png" style="height:150px; width:575px"></p>

<p>Figure 1. A sheet of 10 stickers in 2 rows </p>

<p>Nancy had no idea about what to do. You looked at her and suggested that she should score each sticker and try to choose a possible set of stickers that maximizes the total score. Nancy marked scores to all the 2n stickers as in Figure 1(b). And Nancy had no idea, again. You again took a look at her and sighed. You cannot help doing something for her, and at last decided to help her with a fast computer program. Your program is to select a set of stickers of maximum total score from the 2n stickers such that no two of them share an edge.</p>

<p>In the example shown in Figure 1, the maximum total score is 260 when you select the four stickers of scores 50, 50, 100, 60. Unfortunately, in this case, it is not allowed to simultaneously select both of the two highest scored stickers (of score 100 and 70) because the two stickers share an edge between them. </p>

### 입력 

 <p>Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case starts with a line that contains an integer (1 ≤ n ≤ 100,000), where 2n is the number of stickers in the sheet. In the next two lines, each line contains n integers, each of which represents Nancy’s score for the sticker at that position in the sticker sheet. Every two consecutive integers in a line are separated by a blank. Note that the 2n stickers are of rectangular shape and are arranged in 2 rows and n columns in the sheet. Nancy’s scores range from 0 to 100. </p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line for each test case. The line should contain the maximum possible total score for a subset of the 2n stickers such that no two stickers share an edge. </p>

<p> </p>

