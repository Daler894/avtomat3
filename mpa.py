Q = {'q0', 'qf'}
Sigma = {'a', 'b', 'c'}
Gamma = {'Z', 'A', 'B'}
q0 = 'q0'
Z0 = 'Z'
F = {'qf'}

delta = {
    ('q0', 'b', 'Z'): ('q0', 'BZ'),
    ('q0', 'b', 'B'): ('q0', 'BB'),
    ('q0', 'b', 'A'): ('q0', ''),
    ('q0', 'a', 'Z'): ('q0', 'AZ'),
    ('q0', 'a', 'A'): ('q0', 'AA'),
    ('q0', 'a', 'B'): ('q0', ''),
    ('q0', 'c', 'Z'): ('q0', 'Z'),
    ('q0', 'c', 'A'): ('q0', 'A'),
    ('q0', 'c', 'B'): ('q0', 'B'),
    ('q0', '', 'B'): ('qf', 'B')
}


def mpa_accepts(word):
    """
    Эмулирует работу МПА.
    word - список символов.
    """
    state = q0
    stack = [Z0]

    for ch in word:
        top = stack[-1]

        if (state, ch, top) in delta:
            new_state, push_str = delta[(state, ch, top)]

            stack.pop()
            if push_str != '':
                for symbol in reversed(push_str):
                    stack.append(symbol)

            state = new_state
        else:
            return False

    if (state, '', stack[-1]) in delta:
        new_state, push_str = delta[(state, '', stack[-1])]
        state = new_state

    return state in F


def main():
    """
    Запрашивает у пользователя цепочки в бесконечном цикле.
    Включает проверку на допустимые символы и команду выхода.
    """
    print("Программа распознавания цепочек для МПА (язык L11: na < nb).")
    print("Допустимые символы: a, b, c.")
    print("Для выхода введите 'exit' или 'выход'.\n")

    while True:
        user_input = input("Введите цепочку: ").strip()

        if user_input.lower() in ['exit', 'выход']:
            print("Выход из программы. До свидания!")
            break

        is_valid = True
        for char in user_input:
            if char not in Sigma:
                is_valid = False
                break

        if not is_valid:
            print(f"Ошибка! В цепочке есть символы, которых нет в алфавите {Sigma}.")
            print("Попробуйте еще раз.\n")
            continue

        word = list(user_input)
        res = mpa_accepts(word)
        result = "ДОПУСТИТЬ (Accept)" if res else "ОТКЛОНИТЬ (Reject)"

        print(f"Результат: {result}\n")


if __name__ == "__main__":
    main()