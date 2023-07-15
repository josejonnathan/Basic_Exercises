# Bulls and Cows

## Overview

write a 4-digit secret number. The digits must be all different. Then try to guess their computers number who gives the number of matches. The digits of the number guessed also must all be different. If the matching digits are in their right positions, they are "Bulls", if in different positions, they are "Cows".

### Example

```
Secret number: 4271
Opponent's try: 1234
Answer: 2 Cows and 1 Bull. (The Bull is "2", the Cows are "4" and "1".)
```

## Task

Write a program that generates a random 4 digit number with no repeats and compare it to the prompted, then provide the feedback of Cows and Bulls according to the rules

### Exmaple of the output

```
*** Welcome to Bulls and Cows ***
you will guess a 4 digit number with no repeats, every guessed number in the right position is a 'bull' and every guessed number in the wrong position is a 'cow'. Good luck!!!
Give me your number: 1234
1 Cows, 0 Bulls
Give me your number: 5678
2 Cows, 0 Bulls
Give me your number: 4568
2 Cows, 0 Bulls
Give me your number: 1698
3 Cows, 0 Bulls
Give me your number: 1686
4 Cows, 0 Bulls
Give me your number: 8016
0 Cows, 4 Bulls
You wonn and took 6 tries
```
