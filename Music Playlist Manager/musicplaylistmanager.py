#Music Playlist Manager using LinkedList and Stacks

class SongNode:
    def __init__(self, song_name):
        self.song_name = song_name
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song_name):
        new_song = SongNode(song_name)
        if not self.head:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song
        print(f"Added song: {song_name}")

    def display(self):
        if not self.head:
            print("The playlist is empty.")
            return
        print("Current Playlist:")
        temp = self.head
        while temp:
            print(f" - {temp.song_name}")
            temp = temp.next

    def delete_song(self, song_name):
        temp = self.head
        prev = None
        while temp and temp.song_name != song_name:
            prev = temp
            temp = temp.next
        if not temp:
            print(f"Song {song_name} not found in the playlist.")
            return
        if not prev:
            self.head = temp.next
        else:
            prev.next = temp.next
        print(f"Deleted song: {song_name}")

class PlaylistManager:
    def __init__(self):
        self.playlist = Playlist()
        self.undo_stack = []  
        self.redo_stack = []  

    def add_song(self, song_name):
        self.playlist.add_song(song_name)
        self.undo_stack.append(("delete", song_name))  # To undo add, we delete the song
        self.redo_stack.clear()  

 
    def delete_song(self, song_name):
        self.playlist.delete_song(song_name)
        self.undo_stack.append(("add", song_name))  # To undo delete, we add back the song
        self.redo_stack.clear()  

    def display_playlist(self):
        self.playlist.display()


    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        action, song_name = self.undo_stack.pop()
        if action == "add":
            self.playlist.add_song(song_name)
            self.redo_stack.append(("delete", song_name))
        elif action == "delete":
            self.playlist.delete_song(song_name)
            self.redo_stack.append(("add", song_name))
        print(f"Undone: {action} {song_name}")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        action, song_name = self.redo_stack.pop()
        if action == "add":
            self.playlist.add_song(song_name)
            self.undo_stack.append(("delete", song_name))
        elif action == "delete":
            self.playlist.delete_song(song_name)
            self.undo_stack.append(("add", song_name))
        print(f"Redone: {action} {song_name}")

def main():
    manager = PlaylistManager()

    while True:
        print("\n1. Add Song\n2. Delete Song\n3. Display Playlist\n4. Undo\n5. Redo\n6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            song_name = input("Enter song name to add: ")
            manager.add_song(song_name)
        elif choice == 2:
            song_name = input("Enter song name to delete: ")
            manager.delete_song(song_name)
        elif choice == 3:
            manager.display_playlist()
        elif choice == 4:
            manager.undo()
        elif choice == 5:
            manager.redo()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


#USED LINKED LIST TO STORE THE SONGS AND STACKS FOR UNDO AND REDO FUNCTIONALITY....
