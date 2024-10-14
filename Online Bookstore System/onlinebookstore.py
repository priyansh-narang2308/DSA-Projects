''' Online Bookstore System using Linked lists, Hashmaps, Trees, Stacks
online bookstore platform where customers can browse, purchase, and review books. 
Linked List to manage books in a category.
Hashmaps for fast access to user information.
Trees ( BST) to maintain book categories sorted by name or author.
Stacks for the undo feature '''

#lInked List
class BookNode:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        self.next=None
        
class BookLinkedLst:
    def __init__(self):
        self.head=None
        
    #Add book to the end
    def add_book(self,title,author,price):
        new_book=BookNode(title,author,price)
        if not self.head:
            self.head=new_book
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_book
    
    def remove_book(self,title):
        curr=self.head
        prev=None
        while curr:
            if curr.title==title:
                if prev:
                    prev.next=curr.next
                else:
                    self.head=curr.next
                return True
            prev=curr
            curr=curr.next
        return False

    def display_books(self):
        curr=self.head
        if not curr:
            print("No books Available!")
            return
        while curr:
            print("Title: " , curr.title , "Author: " , curr.author , "Price: " , curr.price)
            curr=curr.next
            
#BST         
class CategoryNode:
    def __init__(self,category_name):
        self.category_name=category_name
        self.books=BookLinkedLst()
        self.left=None    
        self.right=None  
    
class CategroyBST:
    def __init__(self):
        self.root=None
        
    def insert_category(self,category_name):
        if not self.root:
            self.root=CategoryNode(category_name)
        else:
            self._insert(self.root,category_name)
    
    def _insert(self,node,category_name):
        if category_name<node.category_name:
            if not node.left:
                node.left=CategoryNode(category_name)  
            else:
                self._insert(node.left,category_name)
        elif category_name>node.category_name:
            if not node.right:
                node.right=CategoryNode(category_name)  
            else:
                self._insert(node.right,category_name)
                
    def search_category(self,category_name):
        return self._search(self.root,category_name)    
    
    def _search(self,node,category_name):
        if not node:
            return None
        if category_name==node.category_name:
            return node
        if category_name<node.category_name:
            return self._search(node.left,category_name)
        else:
            return self._search(node.right,category_name)
        
    def display_cats(self):
        self._inorder(self.root)
        
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print("Category: " , node.category_name)
            node.books.display_books()
            self._inorder(node.right)
            
#hashMap to store user information
class UserHashMap:
    def __init__(self):
        self.users={}
        
    def add_user(self,username,info):
        self.users[username]=info
        
    def get_user(self,username):
        return self.users.get(username)
    
    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
        else:
            print("User" , {username} , "not found")
            
            

#stack for the undo feature 
class ActionStack:
    def __init__(self):
        self.stack = []

    def push_action(self, action):
        self.stack.append(action)

    def pop_action(self):
        if self.stack:
            return self.stack.pop()
        return None
    

#MAIN
class OnlineBookstoreSystem:
    def __init__(self):
        self.categories =CategroyBST()
        self.users = UserHashMap()
        self.undo_stack = ActionStack()
        
    def add_book(self,category_name,title,author,price):
        category=self.categories.search_category(category_name)
        if not category:
            self.categories.insert_category(category_name)
            category = self.categories.search_category(category_name)
        category.books.add_book(title, author, price)
        self.undo_stack.push_action(f"remove:{category_name}:{title}")
        print(f"Book '{title}' added to category '{category_name}'.")
        
        
    def remove_book(self, category_name, title):
        category = self.categories.search_category(category_name)
        if category and category.books.remove_book(title):
            self.undo_stack.push_action(f"add:{category_name}:{title}")
            print(f"Book '{title}' removed from category '{category_name}'.")
        else:
            print(f"Book '{title}' not found in category '{category_name}'.")
            
            
    def undo_last_action(self):
        action = self.undo_stack.pop_action()
        if action:
            action_type, category_name, title = action.split(":")
            if action_type == "add":
                self.add_book(category_name, title, "Unknown", 0)
            elif action_type == "remove":
                self.remove_book(category_name, title)
        else:
            print("No actions to undo.")
            
            
    def display_all_books(self):
        self.categories.display_cats()

    # Add a new user
    def add_user(self, username, info):
        self.users.add_user(username, info)

    # Get user information
    def get_user_info(self, username):
        return self.users.get_user(username)

    
            
            
def menu():
    store = OnlineBookstoreSystem()

    while True:
        print("\n--- Online Bookstore  ---")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Undo last action")
        print("4. Display all books")
        print("5. Add user")
        print("6. Get user information")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category_name = input("Enter category name: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            store.add_book(category_name, title, author, price)

        elif choice == '2':
            category_name = input("Enter category name: ")
            title = input("Enter book title to remove: ")
            store.remove_book(category_name, title)

        elif choice == '3':
            store.undo_last_action()

        elif choice == '4':
            store.display_all_books()

        elif choice == '5':
            username = input("Enter username: ")
            info = input("Enter user info: ")
            store.add_user(username, info)

        elif choice == '6':
            username = input("Enter username to fetch info: ")
            info = store.get_user_info(username)
            if info:
                print(f"User info: {info}")
            else:
                print(f"User '{username}' not found.")

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please try again.")


menu()
                
        
