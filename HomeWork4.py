# Завдання 1
# Користувач вводить рядок з клавіатури. Перевірте, чи є введений рядок паліндромом.
# Паліндром - слово або текст, яке читається однаково зліва направо та зправа наліво.

# a = input("numb: ") # просто цифри
#
# if a == a[:: -1]:
#     print("yes")
# else:
#     print("no")

# a = input("numb: ")
# a1 = a.lower()
# a2 = "".join(i for i in a1 if i.isalnum())
# if a2 == a2[:: -1]:
#      print("yes")
# else:
#      print("no")

# Завдання 2
# Користувач вводить із клавіатури деякий текст, після чого користувач вводить перелік зарезервованих слів.
# Необхідно знайти в тексті всі зарезервовані слова та змінити їхній регістр на верхній.


# a = input("text: ")
# rez_word = input("Reserved words: ").split(" ")
# # words = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
# #      'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
# #      'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
# #      'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# for words in a.split(" "):
#      if words.lower() in rez_word:
#          a = a.replace(words, words.upper())
# print(a)


# Завдання 3
# Є певний текст. Порахуйте кількість речень у цьому тексті та виведіть на екран отриманий результат.
# Будьте уважні, та не забудьте протестувати на різних текстах.
#
def IsCharOp(text):
    sAll = "!.?"
    k = 0
    for c1 in text:
        for c2 in sAll:
            if c1==c2:
                k = k+1
    return k
user_text = input("Enter text: ")

k = IsCharOp(user_text)
print("Numders of counts = ", k)