class state:
    def __init__(self):
        self.filename = "state.json"

    def display_info(self):
        print(f"state filename: {self.filename}")

    @staticmethod
    def read_state():
        return

    @staticmethod
    def create_state(name, capital, population):
        return state(name, capital, population)

    @staticmethod
    def update_state():
        return

    @staticmethod
    def delete_state():
        return
