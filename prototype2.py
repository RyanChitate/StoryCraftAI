import streamlit as st

def survival_story():
    st.title("Interactive Survival Story")
    st.markdown("---")
    name = st.text_input("What's your name?")
    st.write(f"Hello, {name}!")

    st.markdown("---")
    st.write("You wake up in a dense and mysterious forest. The air is thick with an eerie silence. What do you want to do?")

    options = ["Explore deeper into the forest", "Build a shelter", "Find food"]
    choice = st.radio("Choose your action:", options)

    st.markdown("---")

    if choice == options[0]:
        st.write("As you venture deeper into the forest, you come across an ancient temple.")
        st.write("A) Enter the temple")
        st.write("B) Ignore the temple and keep exploring")
        explore_choice = st.radio("Choose your next action:", ["A", "B"])
        if explore_choice == "A":
            st.write("Inside the temple, you find a hidden treasure and a magical portal. Do you:")
            st.write("A) Take the treasure and use the portal to escape")
            st.write("B) Leave the treasure and continue exploring the forest")
            temple_choice = st.radio("Choose your next action:", ["A", "B"])
            if temple_choice == "A":
                st.write("Congratulations! You escaped the forest with the treasure. You survived!")
            else:
                st.write("You decide to leave the treasure and continue exploring. Suddenly, the temple starts collapsing. You narrowly escape. Unfortunately, you did not survive.")
        else:
            st.write("You continue exploring the forest and encounter a pack of wolves. Do you:")
            st.write("A) Try to scare the wolves away")
            st.write("B) Climb a tree to escape")
            wolf_choice = st.radio("Choose your next action:", ["A", "B"])
            if wolf_choice == "A":
                st.write("Your attempt to scare the wolves succeeds, and they run away. You survived!")
            else:
                st.write("Climbing the tree, you escape the wolves, but you get stuck. Suddenly, a mysterious figure helps you down. Congratulations, you survived!")

    elif choice == options[1]:
        st.write("You decide to build a shelter. Do you want to:")
        st.write("A) Build a treehouse")
        st.write("B) Dig an underground bunker")
        shelter_choice = st.radio("Choose your shelter type:", ["A", "B"])
        if shelter_choice == "A":
            st.write("Your treehouse provides a safe haven. One night, you discover glowing mushrooms that heal wounds. Congratulations, you survived!")
        else:
            st.write("The underground bunker protects you from the elements, but it collapses. As you search for an exit, you find a hidden passage leading to safety. Congratulations, you survived.")

    elif choice == options[2]:
        st.write("You try to find food. Do you want to:")
        st.write("A) Hunt for animals")
        st.write("B) Gather fruits and berries")
        food_choice = st.radio("Choose your food source:", ["A", "B"])
        if food_choice == "A":
            st.write("You successfully hunt and gather enough food to survive. One day, you encounter a wounded animal. Do you:")
            st.write("A) Help the wounded animal")
            st.write("B) Leave the wounded animal and continue hunting")
            wounded_animal_choice = st.radio("Choose your next action:", ["A", "B"])
            if wounded_animal_choice == "A":
                st.write("You help the wounded animal and gain a loyal companion. Congratulations, you survived!")
            else:
                st.write("Leaving the wounded animal, you continue hunting. Suddenly, a group of friendly travelers appears. Together, you form an alliance and survive!")

        else:
            st.write("While gathering, you discover a mysterious cave. Do you:")
            st.write("A) Enter the cave")
            st.write("B) Ignore the cave and keep gathering")
            cave_choice = st.radio("Choose your next action:", ["A", "B"])
            if cave_choice == "A":
                st.write("Inside the cave, you find a hidden oasis with abundant resources. Suddenly, a secret door leads to a shortcut out of the forest. Congratulations, you survived!")
            else:
                st.write("You decide to ignore the cave and keep gathering. As night falls, you hear strange sounds. Do you:")
                st.write("A) Investigate the sounds")
                st.write("B) Stay hidden and observe")
                night_sounds_choice = st.radio("Choose your next action:", ["A", "B"])
                if night_sounds_choice == "A":
                    st.write("Investigating, you discover a group of mystical beings having a celebration. They invite you to join, and you gain their protection. Congratulations, you survived!")
                else:
                    st.write("Staying hidden, you observe a dangerous predator passing by. It doesn't notice you. Congratulations, you survived!")

    st.markdown("---")
    st.write("The night falls, and you hear strange sounds in the distance. What do you want to do?")
    night_options = ["Stay in your shelter", "Build a fire", "Explore the night"]
    night_choice = st.radio("Choose your action:", night_options)

    st.markdown("---")

    if night_choice == night_options[0]:
        st.write("You stay in your shelter and hear footsteps. Do you:")
        st.write("A) Hide quietly")
        st.write("B) Confront the source of the footsteps")
        hide_choice = st.radio("Choose your next action:", ["A", "B"])
        if hide_choice == "A":
            st.write("The footsteps pass by, and you remain hidden. Suddenly, you overhear a secret conversation. You gain valuable information. Congratulations, you survived the night!")
        else:
            st.write("Confronting the source, you find a lost traveler. Together, you face the challenges and survive!")

    elif night_choice == night_options[1]:
        st.write("You build a fire, and the warmth keeps you safe. One night, the flames reveal a hidden path. Following it, you discover a shortcut out of the forest. Congratulations, you survived the night!")

    elif night_choice == night_options[2]:
        st.write("You decide to explore the night and come across a mysterious ritual. Do you:")
        st.write("A) Join the ritual")
        st.write("B) Watch from a distance")
        ritual_choice = st.radio("Choose your next action:", ["A", "B"])
        if ritual_choice == "A":
            st.write("Joining the ritual, you gain the favor of mystical beings. Suddenly, you're granted the ability to communicate with animals. Congratulations, you survived the night!")
        else:
            st.write("Watching from a distance, you remain unnoticed. Suddenly, the ritual reveals a hidden passage. Following it, you find safety. Congratulations, you survived the night!")

def main():
    survival_story()

if __name__ == "__main__":
    main()
