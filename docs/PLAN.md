# 1. 미션 소개
터미널에서 동작하는 나만의 퀴즈 게임을 처음부터 끝까지 구현
Python 기본 문법을 사용
클래스(객체 지향)로 코드를 역할별로 구조화
JSON 파일 저장
Git으로 변경 이력을 관리 - 기능 단위로 커밋하고, 브랜치를 나눠 작업한 뒤 병합하며, GitHub에 저장소를 공개

# 2. 최종 결과물
1. 퀴즈 게임
- 메뉴 - 퀴즈 출제/등록/목록/점수 확인/종료 
- 기능 - 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 점수 확인
- 퀴즈 - 5개 이상
- 점수 - 종료 후 유지(파일 저장)
2. 코드 구조
- class - 2개 이상(Quiz, QuizGame 등)
- method - 입력 처리/게임 진행/저장 로직 등
- data - project root 에 state.json / UTF-8 encoding
3. Github 저장소
- 10개 이상의 의미있는 커밋
- 1회 이상 브랜치 생성·병합
- clone, pull을 각각 1회 이상 사용한 기록
- README.md
    - 프로젝트 개요
    - 퀴즈 주제 선정 이유
    - 실행 방법
    - 기능 목록
    - 파일 구조
    - 데이터 파일 설명(state.json 등)

# 3. 과제 목표
- Python 기초
    - 변수
    - int, str, bool, list, dict
    - if/elif/else
    - for, while
    - 함수, 매개변수, 반환값
- 클래스와 객체
    - 클래스
    - __init__, self
    - attribute, method
- 파일 입출력
    - file read, write
    - JSON
    - try/except
- Git
    - Git
    - init, add, commit, push, pull, checkout, clone
    - branch
    - clone, pull

# 4. 기능 요구 사항
1. Git
    - create Github new repository
    - local repository
    - create .gitignore, README.md
    - 초기 설정, commit, push
2. 메뉴
    - 실행시 메뉴 출력
    - 사용자가 기능 선택
    - 종료 기능
    - 잘못된 입력 처리
    - Git: 메뉴 기능 완성 후 커밋
3. 공통 입력/예외 처리 기준(최소 요구)
    - 숫자 입력
        - 공백 제거
        - 숫자 변환
        - 허용 범위 밖 숫자 처리
        - Enter 처리 - 안내 메시지 출력
    - Ctrl-C(Keyboard Interrupt), 입력 스트림 종료(EOF Error) - 비정상 종료하지 않도록
        - 안내 메시지 출력, 저장, 안전하게 종료
    - 데이터 파일 - 없거나 손상된 경우도 정상 실행
        - 파일 없으면 기본 퀴즈 데이터 사용
        - 손상 -> 메시지 출력 -> 기본 퀴즈 데이터로 복구??? 초기화???
4. Quiz Class
    - Quiz Class - 개별 퀴즈 표현
    - 속성 : question, choices, answer
        - 선택지는 4개 기본
        - 정답은 1~4번 중 하나
    - 메서드 : 퀴즈 출력, 정답 확인 등
    - Git : Quiz Class 작성 후 commit
5. 기본 퀴즈 데이터
    - 5개 이상 직접 작성
    - 선택지 4개, 정답 포함
    - Quiz class instance로 퀴즈 생성
    - Git: 기본 퀴즈 데이터 작성 후 commit
6. 퀴즈 풀기(브랜치 활용)
    - Git: main 브랜치 이외의 추가 브랜치 생성 후 작업
    - 출제
    - 정덥 입력
    - 정/오답 여부 출력
    - 모든 문제 풀면 결과 표시
    - 퀴즈가 없는 경우 처리
    - Git: commit 후 main으로 merge
7. 퀴즈 추가
    - 새 퀴즈 등록
    - 문제, 선택지, 정답 입력
    - 잘못된 입력 처리
    - 파일 저장
    - Git: 완성 후 commit
8. 퀴즈 목록
    - 목록 출력
    - 퀴즈가 없는 경우 처리
    - Git: 완성 후 commit
9. 점수 확인
    - 최고 점수 출력
    - 최고 점수 갱신
    - 파일에 저장
    - 아직 퀴즈를 풀지 않은 경우 처리
    - Git: 완성 후 commit
10. QuizGame Class
    - 게임 전체 관리
    - 속성 : 퀴즈 목록, 최고 점수 등
    - 메서드 : 메뉴 표시, 퀴즈 풀기, 퀴즈 추가, 목록 보기, 점수 확인, 파일 저장/불러오기 등
    - Git: Class 구조 정리 후 commit
11. 파일 저장/불러오기(**state.json**)
    - 프로젝트 루트에 UTF-8 인코딩으로 저장
    - JSON 불러오기
    - 파일이 없는 경우 기본 퀴즈 데이터 사용
    - 파일 손상, 읽기/쓰기 오류 try/except 처리
    - 최소 스키마 예시(데이터 형태 참고; 키 이름/구조는 일관되게 유지):
        - quizzes: 퀴즈 목록
        - best_score: 최고 점수(또는 최고 정답 수 등)
    - Git: 완성 후 commit
12. README.md
    - 상동
    - Git: 완성 후 commit
13. Git 저장소 복제
    - 개발 완료 후 수행
    - 별도 로컬 폴더에 clone
    - README.md 수정 후 commit, push
    - 기존 폴더에서 pull
    - 확인

# 5. 보너스 과제
1. 랜덤 출제
    - 풀기 전 순서 섞기
    - random 모듈 학습
2. 문제 수 선택
    - 풀기 시 몇 문제 풀지 선택
3. 힌트 기능
    - Quiz class에 힌트 속성 추가
    - 풀이 중 힌트 조회
    - 힌트 사용 시 점수 차감
4. 퀴즈 삭제 기능
    - 등록된 퀴즈 삭제
    - 삭제 후 파일에 반영
5. 점수 기록 히스토리
    - 최고 점수 외 모든 게임 기록 저장
    - 날짜/시간, 푼 문제 수, 점수 기록

# 6. 개발 환경
- Python 3.10 이상
- 기본 문법과 표준 라이브러리 사용

# 7. 제약 사항
- 데이터 저장 규칙
    - 상동
    - 상동
- 코드 구조
    - 기능별로 함수 분리
    - 클래스 2개 이상
- Git 워크플로우
    - 10개 이상 의미 있는 커밋
        - 기능 단위 커밋(메뉴/Quiz/플레이/추가/저장/README 등) + 커밋 메시지에 변경 요약 포함
    - 의미 있는 커밋 메시지
        - `Feat: 퀴즈 출제 기능 구현`
        - `Fix: 점수 계산 오류 수정`
        - `Docs: README 실행 방법 추가`
        - `Refactor: QuizGame 책임 분리`
    - `init`, `add`, `commit`, `push`, `pull`, `checkout`, `clone`
- 제출물
    - Github 저장소 URL
    - 개발 환경 설정 스크린샷(예: VSCode, Python 버전, Git 설정)
    - 프로그램 실행 결과 스크린샷(퀴즈 추가, 목록, 플레이, 점수)
    - git log --oneline --graph 결과 스크린샷

