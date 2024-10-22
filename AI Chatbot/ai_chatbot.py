""" AI Chatbot with Context-Aware Conversations
Data Structures: Queues, Hashmaps, Tries, Linked Lists
Overview: Build a chatbot that can engage in context-aware conversations and remember previous user inputs.
Queues to manage message history in chronological order.
Hashmaps to store user context and frequently asked questions for quick responses.
Tries to implement efficient auto-complete suggestions for user inputs.
Linked Lists to manage dialogue flows with the option to go back and modify previous responses.
Give every good and appipriate code for this very good pss and ask user for input"""

from collections import deque
from typing import Optional


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def search(self, prefix: str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_with_prefix(node, prefix)

    def _find_words_with_prefix(self, node: TrieNode, prefix: str):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._find_words_with_prefix(child_node, prefix + char))
        return words


# Linked list


class Node:
    def __init__(self, message: str):
        self.message = message
        self.next = None


class DialogueLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_mess(self, message: str):
        new_node = Node(message)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.message)
            curr = curr.next


class AIChatbot:
    def __init__(self):
        self.message_history = deque(maxlen=5)
        self.user_context = {}
        self.trie = Trie()  # Trie for auto-complete suggestions
        self.dialogue_flow = DialogueLL()  # Linked List for dialogue management

    def set_user_context(self, key: str, value: str):
        self.user_context[key] = value

    def get_user_context(self, key: str) -> Optional[str]:
        return self.user_context.get(key, "No context found.")

    def add_message(self, message: str):
        self.message_history.append(message)
        self.dialogue_flow.add_mess(message)

    def suggest_auto_complete(self, prefix: str):
        return self.trie.search(prefix)

    def remember_frequently_asked(self, word: str):
        self.trie.insert(word)

    def show_dialogue_flow(self):
        self.dialogue_flow.traverse()

    def chat(self):
        print("Hello! I'm your AI chatbot. How can I assist you today?")
        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            # Handle specific responses based on user context
            if "name" in self.user_context:
                print(f"Chatbot: Nice to meet you, {self.user_context['name']}!")
            else:
                self.set_user_context("name", user_input)
                print(f"Chatbot: Hi {user_input}! What can I do for you today?")

            # Add message to history and dialogue flow
            self.add_message(user_input)

            # Suggest auto-complete for the next input if the user types "how"
            if user_input.lower().startswith("how"):
                suggestions = self.suggest_auto_complete(user_input.lower())
                if suggestions:
                    print(f"Chatbot: Did you mean: {', '.join(suggestions)}?")
                else:
                    print("Chatbot: I'm not sure. Could you clarify?")

            # Remember the user's frequent phrases or important inputs
            self.remember_frequently_asked(user_input.lower())


# Example Usage
if __name__ == "__main__":
    chatbot = AIChatbot()
    chatbot.chat()
