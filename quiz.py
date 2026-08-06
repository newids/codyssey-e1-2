class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display_question(self, number):
        print(f"Q{number}: {self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            question=str(data["question"]), 
            choices=[str(choice) for choice in data["choices"]],
            answer=int(data["answer"])
            )

def default_quizzes():
    return [
        Quiz(
            question="파이썬에서 변수명으로 사용할 수 없는 것은?",
            choices=["my_var", "_value", "2nd_user", "user_name"],
            answer=3
        ),
        Quiz(
            question="다음 중 파이썬의 기본 데이터 타입이 아닌 것은?",
            choices=["int", "string", "list", "dict"],
            answer=2
        ),
        Quiz(
            question="리스트 `a = [10, 20, 30, 40]`에서 `a[1:3]`의 결과는?",
            choices=["[10, 20]", "[20, 30]", "[20, 30, 40]", "[10, 20, 30]"],
            answer=2
        ),
        Quiz(
            question="다음 연산의 결과는? `print(7 // 2)`",
            choices=["3.5", "3", "1", "3.0"],
            answer=2
        ),
        Quiz(
            question="파이썬에서 함수를 정의할 때 사용하는 키워드는?",
            choices=["func", "function", "def", "define"],
            answer=3
        )
    ]

# [
#     Quiz(
#         question="파이썬에서 조건문의 블록을 구분할 때 사용하는 방식은?",
#         choices=["중괄호 ({})", "들여쓰기 (Indentation)", "키워드 end", "세미콜론 (;)"],
#         answer=2
#     ),
#     Quiz(
#         question="문자열 `s = 'Python'`에서 `s.upper()`의 실행 결과는?",
#         choices=["python", "PYTHON", "Python", "Error"],
#         answer=2
#     ),
#     Quiz(
#         question="다음 중 딕셔너리(dictionary) 구조의 올바른 표현은?",
#         choices=["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "{'a': 1, 'b': 2}"],
#         answer=4
#     ),
#     Quiz(
#         question="`list(range(1, 5))`의 실행 결과는?",
#         choices=["[1, 2, 3, 4, 5]", "[1, 2, 3, 4]", "[0, 1, 2, 3, 4]", "[2, 3, 4, 5]"],
#         answer=2
#     ),
#     Quiz(
#         question="다음 코드 중 오류(Error) 없이 정상 실행되는 것은?",
#         choices=["'Age: ' + 20", "'Hello' * 3", "[1, 2] + 3", "(1, 2) + [3, 4]"],
#         answer=2
#     )
# ]