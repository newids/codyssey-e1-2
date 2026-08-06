from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quiz = Quiz()
        self.state = {}

    def menu(self):
        print()
        print("=" * 40)
        print("          🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("        1. 퀴즈 풀기")
        print("        2. 퀴즈 추가")
        print("        3. 퀴즈 목록")
        print("        4. 점수 확인")
        print("        5. 종료")
        print("=" * 40)

    def run(self):
        # Main game loop
        while True:
            self.menu()
            choice = input(".    선택: ").strip()
            if not choice.isdigit() or not (1 <= int(choice) <= 5):
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue

            choice = int(choice)
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.check_score()
            else:
                print("👋 게임을 종료합니다.")
                break

    def play_quiz(self):
        print("\n🎮 퀴즈를 시작합니다! 🎮")
        return

    def add_quiz(self):
        print("\n➕ 새로운 퀴즈를 추가합니다. ➕")
        return

    def list_quizzes(self):
        print("\n📜 퀴즈 목록을 확인합니다. 📜")
        return

    def check_score(self):
        print("\n🏆 점수를 확인합니다. 🏆")
        return

    def write_state(self):
        print("💾 상태를 저장합니다. 💾")
        return
