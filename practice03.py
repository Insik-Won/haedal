class Human:
    human_count = 0

    def __init__(self, name, age, state, is_drunk):
        self.name = name
        self.age = age
        self.state = state
        self.is_drunk = is_drunk

    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.state)
        if self.is_drunk:
            print("술에 취했습니다.")
            print("이 사람은 네발로 걸어다닙니다.")
        else:
            print('멀쩡합니다.')
            print("이 사람은 두발로 걸어다닙니다.")
        print()


human1 = Human("가유리", 15, "학생", is_drunk=False)
human2 = Human("황동석", 43, "회사원", is_drunk=True)

human1.print_info()
human2.print_info()
