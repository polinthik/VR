import random
import string
import sys

class PasswordManager:
    def __init__(self):
        # Распространённые слабые пароли (в нижнем регистре)
        self.common_passwords = {
            'password', '123456', '12345678', '1234', 'qwerty', '12345', 'dragon',
            'baseball', 'football', 'letmein', 'monkey', '696969', 'abc123',
            'mustang', 'michael', 'shadow', 'master', 'jennifer', '111111',
            '2000', 'jordan', 'superman', 'harley', '1234567', 'fuckyou',
            'hunter', 'trustno1', 'ranger', 'buster', 'thomas', 'tigger',
            'robert', 'soccer', 'batman', 'test', 'pass', 'hello', 'admin'
        }
    
    def get_yes_no(self, prompt):
        """Запрос ответа да/нет с обработкой ошибок"""
        while True:
            answer = input(prompt).strip().lower()
            if answer in ['да', 'yes', 'y', 'д']:
                return True
            elif answer in ['нет', 'no', 'n', 'н']:
                return False
            else:
                print("Ошибка: введите 'да' или 'нет'")
    
    def get_password_length(self):
        """Запрос длины пароля с проверкой"""
        while True:
            try:
                length = int(input("Введите длину пароля (от 4 до 64): "))
                if 4 <= length <= 64:
                    return length
                else:
                    print("Ошибка: длина должна быть от 4 до 64 символов")
            except ValueError:
                print("Ошибка: введите целое число")
    
    def generate_password(self):
        """Генерация пароля по заданным критериям"""
        print("\n=== Генерация пароля ===\n")
        
        # Получение параметров
        length = self.get_password_length()
        use_upper = self.get_yes_no("Включать прописные буквы (A-Z)? (да/нет): ")
        use_lower = self.get_yes_no("Включать строчные буквы (a-z)? (да/нет): ")
        use_digits = self.get_yes_no("Включать цифры (0-9)? (да/нет): ")
        use_special = self.get_yes_no("Включать специальные символы (!@#$%^&*()_+)? (да/нет): ")
        
        # Проверка: выбрана хотя бы одна категория
        if not (use_upper or use_lower or use_digits or use_special):
            print("Ошибка: необходимо выбрать хотя бы одну категорию символов!\n")
            return
        
        # Формирование наборов символов
        char_sets = []
        if use_upper:
            char_sets.append(string.ascii_uppercase)
        if use_lower:
            char_sets.append(string.ascii_lowercase)
        if use_digits:
            char_sets.append(string.digits)
        if use_special:
            char_sets.append("!@#$%^&*()_+=-{}[]:;\"'<>,.?/|\\~")
        
        # Формирование общего набора символов
        all_chars = ''.join(char_sets)
        
        # Гарантируем хотя бы один символ из каждой выбранной категории
        password_chars = []
        for char_set in char_sets:
            password_chars.append(random.choice(char_set))
        
        # Добираем остальные символы
        for _ in range(length - len(password_chars)):
            password_chars.append(random.choice(all_chars))
        
        # Перемешиваем символы
        random.shuffle(password_chars)
        
        # Формируем пароль
        password = ''.join(password_chars)
        
        print(f"\nСгенерированный пароль: {password}\n")
    
    def check_password_strength(self, password):
        """Проверка надёжности пароля"""
        score = 0
        feedback = []
        
        # Проверка длины
        length = len(password)
        if length >= 12:
            score += 2
            feedback.append(f"✓ Длина ({length}) отличная")
        elif length >= 8:
            score += 1
            feedback.append(f"✓ Длина ({length}) хорошая")
        else:
            feedback.append(f"✗ Длина ({length}) недостаточная (рекомендуется 8+)")
        
        # Проверка на распространённые пароли
        if password.lower() in self.common_passwords:
            feedback.append("✗ Пароль входит в список самых распространённых!")
            return 0, feedback
        
        # Проверка различных типов символов
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+=-{}[]:;\"'<>,.?/|\\~" for c in password)
        
        if has_upper:
            score += 1
            feedback.append("✓ Есть прописные буквы")
        else:
            feedback.append("✗ Нет прописных букв")
        
        if has_lower:
            score += 1
            feedback.append("✓ Есть строчные буквы")
        else:
            feedback.append("✗ Нет строчных букв")
        
        if has_digit:
            score += 1
            feedback.append("✓ Есть цифры")
        else:
            feedback.append("✗ Нет цифр")
        
        if has_special:
            score += 1
            feedback.append("✓ Есть специальные символы")
        else:
            feedback.append("✗ Нет специальных символов")
        
        # Проверка на повторяющиеся символы
        if len(set(password)) < length * 0.7:
            feedback.append("⚠ Много повторяющихся символов")
            score -= 1
        
        # Оценка надёжности
        if score >= 6:
            strength = "ОТЛИЧНЫЙ"
            time_to_crack = "более 100 лет"
        elif score >= 4:
            strength = "ХОРОШИЙ"
            time_to_crack = "от нескольких месяцев до года"
        elif score >= 2:
            strength = "СРЕДНИЙ"
            time_to_crack = "от нескольких дней до недели"
        else:
            strength = "СЛАБЫЙ"
            time_to_crack = "от нескольких минут до часов"
        
        return score, feedback, strength, time_to_crack
    
    def evaluate_password(self):
        """Оценка надёжности пароля"""
        print("\n=== Проверка надёжности пароля ===\n")
        password = input("Введите пароль для проверки: ")
        
        # Проверка на пустой пароль
        if not password:
            print("Ошибка: пароль не может быть пустым!\n")
            return
        
        result = self.check_password_strength(password)
        
        if len(result) == 2:  # Случай распространённого пароля
            score, feedback = result
            print(f"\n{'='*50}")
            print(f"Результат проверки:")
            print(f"{'='*50}")
            for item in feedback:
                print(item)
            print(f"\nОценка надёжности: КРИТИЧЕСКИ СЛАБЫЙ (0/6)")
            print("Время взлома: мгновенно")
            print(f"{'='*50}\n")
        else:
            score, feedback, strength, time_to_crack = result
            print(f"\n{'='*50}")
            print(f"Результат проверки:")
            print(f"{'='*50}")
            for item in feedback:
                print(item)
            print(f"\nОценка надёжности: {strength} ({score}/6)")
            print(f"Примерное время взлома: {time_to_crack}")
            
            # Дополнительные рекомендации
            if score < 4:
                print("\nРекомендации по улучшению:")
                if len(password) < 8:
                    print("- Увеличьте длину пароля до 12+ символов")
                if not any(c.isupper() for c in password):
                    print("- Добавьте прописные буквы")
                if not any(c.islower() for c in password):
                    print("- Добавьте строчные буквы")
                if not any(c.isdigit() for c in password):
                    print("- Добавьте цифры")
                if not any(c in "!@#$%^&*()_+=-{}[]:;\"'<>,.?/|\\~" for c in password):
                    print("- Добавьте специальные символы")
                if password.lower() in self.common_passwords:
                    print("- Избегайте использования распространённых паролей")
            print(f"{'='*50}\n")
    
    def run(self):
        """Главный цикл программы"""
        print("\n" + "="*60)
        print(" ДОБРО ПОЖАЛОВАТЬ В ГЕНЕРАТОР И ОЦЕНЩИК ПАРОЛЕЙ ")
        print("="*60)
        print(" Ваш надёжный помощник в создании безопасных паролей ")
        print("="*60 + "\n")
        
        while True:
            print("ГЛАВНОЕ МЕНЮ:")
            print("1 - Сгенерировать пароль")
            print("2 - Проверить надёжность пароля")
            print("3 - Выйти")
            
            choice = input("\nВыберите действие (1-3): ").strip()
            
            if choice == '1':
                self.generate_password()
            elif choice == '2':
                self.evaluate_password()
            elif choice == '3':
                print("\nБлагодарим за использование программы!")
                print("Помните: безопасность начинается с надёжного пароля.\n")
                sys.exit(0)
            else:
                print("Ошибка: введите 1, 2 или 3\n")
            
            # Пауза перед возвратом в меню
            input("Нажмите Enter для продолжения...")
            print("\n" + "-"*60 + "\n")

def main():
    """Точка входа в программу"""
    app = PasswordManager()
    app.run()

if __name__ == "__main__":
    main()