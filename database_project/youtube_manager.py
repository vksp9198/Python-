import sqlite3
conn = sqlite3.connect("youtube_data.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL) 
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name , time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (? ,? )", (name , time))
    conn.commit()

def update_video(video_id , name , time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE Id =?  ",(name, time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ? " , (video_id, ))

def main():
    while True:
        print(f"====== YOUTUBE MANAGER APP ======")
        print("1. List videos ")
        print("2. Add video ")
        print("3. Update video ")
        print("4. delete video ")
        print("5. Exit App ")
        
        choice = input("Enter your choice : ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name , time)
        elif choice == '3':
            video_id = input("Enter video id to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id, name , time)
        elif choice == '4':
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        else:
            print("Goodbye!!")
            break
    
    conn.close()
if __name__ == "__main__":
    main()