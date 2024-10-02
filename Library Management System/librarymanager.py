#Library Management System using LinkedList,Queues,and Trees


#For managing borrowers.
class Queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,item):
        self.queue.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    

#To represent indivisual bookks

class Book:
    def __init__(self,title,author,category):
        self.title=title
        self.author=author
        self.category=category
        self.is_available=True
        self.borrowers_queue=Queue()   #Users weight for books right thats why
        
    def __str__(self):
        status="Available" if self.is_available else "Not Available"
        return "Title: " , self.title , "Author: " , self.author , "Category: " , self.category ,  "Status: " , status
    

class BookNode:
    def __init__(self,book):
        self.book=book
        self.left=None
        self.right=None
        
class BookBST:
    def __init__(self):
        self.root=None
        
    def insert(self,book):
        if self.root is None:
            self.root=BookNode(book)
        else:
            self._insert(self.root,book)
            
    def _insert(self,node,book):
        if book.title<node.book.title:
            if node.left is None:
                node.left=BookNode(book)
            else:
                self._insert(node.left,book)
        elif book.title>node.book.title:
            if node.right is None:
                node.right=BookNode(book)
            else:
                self._insert(node.right,book)
                
    def search(self,title):
        return self._search(self.root,title)

    def _search(self,node,title):
        if node is None or node.book.title==title:
            return node
        elif title<node.book.title:
            return self._search(node.left,title)
        elif title>node.book.title:
            return self._search(node.right,title)
        
    def delete(self,title):
        self.root,_=self._delete(self.root,title)
        
    def _delete(self,node,title):
        if node is None:
            return node, None

        if title < node.book.title:
            node.left, deleted_node = self._delete(node.left, title)
        elif title > node.book.title:
            node.right, deleted_node = self._delete(node.right, title)
        else:
            deleted_node = node
            # Node with only one child or no child
            if node.left is None:
                return node.right, deleted_node
            elif node.right is None:
                return node.left, deleted_node

            min_larger_node = self._min_value_node(node.right)
            node.book = min_larger_node.book
            node.right, _ = self._delete(node.right, min_larger_node.book.title)

        return node, deleted_node
        
    def _min_value_node(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr
    
    def inorder_trav(self):
        books=[]
        self._inorder_travs(self.root,books)
        return books
    
    def _inorder_travs(self,node,books):
        if node:
            self._inorder_travs(node.left,books)
            books.append(node.book)
            self._inorder_travs(node.right,books)
            
            
class CategorynODE:
    def __init__(self, category_name):
        self.category_name = category_name
        self.books = []  # List of books under this category
        self.subcategories = []
        
class CategroyManag:
    def __init__(self):
        self.categories={}
        
    def add_category(self,category_name):
        if category_name not in self.categories:
            self.categories[category_name] = CategorynODE(category_name)
            print("Category : " , category_name ,"added")
        else:
            print("Category: " , category_name , "already exists.")
            
    def add_book_to_category(self, book):
        category_name = book.category
        if category_name not in self.categories:
            self.add_category(category_name)
        self.categories[category_name].books.append(book)
        print(f"Book '{book.title}' added to category '{category_name}'.")
        
        
    def remove_book_from_category(self, title, category_name):
        if category_name in self.categories:
            category_node = self.categories[category_name]
            for book in category_node.books:
                if book.title == title:
                    category_node.books.remove(book)
                    print(f"Book '{title}' removed from category '{category_name}'.")
                    return
            print(f"Book '{title}' not found in category '{category_name}'.")
        else:
            print(f"Category '{category_name}' does not exist.")
            
    def display_categories(self):
        for category_name, category_node in self.categories.items():
            print(f"\nCategory: {category_name}")
            for book in category_node.books:
                print(f"  - {book}")
                
                
                
class LibraryManagementSystem:
    def __init__(self):
        self.book_bst = BookBST()  # book management
        self.category_manager = CategroyManag()  #  linked lists for categories

    def add_book(self, title, author, category):
        new_book = Book(title, author, category)
        self.book_bst.insert(new_book)
        self.category_manager.add_book_to_category(new_book)  #Category
        print(f"Book '{title}' added successfully.") 

    def delete_book(self, title):
        book_node = self.book_bst.search(title)
        if book_node:
            self.book_bst.delete(title)
            self.category_manager.remove_book_from_category(title, book_node.book.category)
            print(f"Book '{title}' deleted successfully.")
        else:
            print(f"Book '{title}' not found.")

    def search_book(self, title):
        book_node = self.book_bst.search(title)
        if book_node:
            print("Book found:")
            print(book_node.book)
        else:
            print(f"Book '{title}' not found.")

    def borrow_book(self, title, user):
        book_node = self.book_bst.search(title)
        if book_node and book_node.book.is_available:
            book_node.book.is_available = False
            print(f"Book '{title}' borrowed by {user}.")
        elif book_node:
            book_node.book.borrowers_queue.enqueue(user)
            print(f"Book '{title}' is currently unavailable. {user} has been added to the waiting list.")
        else:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        book_node = self.book_bst.search(title)
        if book_node:
            if not book_node.book.borrowers_queue.is_empty():
                next_user = book_node.book.borrowers_queue.dequeue()
                print(f"Book '{title}' is now issued to {next_user}.")
            else:
                book_node.book.is_available = True
                print(f"Book '{title}' has been returned and is now available.")
        else:
            print(f"Book '{title}' not found in the library.")

    def display_all_books(self):
        books = self.book_bst.inorder_trav()
        print("Books in the library:")
        for book in books:
            print(book)

    def display_categories(self):
        print("Categories in the library:")
        self.category_manager.display_categories()
        

def main():
    library = LibraryManagementSystem()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Delete a Book")
        print("3. Search for a Book")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Display All Books")
        print("7. Display Categories")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            category = input("Enter book category: ")
            library.add_book(title, author, category)

        elif choice == '2':
            title = input("Enter the title of the book to delete: ")
            library.delete_book(title)

        elif choice == '3':
            title = input("Enter the title of the book to search: ")
            library.search_book(title)

        elif choice == '4':
            title = input("Enter the title of the book to borrow: ")
            user = input("Enter your name: ")
            library.borrow_book(title, user)

        elif choice == '5':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == '6':
            library.display_all_books()

        elif choice == '7':
            library.display_categories()

        elif choice == '8':
            # Exit the program
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

