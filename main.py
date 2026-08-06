from quiz_game import QuizGame

def main():
    quiz_game = QuizGame()
    try:
        quiz_game.run()
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("\nExiting the quiz game. Writing state...")
        quiz_game.write_state()

if __name__ == "__main__":
    main()
