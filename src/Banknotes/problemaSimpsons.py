import csv
import random

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

with open("simpsonData.csv") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"evidence":[float(cell) for cell in row[1:4]], "label": "H" if row[4] == "1" else "M"})
    
# Separate data into training and testing groups
holdout = int(0.20 * len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[holdout:]

# Train model on training set
X_training = [row["evidence"] for row in training]
y_training = [row["label"] for row in training]
model.fit(X_training, y_training)

# Make predictions on the testing set
X_testing = [row["evidence"] for row in testing]
y_testing = [row["label"] for row in testing]
predictions = model.predict(X_testing)

# Compute how well we performed
correct = 0
incorrect = 0
total = 0
for actual, predicted in zip(y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
    else:
        incorrect += 1

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")

predictions = model.predict([[8.0,290.0,38.0]])
print("Resultado de prediccion para Comic: {}".format(predictions[0]))