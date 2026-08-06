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

    def read_input(self, prompt, valid_range):
        MESSAGE = "⚠️ 잘못된 입력입니다. {}-{} 사이의 숫자를 입력하세요."
        while True:
            user_input = input(prompt).strip()
            if user_input == "":
                print(f"⚠️ 입력이 비어있습니다. {MESSAGE.format(min(valid_range), max(valid_range))}")
                continue
            try:
                value = int(user_input)
                if value in valid_range:
                    return value
                else:
                    print(f"⚠️ 잘못된 범위입니다. {MESSAGE.format(min(valid_range), max(valid_range))}")
            except ValueError:
                print(f"⚠️ 잘못된 입력입니다. {MESSAGE.format(min(valid_range), max(valid_range))}")

    def read_text(self, prompt):
        while True:
            raw = input(prompt).strip()
            if not raw:
                print("⚠️ 빈 입력은 사용할 수 없습니다. 다시 입력하세요.")
                continue
            try:
                # 터미널 인코딩 불일치로 들어온 대리 문자(surrogate)는
                # UTF-8로 저장할 수 없으므로 여기서 걸러낸다.
                raw.encode("utf-8")
            except UnicodeEncodeError:
                print("⚠️ 인식할 수 없는 문자가 포함되어 있습니다. 터미널 인코딩(UTF-8)을 확인하고 다시 입력하세요.")
                continue
            return raw
        
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
