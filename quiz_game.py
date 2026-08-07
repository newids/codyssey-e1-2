from datetime import datetime
import json
import os
import random

from quiz import Quiz, default_quizzes

STATE_FILE = "state.json"
HISTORY_FILE = "history.json"


class QuizGame:
    def __init__(self):
        self.quizzes = default_quizzes()
        self.best_score = None

    def display_menu(self):
        print()
        print("=" * 40)
        print("          🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("        1. 퀴즈 풀기")
        print("        2. 퀴즈 추가")
        print("        3. 퀴즈 목록")
        print("        4. 점수 확인")
        print("        5. 퀴즈 삭제")
        print("        6. 종료")
        print("=" * 40)

    def read_int(self, prompt, valid_range):
        MESSAGE = "⚠️ 잘못된 입력입니다. {}-{} 사이의 숫자를 입력하세요."
        while True:
            user_input = input(prompt).strip()
            if user_input == "":
                print(
                    f"⚠️ 입력이 비어있습니다. {MESSAGE.format(min(valid_range), max(valid_range))}")
                continue
            try:
                value = int(user_input)
                if value in valid_range:
                    return value
                else:
                    print(
                        f"⚠️ 잘못된 범위입니다. {MESSAGE.format(min(valid_range), max(valid_range))}")
            except ValueError:
                print(
                    f"⚠️ 잘못된 입력입니다. {MESSAGE.format(min(valid_range), max(valid_range))}")

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
        self.load_state()
        while True:
            self.display_menu()
            choice = self.read_int("     선택: ", range(1, 7))
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.check_score()
            elif choice == 5:
                self.delete_quiz()
            else:
                print("👋 게임을 종료합니다.")
                break

    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        total = len(self.quizzes)
        correct = 0
        penalty = 0

        new_quizzes = self.quizzes.copy()

        print("\n🎮 퀴즈를 시작합니다! 🎮")
        print("-" * 40)

        while True:
            random_on_off = self.read_text("랜덤으로 문제를 섞을까요? (y/n): ").lower()
            if random_on_off in ["y", "n"]:
                break
            print("⚠️ 'y' 또는 'n'을 입력하세요.")

        if random_on_off == "y":
            random.shuffle(new_quizzes)

        how_many = self.read_int(
            f"몇 문제를 풀고 싶으신가요? (1-{total}): ", range(1, total + 1))

        if how_many < total:
            new_quizzes = new_quizzes[:how_many]

        for number, quiz in enumerate(new_quizzes, start=1):
            quiz.display_question(number)
            user_answer = self.read_int(
                f"힌트가 보고 싶다면 0을 선택하세요. 답을 선택하세요 (1-{len(quiz.choices)}): ", range(0, len(quiz.choices) + 1))
            if user_answer == 0:
                quiz.display_hint()
                penalty += 1
                user_answer = self.read_int(
                    f"답을 선택하세요 (1-{len(quiz.choices)}): ", range(1, len(quiz.choices) + 1))

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                correct += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")
            print("-" * 40)
        score = round(correct / how_many * 100 - penalty / how_many * 50)
        if score < 0:
            score = 0
        print(
            f"🏆 결과: {how_many}문제 중 {correct}문제 정답! 힌트:{penalty}개 총점:({score}점)")
        self.save_history(how_many, correct, penalty, score)
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
            self.save_state()
        print("=" * 40)

    def add_quiz(self):
        print("\n➕ 새로운 퀴즈를 추가합니다. ➕")
        question = self.read_text("새로운 문제를 입력하세요: ")
        choices = []
        for i in range(4):
            choice = self.read_text(f"선택지 {i + 1}을 입력하세요: ")
            choices.append(choice)
        answer = self.read_int("정답 선택지 번호를 입력하세요 (1-4): ", range(1, 5))
        hint = self.read_text("힌트를 입력하세요: ")
        new_quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(new_quiz)
        self.save_state()
        print("✅ 퀴즈가 성공적으로 추가되었습니다.")

    def list_quizzes(self):
        if not self.quizzes:
            print("⚠️ 조회할 퀴즈가 없습니다.")
            return

        print("\n📜 퀴즈 목록을 확인합니다. 📜")
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")
        print("-" * 40)

    def delete_quiz(self):
        if not self.quizzes:
            print("⚠️ 삭제할 퀴즈가 없습니다.")
            return

        self.list_quizzes()
        print("-" * 40)
        index = self.read_int(
            f"삭제할 퀴즈 번호를 입력하세요 (1-{len(self.quizzes)}): ", range(1, len(self.quizzes) + 1))
        deleted_quiz = self.quizzes.pop(index - 1)
        self.save_state()
        print(f"✅ '{deleted_quiz.question}' 퀴즈가 삭제되었습니다.")

    def check_score(self):
        print("\n🏆 점수를 확인합니다. 🏆")
        if self.best_score is None:
            print("⚠️ 아직 퀴즈를 풀지 않았습니다. 최고 점수가 없습니다.")
        else:
            print(f"💯 최고 점수: {self.best_score}점")
        print("-" * 40)

    def load_state(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
            self.best_score = data.get("best_score")
            best = f"{self.best_score}점" if self.best_score is not None else "없음"
            print("💾 상태를 불러왔습니다. 💾")
            print(f"💾 {len(self.quizzes)}개의 퀴즈가 있습니다. 💾")
            print(f"💾 최고 점수: {best} 💾")
        except FileNotFoundError:
            print("💾 저장된 상태가 없습니다. 기본 퀴즈로 시작합니다. 💾")
        except (json.JSONDecodeError, KeyError, TypeError, ValueError, OSError):
            self.quizzes = default_quizzes()
            self.best_score = None
            print("⚠️ 데이터 파일이 손상되어 기본 퀴즈로 초기화합니다.")
            self.save_state()

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        # 임시 파일에 먼저 쓴 뒤 교체해서, 저장 중 오류가 나도 기존 파일이 손상되지 않게 한다.
        temp_file = STATE_FILE + ".tmp"
        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            os.replace(temp_file, STATE_FILE)
        except (OSError, ValueError) as e:
            print(f"⚠️ 데이터 저장에 실패했습니다: {e}")
            if os.path.exists(temp_file):
                os.remove(temp_file)

    def save_history(self, how_many, correct, penalty, score):
        new_entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "how_many": how_many,
            "correct": correct,
            "penalty": penalty,
            "score": score
        }
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history_data = json.load(f)
            if not isinstance(history_data, list):
                print("⚠️ 히스토리 파일 형식이 올바르지 않아 초기화합니다.")
                history_data = []
        except FileNotFoundError:
            history_data = []
        except (json.JSONDecodeError, OSError):
            print("⚠️ 히스토리 파일을 읽을 수 없어 새 히스토리로 시작합니다.")
            history_data = []

        history_data.append(new_entry)

        # 임시 파일에 먼저 쓴 뒤 교체해서, 저장 중 오류가 나도 기존 파일이 손상되지 않게 한다.
        temp_file = HISTORY_FILE + ".tmp"

        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(history_data, f, ensure_ascii=False, indent=2)
            os.replace(temp_file, HISTORY_FILE)
        except (OSError, ValueError) as e:
            print(f"⚠️ 히스토리 저장에 실패했습니다: {e}")
            if os.path.exists(temp_file):
                os.remove(temp_file)
