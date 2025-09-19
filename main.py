from playlist.playlist import Playlist


def main():
    my_playlist = Playlist()

    print("Adding songs to the playlist ...")
    my_playlist.add_song("Bohemian Rhapsody")
    my_playlist.add_song("Hotel California")
    my_playlist.add_song("Stairway to Heaven")
    my_playlist.add_song("Stairway to Heaven")

    print("\n" + "="*25 + "\n")
    my_playlist.show_playlist()


if __name__ == "__main__":
    main()



