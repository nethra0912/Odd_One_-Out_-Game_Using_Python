import random

questions = [
    (["Mercury", "Venus", "Earth", "Pluto"], 4),  # Pluto not a planet
    (["Square", "Rectangle", "Rhombus", "Circle"], 4),  # Circle not quadrilateral
    (["Cheetah", "Leopard", "Tiger", "Cow"], 4),  # Cow herbivore
    (["Copper", "Iron", "Aluminium", "Plastic"], 4),  # Plastic not metal
    (["Python", "Java", "C++", "HTML"], 4),  # HTML not programming language
    (["Rose", "Lotus", "Tulip", "Fern"], 4),  # Fern not flowering plant
    (["January", "February", "March", "Sunday"], 4),  # Sunday not month
    (["Table", "Chair", "Sofa", "Curtain"], 4),  # Curtain not furniture
    (["Red", "Blue", "Green", "Triangle"], 4),  # Triangle not color
    (["Gold", "Silver", "Bronze", "Diamond"], 4),  # Diamond not metal
    (["Shark", "Whale", "Dolphin", "Octopus"], 4),  # Octopus not mammal
    (["Keyboard", "Mouse", "Monitor", "Printer"], 3),  # Monitor is output-only (tricky)
    (["Carrot", "Potato", "Onion", "Apple"], 4),  # Apple fruit others vegetables
    (["Amazon", "Nile", "Ganga", "Pacific"], 4),  # Pacific ocean
    (["Dog", "Cat", "Bat", "Tiger"], 3),  # Bat is flying mammal
]

score = 0

print("🧠 Odd One Out Game")
print("---------------------")

# Shuffle questions for randomness
random.shuffle(questions)

for items, answer in questions:
    # Display options
    for i in range(len(items)):
        print(f"{i+1}. {items[i]}")

    try:
        user = int(input("Enter the odd one out (1-4): "))
    except:
        print("❌ Invalid input!\n")
        continue

    if user == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer was option {answer}\n")

print("🎉 Game Over")
print(f"Your Score: {score} / {len(questions)}")
