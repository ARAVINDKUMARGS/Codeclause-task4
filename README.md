# Codeclause-task4
Artificial intelligence 

Personality Prediction from CV/Resume Analysis

This project analyzes a candidate's resume and predicts personality traits (Extraversion, Agreeableness, Conscientiousness, Openness, Emotional Stability) based on keywords present in the text.


---

How it works

1. The program reads the input file resume.txt.


2. It scans for specific keywords linked to personality traits.


3. It counts the occurrences of these keywords to generate scores for each trait.


4. Results are displayed in the console and saved in task4_output.txt.




---

Requirements

Python 3

No additional libraries required (pure Python).



---

Steps to Run

1. Place your resume text file (resume.txt) in the same folder as the script.


2. Run the script:

python task4_personality.py


3. The predicted personality scores will be shown in the console and saved in task4_output.txt.




---

Example Input (resume.txt)

I am a creative team leader who has experience in planning events, collaborating with peers, and mentoring juniors. I enjoy research and learning new skills.


---

Example Output

Console Output:

Predicted Personality Scores:

Extraversion: 2
Agreeableness: 2
Conscientiousness: 1
Openness: 3
Emotional Stability: 0

task4_output.txt:

Predicted Personality Scores:
Extraversion: 2
Agreeableness: 2
Conscientiousness: 1
Openness: 3
Emotional Stability: 0
