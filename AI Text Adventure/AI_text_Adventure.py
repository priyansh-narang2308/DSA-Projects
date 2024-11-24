""" AI-Powered Text Adventure Game
Concept: Create a text-based game where the user interacts with an AI-powered storyline. Use trees to represent the decision paths and graphs for connecting locations.
Story progression using decision trees.
Dynamic responses generated using AI or predefined rules.
Inventory managed via stacks or queues.
Unique Factor: Combines AI and DSA for immersive storytelling."""

# Uses Trees,Stacks and Queues

import random  # used to put AI also


class Node:
    def __init__(self, story, left=None, right=None):  # To represent Decisions
        self.story = story
        self.left = left
        self.right = right


class TextAdventureGame:
    def __init__(self):
        self.inventory = []
        self.curr_node = self.create_story_tree()
        self.AI_responses = [
            "That's an interesting choice!",
            "Your bravery is unmatched.",
            "This decision will shape your destiny.",
            "A wise move, but is it enough?",
        ]

    def create_story_tree(self):
        left_leaf = Node("You found the treasure! The adventure ends Here!!")
        right_leaf = Node("You fell into a trap ! Game Over!!")

        # Middle Lead
        second_level_left = Node(
            "You entered a Dark Forest. Do u want to go left or right? ",
            left_leaf,
            right_leaf,
        )

        second_level_right = Node(
            "You reached a river. Do u swim across or walk along the bank? ",
            left_leaf,
            right_leaf,
        )

        root = Node(
            "You are at the start of the advneture. U want to go into the forest or follow the river? ",
            second_level_left,
            second_level_right,
        )

        return root

    def play(self):
        print("Welcome to the AI-Powered Text Adventure Game! ")
        while self.curr_node:
            print("\n" + self.curr_node.story)
            if not self.curr_node.left and not self.curr_node.right:
                print("The Game has Ended ! \n Thanks for Playing with Us!")
                break

            choice = input("Enter 'left' or 'right' : ").strip().lower()
            ai_feedback = self.get_AI_response()
            print("AI: ", ai_feedback)

            if choice == "left":
                self.curr_node = self.curr_node.left
                self.add_to_inventory("Map Piece")
            if choice == "right":
                self.curr_node = self.curr_node.right
                self.add_to_inventory("Magic Stone")
            else:
                print("Invalid Choice ! Try Again! ")

        self.show_inventory()

    def get_AI_response(self):
        return random.choice(self.AI_responses)  # Generating random choices

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print("You found a ", item, "! Its added to ur inventory.")

    def show_inventory(self):
        print("Your Inventory: ")
        while self.inventory:
            print(f"- {self.inventory.pop()}")


if __name__ == "__main__":
    game = TextAdventureGame()
    game.play()
