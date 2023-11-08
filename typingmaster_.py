import random
import json
import time

# Constants
WORD_LIST_FILE = 'word_categories.json'  # Change to  your word category files
LEADERBOARD_FILE = 'leaderboard.json'  # Change to your leader board files

class TypingTest:
    def __init__(self):
        self.username = input("Enter your username: ")
        self.leaderboard = []

    def load_words_from_json(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def update_leaderboard(self, wpm):
        self.leaderboard.append({'username': self.username, 'wpm': wpm})
        self.leaderboard.sort(key=lambda x: x['wpm'], reverse=True)
        with open(LEADERBOARD_FILE, 'w') as file:
            json.dump(self.leaderboard, file, indent=4)

    def show_leaderboard(self):
        try:
            with open(LEADERBOARD_FILE, 'r') as file:
                leaderboard_data = json.load(file)
                print("Leaderboard:")
                for i, entry in enumerate(leaderboard_data, start=1):
                    print(f"{i}. {entry['username']}: {entry['wpm']} WPM")
        except FileNotFoundError:
            print("Leaderboard is empty.")

    def start_typing_test(self):
        word_data = self.load_words_from_json(WORD_LIST_FILE)
        categories = list(word_data.keys())
        
        print("Select a category:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        category_choice = input("Enter the category number: ")

        if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
            category = categories[int(category_choice) - 1]
            words = word_data[category]
            random.shuffle(words)

            print(f"Category: {category}")
            print("Type the following words. Press 'Ctrl+C' to quit.")
            input("Press Enter to start...")  # Wait for press "enter" by the user

            start_time = time.time()
            words_typed = 0

            try:
                for word in words:
                    print(word)
                    user_input = input()
                    words_typed += 1
            except KeyboardInterrupt:
                print("Typing test aborted.")

            end_time = time.time()
            elapsed_time = end_time - start_time
            wpm = int(words_typed / (elapsed_time / 60))

            print(f"Words Typed: {words_typed}")
            print(f"Time Taken: {elapsed_time:.2f} seconds")
            print(f"Words Per Minute (WPM): {wpm}")

            self.update_leaderboard(wpm)
        else:
            print("Invalid category choice!! Please try again..")

    def run(self):
        print("Welcome to the Typing Test Application!")

        while True:
            print("\nOptions:")
            print("1. Start Typing Test")
            print("2. Show Leaderboard")
            print("3. Exit")
            choice = input("please choose your choice: ")

            if choice == '1':
                self.start_typing_test()
            elif choice == '2':
                self.show_leaderboard()
            elif choice == '3':
                print("Goodbye..., come back soon!. have a good day")
                break

if __name__ == "__main__":
    typing_test = TypingTest()
    typing_test.run()
