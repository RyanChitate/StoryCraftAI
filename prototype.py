import streamlit as st
import random
import time

def simple_ai(response_type):
    if response_type == "positive":
        return random.choice(["Well done!", "Great choice!", "You're on the right track!"])
    elif response_type == "negative":
        return random.choice(["Uh-oh, that might be risky.", "Be cautious!", "Consider other options."])

def ascii_art(encounter):
    if encounter == "a hidden cave":
        return """
                    _______
              _    |\\      \\
             / \\   |  \\      \\
            //\\ \\  |    \\_____\\_____________
           ||  \\ \\ |   /    /             \\
           | \\  |\\ \\_/____/        (  )    |
           | |  | \\___,||____,    ( /\\ /\\   |
           | |   \\    ||       \\   \\_||_\\_|
           | |    \\   ||        \\
           | |     \\  ||         \\
           | |      \\ ||          |
           | |______/ ||__________|
           | |_________|_________|
           |_|__________________|
        """

    elif encounter == "a stream with fresh water":
        return """
                    _________________
          _______/                 \\_______
         |                                 |
         |                                 |
         |                                 |
         |                                 |
         |____________    ________________|
                       \\  /
                        \\/
        """

    elif encounter == "animal tracks":
        return """
                    __
              (\\,--------'
              /  \\_
          _/     /
         /      /
        (      /
        \\     /
         \\_  (
           |\\  \\
           | |  \\
           | |   )
           (_/   )
                 /
                /
               /
        """

def game_screen(text, delay=2):
    container = st.empty()
    container.write(text)
    time.sleep(delay)

def survive_wilderness(user_name, ai_name):
    st.title("Survival Adventure Game")
    st.subheader(f"Welcome, {user_name}, to the Survival Adventure!")

    game_screen(f"You and your AI companion, {ai_name}, find yourselves stranded in a dense and mysterious wilderness after a plane crash.")

    decision = st.radio("What's your first move?", ["Explore the surroundings", "Build a shelter", "Look for food"])
    ai_response = simple_ai("positive" if random.random() < 0.7 else "negative")
    game_screen(f"{ai_name}: {ai_response}")

    if decision == "Explore the surroundings":
        game_screen("As you explore, you discover...")
        encounter = random.choice(["a hidden cave", "a stream with fresh water", "animal tracks"])
        game_screen(ascii_art(encounter))
        game_screen(f"You and {ai_name} find {encounter}.")

        decision_explore = st.radio("What do you do?", ["Enter the cave", "Follow the stream", "Examine the animal tracks"])
        ai_response = simple_ai("positive" if random.random() < 0.7 else "negative")
        game_screen(f"{ai_name}: {ai_response}")

        if decision_explore == "Enter the cave":
            game_screen("Inside the cave, you find...")
            # Add more storytelling elements and choices
        elif decision_explore == "Follow the stream":
            game_screen("Following the stream leads you to...")
            # Add more storytelling elements and choices
        elif decision_explore == "Examine the animal tracks":
            game_screen("The tracks belong to...")
            # Add more storytelling elements and choices

    elif decision == "Build a shelter":
        game_screen("While building your shelter, you encounter...")
        obstacle = random.choice(["heavy rain", "wild animals", "limited resources"])
        game_screen(f"You and {ai_name} must overcome the obstacle of {obstacle}.")

        decision_shelter = st.radio("What's your strategy?", ["Build a rainproof roof", "Set up traps for animals", "Search for more resources"])
        ai_response = simple_ai("positive" if random.random() < 0.7 else "negative")
        game_screen(f"{ai_name}: {ai_response}")

        if decision_shelter == "Build a rainproof roof":
            game_screen("With a rainproof roof, you...")
            # Add more storytelling elements and choices
        elif decision_shelter == "Set up traps for animals":
            game_screen("Setting up traps, you catch...")
            # Add more storytelling elements and choices
        elif decision_shelter == "Search for more resources":
            game_screen("While searching, you find...")
            # Add more storytelling elements and choices

    elif decision == "Look for food":
        game_screen("In your quest for food, you come across...")
        food_source = random.choice(["wild berries", "a small game", "edible plants"])
        game_screen(ascii_art(food_source))
        game_screen(f"You and {ai_name} find {food_source}.")

        decision_food = st.radio("What's your approach?", ["Eat the wild berries", "Hunt the small game", "Harvest the edible plants"])
        ai_response = simple_ai("positive" if random.random() < 0.7 else "negative")
        game_screen(f"{ai_name}: {ai_response}")

        if decision_food == "Eat the wild berries":
            game_screen("Eating the wild berries, you...")
            # Add more storytelling elements and choices
        elif decision_food == "Hunt the small game":
            game_screen("Hunting the small game, you catch...")
            # Add more storytelling elements and choices
        elif decision_food == "Harvest the edible plants":
            game_screen("Harvesting the edible plants, you...")
            # Add more storytelling elements and choices

def main():
    st.set_page_config(page_title="Survival Adventure", page_icon=":evergreen_tree:")
    st.title("Survival Adventure Game")

    user_name = st.text_input("Enter your name:")
    ai_name = "SurvivorBot"  # You can customize the AI's name

    if not user_name:
        st.warning("Please enter your name.")
        st.stop()

    if st.button("Start Adventure"):
        survive_wilderness(user_name, ai_name)

if __name__ == "__main__":
    main()
