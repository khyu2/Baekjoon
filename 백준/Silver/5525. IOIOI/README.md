# [Silver I] IOIOI - 5525 

[문제 링크](https://www.acmicpc.net/problem/5525) 

### 성능 요약

메모리: 113104 KB, 시간: 148 ms

### 분류

문자열

### 제출 일자

2024년 3월 23일 22:28:19

### 문제 설명

<p>1 以上の整数 N に対し，N + 1 個の <code>I</code> と N 個の <code>O</code> を <code>I</code> から始めて交互に並べてできる文字列を P<sub>N</sub> とする．ここで <code>I</code> と <code>O</code> はそれぞれ英大文字のアイとオーである．</p>

<ul>
	<li>P<sub>1</sub> <code>IOI</code></li>
	<li>P<sub>2</sub> <code>IOIOI</code></li>
	<li>P<sub>3</sub> <code>IOIOI</code></li>
	<li>P<sub>N</sub> <code>IOIOI...OI</code> (<code>O</code> が N 個)</li>
</ul>

<p>整数 N と，I と O のみからなる文字列 S が与えられたとき，S の中に P<sub>N</sub> が何ヶ所含まれているかを求めるプログラムを作成せよ．</p>

### 입력 

 <p><span style="line-height:1.6em">標準入力から以下のデータを読み込め．</span></p>

<ul>
	<li>1 行目には整数 N が書かれている．</li>
	<li>2 行目には整数 M が書かれている．これは，入力として与えられる文字列 S の長さが M であることを表す．</li>
	<li>3 行目には長さ M の文字列 S が書かれている．</li>
</ul>

### 출력 

 <p>標準出力に，文字列 S に文字列 P<sub>N</sub> が何ヶ所含まれているかを表す整数を 1 行で出力せよ. もし S に P<sub>N</sub>が含まれていない場合は，0 を出力せよ．</p>

