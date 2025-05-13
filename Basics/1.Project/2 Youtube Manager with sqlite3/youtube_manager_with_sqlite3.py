import sqlite3
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def print_line():
    print(Fore.YELLOW + "-" * 50)

def print_start_line():
    print(Fore.YELLOW + "╔" + "═" * 5 + "╦" + "═" * 30 + "╦" + "═" * 20 + "╗")

def print_middle_line():
    print(Fore.YELLOW + "╠" + "═" * 5 + "╬" + "═" * 30 + "╬" + "═" * 20 + "╣")

def print_bottom_line():
    print(Fore.YELLOW + "╚" + "═" * 5 + "╩" + "═" * 30 + "╩" + "═" * 20 + "╝")


def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    if not videos:
        print(Fore.RED + "❌ No videos found.")
    else:
        print_start_line()
        print(Fore.YELLOW + "║ " + Fore.CYAN + f"{'ID':<3} " +
        Fore.YELLOW + "║ " + Fore.CYAN + f"{'Video Name':<28} " +
        Fore.YELLOW + "║ " + Fore.CYAN + f"{'Duration':<18} " +
        Fore.YELLOW + "║")

        print_middle_line()

        for row in videos:
            print(Fore.YELLOW + "║ " + Fore.GREEN + f"{row[0]:<3} " +
            Fore.YELLOW + "║ " + Fore.GREEN + f"{row[1]:<28} " +
            Fore.YELLOW + "║ " + Fore.GREEN + f"{row[2]:<18} " +
            Fore.YELLOW + "║")


        print_bottom_line()


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print(Fore.GREEN + "✅ Video added successfully!")

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    if cursor.rowcount == 0:
        print(Fore.RED + "❌ No video found with that ID.")
    else:
        conn.commit()
        print(Fore.GREEN + "✅ Video updated successfully!")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    if cursor.rowcount == 0:
        print(Fore.RED + "❌ No video found with that ID.")
    else:
        conn.commit()
        print(Fore.GREEN + "🗑️  Video deleted successfully!")

def main():   
    print(
        "\n" +
        Fore.BLUE + Style.BRIGHT + "🎬 YouTube Video Manager " +
        Fore.LIGHTYELLOW_EX + Style.BRIGHT + "- by " +
        Fore.MAGENTA + Style.BRIGHT + "PARAG DEB"
    )
    while True:
        print_line()
        print(Fore.MAGENTA + "1. List all YouTube videos")
        print(Fore.MAGENTA + "2. Add a YouTube video")
        print(Fore.MAGENTA + "3. Update a YouTube video")
        print(Fore.MAGENTA + "4. Delete a YouTube video")
        print(Fore.MAGENTA + "5. Exit")
        print_line()

        choice = input(Fore.YELLOW + "Enter your choice (1-5): ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter video name: ").strip()
                time = input("Enter video duration (e.g., 10:30): ").strip()
                add_video(name, time)
            case '3':
                list_all_videos()
                try:
                    video_id = int(input("Enter video ID to update: "))
                    name = input("Enter new video name: ").strip()
                    time = input("Enter new video duration: ").strip()
                    update_video(video_id, name, time)
                except ValueError:
                    print(Fore.RED + "⚠️ Invalid input. ID must be a number.")
            case '4':
                list_all_videos()
                try:
                    video_id = int(input("Enter video ID to delete: "))
                    delete_video(video_id)
                except ValueError:
                    print(Fore.RED + "⚠️ Invalid input. ID must be a number.")
            case '5':
                print(Fore.CYAN + "👋 Exiting... Goodbye!")
                break
            case _:
                print(Fore.RED + "❌ Invalid choice. Please enter a number between 1 and 5.")

    conn.close()

if __name__ == "__main__":
    main()
