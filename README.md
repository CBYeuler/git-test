# 🎉 Birthday Paradox Simulation

This is a simple Python project that simulates the famous **Birthday Paradox** — the counterintuitive probability that, in a group of just 23 people, there's about a 50% chance that two people share the same birthday.

## 📖 What is the Birthday Paradox?

The Birthday Paradox refers to the surprising probability that in a group of just 23 people, there is a ~50% chance that at least two people will share the same birthday. As the group size increases, the probability of a shared birthday increases rapidly.

This simulation runs multiple experiments to demonstrate this probability in action.

## 🚀 How the Code Works

- **Random Date Generator:**  
  Generates random birthdays for a group of people, using realistic month lengths (January: 31 days, February: 28 days, etc.).

- **Simulation Loop:**  
  Runs the birthday generation process multiple times (default: 1000 simulations), and counts how often at least two people share the same birthday.

- **Result Summary:**  
  After all simulations, prints:
  - Total simulations run
  - Number of times a shared birthday was found
  - Percentage of simulations with at least one shared birthday

## 🛠️ How to Run

1. Clone this repository or download the code.
2. Make sure you have Python installed.
3. Navigate to the project folder.
4. Run the script:
   ```bash
   python birthday_paradox.py
