# Завдання 1:
#
# Дано два текстових файли. Визначте, чи збігаються їхні рядки.
# Якщо ні, виведіть відмінний рядок з кожного файлу.
import filecmp

# lines1 = []
# file1 = open('file3.txt', 'r', encoding= 'utf8')
# for line in file1:
#     lines1.append(line)
# print(lines1)
# file1.close()
#
# lines2 = []
# file2 = open('File_new.txt', 'r', encoding= 'utf8')
# for text in file2:
#     lines2.append(text)
# print(lines2)
# file2.close()
# result = list(set(lines1)-set(lines2))
# print(result) # Пояснення. Я знайшла, що можна порівняти файли за допомогою модулю filecmp.cmp(f1, f2, shallow=True)
# але як правильно це робиться не описано, тому зробила по іншому
#
# Завдання 2:
#
# Даний текстовий файл. Створіть новий файл та запишіть у нього наступну статистику
# щодо вихідного файлу:
#
# with open('File_new.txt', 'r', encoding= 'utf8') as out_file:
#     text_in = out_file.read()
# count_sum = len(text_in)
# print(count_sum)
#
# count_line = text_in.count('\n') + 1
# print(count_line)
#
# vowels = 'УЕЄОАІЯИЮуеєоаіяию'
# consonants = 'ЙЦКНГШЩЗХЖДЛРПВФЬЧСМТБйцкнгшщзхждлрпвфчсмтьб'
# numbers = "0123456789"
# vowels_count = 0
# consonants_count = 0
# numbers_count = 0
# for i in text_in:
#     if i in vowels:
#         vowels_count = vowels_count + 1
#     elif i in consonants:
#         consonants_count = consonants_count + 1
#     elif i in numbers:
#         numbers_count = numbers_count + 1
# print(vowels_count)
# print(consonants_count)
# print(numbers_count)
#
# with open('New3.txt', 'w', encoding= 'utf8') as statistics:
#     statistics.write(f'Кількість символів: {count_sum}\n')
#     statistics.write(f'Кількість голосних букв: {vowels_count}\n')
#     statistics.write(f'Кількість приголосних букв: {consonants_count}\n')
#     statistics.write(f'Кількість рядків: {count_line}\n')
#     statistics.write(f'Кількість цифр: {numbers_count}\n')
# = Кількість символів;
# = Кількість рядків;
# = Кількість голосних букв;
# = Кількість приголосних букв;
# = Кількість цифр.
#
# Завдання 3:
#
# Даний текстовий файл. Видаліть з нього останній рядок.
# Результат запишіть у інший файл.

# f = open("file3.txt", 'rt', encoding= 'utf8')
# l = f.readlines()
# print(l[0 : -1])
# m = l[0 : -1]
# f.close()
#
# f = open('File_new2.txt', 'w', encoding= 'utf8')
# f.writelines(m)
# f.close()
# Завдання 4:
#
# Даний текстовий файл.
# Знайдіть довжину найдовшого рядка.

# f = open("file3.txt", 'rt', encoding= 'utf8')
# l = f.readlines()
# lines = []
# for i in l:
#     lines.append(len(i))
# bid_line = lines.index(max(lines))
# print(l[bid_line])
#
# f.close()


