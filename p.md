# Student Score Calculator

---

## Description
This Python program calculates a student's final score based on three different evaluation areas: emotional skills, English, and development.  
Each score must be entered by the user with a value between **0 and 100**, and the program validates the input to ensure it is within the allowed range.

The program then applies a weighted calculation to determine the final score and displays the student's performance level.

---

## Features
- User input validation
- Screen cleaning for a better console experience
- Weighted score calculation
- Final evaluation message

---

## Score Weights
The final score is calculated using the following weights:

| Category | Weight |
|--------|--------|
| Emotional Skills | 20% |
| English | 20% |
| Development | 60% |

---

## How It Works
1. The program asks the user to enter their score in:
   - Emotional skills
   - English
   - Development
2. Each value must be between **0 and 100**.
3. If the user enters an invalid value, the program shows an error message and asks for the score again.
4. The program calculates the weighted final score.
5. Finally, it displays the performance result.

---

## Result Categories
- **Excellent** – High final score and successful approval.
- **Good** – Acceptable score and approved.
- **Regular** – Low score and not approved.

---

## Requirements
- Python 3.x

---

## Example
Example interaction:

```
Enter your emotional skills score (0-100):
80

Enter your English score (0-100):
75

Enter your development score (0-100):
90

Output:
Your final score is: EXCELLENT 87 and you have successfully passed.
```