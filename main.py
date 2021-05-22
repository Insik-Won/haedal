class RegistrationNum:

    def is_born_before_2000(self, num_str):
        check_number = int(num_str[7]);
        return check_number <= 2;

    def get_location(self, num_str):
        check_number = int(num_str[8] + num_str[9])
        if check_number <= 8:
            return "서울"
        elif check_number <= 12:
            return "부산"
        elif check_number <= 15:
            return "인천"
        elif check_number <= 25:
            return "경기"
        elif check_number <= 34:
            return "강원"
        elif check_number <= 47:
            return "충청"
        elif check_number <= 66:
            return "전라"
        elif check_number <= 91:
            return "경상"
        elif check_number <= 95:
            return "제주"
        else:
            print("잘못된 주민등록번호입니다.")
            return None

    def get_sex(self, num_str):
        check_number = int(num_str[7]);
        return "남자" if check_number % 2 == 1 else "여자"

    def check_age(self, num_str):
        check_number = int(num_str[0] + num_str[1])
        if self.is_born_before_2000(num_str):
            return 2021 - (1900 + check_number);
        else:
            return 2021 - (2000 + check_number);

    def get_birthday(self, num_str):
        return num_str[0:6]

    def check_number_error(self, num_str):
        multipliers = "234567892345"

        check_number = 0
        for i in range(0, 12):
            check_number += int(num_str[i]) * int(multipliers[i])

        check_number = (11 - (check_number % 11)) % 10;

        return check_number;


checker = RegistrationNum()

num_str = "0207253861411"

print(checker.check_number_error(num_str))

'''
if  check_number <= 8:
    print(number, ": 출생 지역은 서울 입니다.")
elif check_number <= 12:
    print(number, ": 출생 지역은 부산 입니다.")
elif check_number <= 15:
    print(number, ": 출생 지역은 인천 입니다.")
elif check_number <= 25:
    print(number, ": 출생 지역은 경기 입니다.")
elif check_number <= 34:
    print(number, ": 출생 지역은 강원 입니다.")
elif check_number <= 47:
    print(number, ": 출생 지역은 충청 입니다.")
elif check_number <= 66:
    print(number, ": 출생 지역은 전라 입니다.")
elif check_number <= 91:
    print(number, ": 출생 지역은 경상 입니다.")
elif check_number <= 95:
    print(number, ": 출생 지역은 제주 입니다.")
else :
    print("잘못된 주민등록번호입니다.")
'''