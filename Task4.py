# Task 4 – Personality Prediction from CV Analysis
# This program analyzes resume text and predicts personality traits based on keywords.

# Open the resume text file
try:
    with open("resume.txt", "r") as f:
        text = f.read().lower()
except FileNotFoundError:
    print("Error: resume.txt not found. Please place it in the same folder.")
    exit()

# Keywords linked to Big Five personality traits
traits_keywords = {
    "Extraversion": ["team", "leader", "presentation", "networking", "communicate"],
    "Agreeableness": ["help", "support", "collaborate", "volunteer", "mentor"],
    "Conscientiousness": ["plan", "organize", "detail", "document", "deadline"],
    "Openness": ["creative", "innovate", "research", "design", "learn"],
    "Emotional Stability": ["resilient", "calm", "stress", "balanced", "adapt"]
}

# Count occurrences for each trait
trait_scores = {}
for trait, keywords in traits_keywords.items():
    score = sum(text.count(word) for word in keywords)
    trait_scores[trait] = score

# Display results
print("Predicted Personality Scores:\n")
for trait, score in trait_scores.items():
    print(f"{trait}: {score}")

# Save results to file
with open("task4_output.txt", "w") as out:
    out.write("Predicted Personality Scores:\n")
    for trait, score in trait_scores.items():
        out.write(f"{trait}: {score}\n")
