from .node import Node

class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None


    def add_song(self, title):
        new_song = Node(title)


        if self.head is None:
            self.head = new_song
            self.tail = new_song
        else:
            self.tail.next = new_song
            self.tail = new_song

    def show_playlist(self):
        current_node = self.head

        if current_node is None:
            print("The playlist is empty")
            return
        print("Your playlist!")

        while current_node:
            print(f"- {current_node.title}")
            current_node = current_node.next
        

