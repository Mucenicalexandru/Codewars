import numpy
import string
import re
import math
from collections import Counter


def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = mpg * fuel_left
    if distance_to_pump < a:
        return True1
    else:
        return False


def basic_op(operator, value1, value2):
    if operator == "+":
        return value1+value2
    elif operator == "-":
        return value1-value2
    elif operator == "*":
        return value1*value2
    elif operator == "/":
        return value1/value2
    else:
        print("Invalid input")


def count_positives_sum_negatives(arr):
    positive = 0
    if len(arr) < 1:
        return arr
    else:
        for i in arr:
            if i > 0:
                positive += 1
        a = sum(i for i in arr if i < 0)
        return [positive, a]


def array_diff(a, b):
    c = [i for i in a if i not in b]
    return c


def summation(num):
    #  return (1+num) * num / 2
    b = []
    for i in range(num+1):
        b.append(i)
    return sum(b)


def row_sum_odd_numbers(n):
    return n**3


def count_smileys(arr):
    a = [':)', ':D', ':-)', ':-D', ':~)', ':~D',
         ';)', ';D', ';-)', ';-D', ';~)', ';~D']
    b = []
    for i in a:
        if i in arr:
            b.append(i)
    return len(b)


def past(h, m, s):
    if 0 < s <= 59:
        s = s * 1000
    else:
        s = 0
    if 0 < m <= 59:
        m = m * 60000
    else:
        m = 0
    if 0 < h <= 23:
        h = h * 60 * 60 * 1000
    else:
        h = 0
    return s+m+h


def getCount(inputStr):
    num_vowels = 0
    for i in inputStr:
        if i in "aeiou":
            num_vowels = num_vowels+1
    return num_vowels


def hero(bullets, dragons):
    a = bullets/dragons
    if a >= 2:
        return True
    else:
        return False


def triple_trouble(one, two, three):
    list_l = []
    for i in range(len(one)):
        a = one[i] + two[i] + three[i]
        list_l.append(a)
    return "".join(list_l)


def solution(number):
    a = (number-1) // 3
    b = (number-1) // 5
    list1 = []
    list2 = []
    if number in range(0, 6):
        return 0
    else:
        for i in range(1, a+1):
            x = i*3
            list1.append(x)
            z = set(list1)

        for j in range(1, b+1):
            y = j*5
            list2.append(y)
            w = set(list2)
        res = z | w
        return sum(res)


def sum_of_minimums(numbers):
    min_list = []
    for i in range(len(numbers)):
        x = min(numbers[i])
        min_list.append(x)
    return sum(i for i in min_list)


'''def sum_of_minimums(numbers):
    return sum(map(min, numbers))'''


def get_middle(s):
    0 < len(s) < 1000
    if len(s) % 2 != 0:
        x = len(s)
        y = (x - 1) / 2
        return s[int(y)]
    else:
        q = len(s)
        w = int((q - 1) / 2)
        r = int((q + 1) / 2)
        string = s[w]+s[r]
        return string


def duplicate_count(text):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    x = []
    text = text.lower()
    for i in range(26):
        b = text.count(a[i])
        if b > 1:
            x.append(b)
    return len(x)


def duplicate_count(text):
    x = Counter(text.lower())
    y = x.values()
    a = []
    for i in y:
        if i > 1:
            a.append(i)
    return len(a)


def find_next_square(sq):
    a = math.sqrt(sq)   # a = sq**0.5
    int_a = int(a)
    if int_a == a:
        return int((a+1)**2)
    else:
        return -1


def xo(s):
    a = Counter(s.lower())
    value_x = a.get('x')
    value_y = a.get('o')
    if value_x == value_y:
        return True
    else:
        return False


def even_or_odd(number):
    number = abs(number)
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def is_square(n):
    x = n**0.5
    if n >= 0:
        if int(x) == x:
            return True
        else:
            return False
    else:
        return False


def disemvowel(string):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    return string.translate({ord(i): None for i in vowels})
    return string.translate(None, "aeiouAEIOU")


def find_it(seq):
    dictionary_seq = Counter(seq)
    for k, v in dictionary_seq.items():
        if v % 2 != 0:
            return k


def divide(weight):
    x = weight / 2
    if x == 1:
        return False
    elif x == int(x):
        return True
    else:
        return False


def ifChuckSaysSo():
    return not True


def comp(array1, array2):
    try:
        return sorted([i**2 for i in array1]) == array2
    except:
        return False


def square_sum(numbers):
    return sum(i**2 for i in numbers)


def shorten_to_date(long_date):
    return long_date.split(',')[0]


def is_isogram(string):
    a = []
    for i in string.lower():
        a.append(i)
    b = set(a)
    if len(a) == len(b):
        return True
    else:
        return False


def is_isogram(string):
    return len(string) == len(set(string.lower()))


def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) < len(odds):
        return evens[0]
    else:
        return odds[0]

#    evens = [i for i in integers if x%2 == 0]
#    odds = [i for i in integers if x%2 != 0
#    return odds[0] if len(odds)<len(evens) else evens[0]


def create_phone_number(n):
    a = str(n[0]) + str(n[1]) + str(n[2])
    b = str(n[3]) + str(n[4]) + str(n[5])
    c = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    return ('('+a+')'+" "+b+"-"+c)
#  print("({}{}{}) {}{}{}-{}{}{}{}".format(*n))


def number(bus_stops):
    b = []
    for i in range(len(bus_stops)):
        a = bus_stops[i][0] - bus_stops[i][1]
        b.append(a)
    return sum(i for i in b)


def descending_order(num):
    array = [i for i in str(num)]
    return int("".join(sorted(array, reverse=True)))


'''def high_and_low(numbers):
    li = list(numbers.split(" ")) 
    return max(li)'''

'''numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
li = list(numbers.split(" ")) 
print(li)
print(max(li))
print(min(li))
'''


def high_and_low(s):
    a = [int(n) for n in s.split()]
    max = -99999999999
    min = 9999999999
    number = ""
    for i in a:
        if i > max:
            max = i
    for j in a:
        if j < min:
            min = j
    number = str(max) + " " + str(min)
    return number


def accum(s):
    s = s.lower()
    array = []
    for i in range(1, len(s)+1):
        for j in s:
            array.append(j*i)
    b = []
    for i in range(len(s)):
        a = array[(len(s)+1)*i]
        b.append(a.capitalize())
    return ("-".join(b))


s = "helloWorld"  # return hello World


def solution(s):
    a = re.findall('[A-Z][^A-Z]*', s)
    index = []
    for i, j in enumerate(s):
        if j.isupper():
            index.append(i)
    b = index[0]
    x = s[0:b]
    y = " ".join(a)
    lst = []
    lst.append(x)
    lst.append(y)
    return ' '.join(lst)

# clever solution : return ''.join(' ' + c if c.isupper() else c for c in s)


def hydrate(drink_string):
    a = sum(int(i) for i in drink_string if i.isdigit())
    if a == 1:
        return (str(a) + " " + "glass of water")
    else:
        return (str(a) + " " + "glasses of water")


def up_array(arr):
    a = []
    for i in arr:
        if i >= 0:
            a.append(str(i))
        if len(str(i)) > 1:
            return None
    if len(a) != len(arr):
        return None
    else:
        b = "".join(a)
        c = int(b)+1
        lst = []
        for i in str(c):
            lst.append(i)
        for i in range(0, len(lst)):
            lst[i] = int(lst[i])
        return lst


def data_reverse(data):
    len_array = len(data)
    the_range = len_array / 8
    the_range = int(the_range)
    empty_array = []
    for i in range(the_range):
        empty_array.append(data[8*i:8*(i+1)])
    reversed_array = empty_array[::-1]
    return [j for i in reversed_array for j in i]


def remove_smallest(numbers):
    numbers.remove(min(numbers))
    return numbers


def square_digits(num):
    strings = []
    for i in str(num):
        strings.append(str(int(i)**2))
    a = "".join(strings)
    return int(a)


def alphabet_position(text):
    letter_list = list(string.ascii_lowercase)
    number_list = [i for i in range(1, 27)]
    dictionary = dict(zip(letter_list, number_list))

    result = []
    for i in text.lower():
        if i in letter_list:
            result.append(str(dictionary.get(i)))

    final_result = " ".join(result)
    return final_result


def beggars(values, n):
    if n == 0:
        return []
    else:
        empty_array = []
        sum = 0
        for j in range(n):
            for i in range(j, len(values), n):
                sum = sum + values[i]
            empty_array.append(sum)

        new_list = [empty_array[0]]
        for i in range(1, len(empty_array)):
            dif = empty_array[i]-empty_array[i-1]
            new_list.append(dif)
        return new_list

# return [sum(values[i::n]) for i in range(n)]


def digital_root(n):
    while len(str(n)) > 1:
        sum = 0
        for i in str(n):
            sum = sum + int(i)
            n = sum
    return n


def find_short(s):
    array = []
    for i in s.split(" "):
        array.append(len(i))
    return min(array)


def dig_pow(n, p):
    number_list = []
    for i in str(n):
        number_list.append(i)
    array = []
    for i, j in enumerate(number_list):
        array.append(int(j)**(i+p))
    sum_array = sum(array)
    res = sum_array/n
    if res == int(res):
        return int(res)
    else:
        return -1


def order(sentence):
    array = []
    sentence = sentence.split(" ")
    for j in range(len(sentence)):
        for string in sentence:
            if str(j+1) in string:
                array.append(string)
    return " ".join(array)


def domain_name(url):
    array = ["https://www.", "http://www.", "http://", "https://", "www."]
    result = url.startswith("http")
    result1 = url.startswith("www.")
    if result or result1 is True:
        for i in array:
            if i in url:
                url = url.split(i)
                new_url = url[1]
                new_url = new_url.split(".")
                return new_url[0]
    else:
        url1 = url.split(".")
        return url1[0]


def domain_name_1(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


def find_missing_letter(chars):
    array = []
    correct_array = []
    letter_number = ord(chars[0])
    for i in chars:
        array.append(ord(i))
    for i in range(len(chars)+1):
        correct_array.append(int(letter_number) + i)
    unique_number = set(array) ^ set(correct_array)
    number = list(unique_number)[0]
    return chr(number)


def get_sum(a, b):
    if a < b:
        return [sum(i for i in range(a, b+1))][0]
    elif a > b:
        return [sum(i for i in range(b, a+1))][0]
    else:
        return a


def divisors(integer):
    array = []
    for i in range(2, integer+1):
        if integer % i == 0:
            array.append(i)
    if len(array) == 1:
        return (f"{str(integer)} is prime")
    else:
        array.remove(integer)
        return array


def longest(s1, s2):
    unique_letters = set(s1) | set(s2)
    sorted_list = sorted(list(unique_letters))
    string = "".join(sorted_list)
    return string


def is_prime(num):
    array = [i for i in range(1, num+1) if num % i == 0]
    return len(array) == 2


def letter_count(s):
    array = []
    for i in s:
        array.append(i)

    dictionary = dict(Counter(array))
    return dictionary


def is_pangram(s):
    array = []
    for i in s:
        if i.isalpha():
            array.append(i.lower())
    return len(set(array)) == 26


def up_array(arr):
    a = []
    for i in arr:
        if i >= 0:
            a.append(str(i))
        if len(str(i)) > 1:
            return None
    if len(a) != len(arr):
        return None
    elif arr == []:
        return None
    else:
        b = "".join(a)
        c = int(b)+1
        lst = []
        for i in str(c):
            lst.append(i)
        for i in range(0, len(lst)):
            lst[i] = int(lst[i])
        return lst


def tower_builder(n_floors):
    number_list = [i for i in range(2*n_floors) if i % 2 != 0]
    empty_array = []
    for i in range(1, n_floors+1):
        empty_array.append((len(number_list)-i)*" " +
                           number_list[i-1]*"*" + (len(number_list)-i)*" ")
    return empty_array


def persistence(n):
    counter = 0
    while len(str(n)) > 1:
        array = []
        for i in str(n):
            array.append(int(i))
        n = numpy.prod(array)
        counter += 1
    return counter


def find_uniq(arr):
    dictionary = dict(Counter(arr))
    for k, v in dictionary.items():
        if v == 1:
            return k


def iq_test(numbers):
    number_list = numbers.split(" ")
    odd_pos = []
    even_pos = []
    for i, j in enumerate(number_list):
        if int(j) % 2 != 0:
            odd_pos.append(i+1)
        else:
            even_pos.append(i+1)
    if len(odd_pos) > len(even_pos):
        return even_pos[0]
    else:
        return odd_pos[0]


def sort_array(source_array):
    all_index = [i for i in range(len(source_array))]
    even_index = []
    odd = []
    even = []

    for i, j in enumerate(source_array):
        if j % 2 == 0:
            even_index.append(i)
            even.append(j)
        else:
            odd.append(j)

    odd_index = list(set(all_index) ^ set(even_index))

    sorted_odd = sorted(odd)

    for i, j in enumerate(odd_index):
        even.insert(j, sorted_odd[i])

    return even


def high(word):
    letters = list(string.ascii_lowercase)
    numbers = [n for n in range(1, 27)]

    dictionary = dict(zip(letters, numbers))

    list_of_words = word.split(" ")

    sum = 0
    sum_list = []
    for j in range(len(list_of_words)):
        for i in list_of_words[j]:
            sum = sum + dictionary[i]
        sum_list.append(sum)
        sum = 0

    for i, j in enumerate(sum_list):
        if j == max(sum_list):
            return list_of_words[i]


def narcissistic(value):
    power = len(list(str(value)))
    for i in str(value):
        result = sum([int(i)**power for i in str(value)])

    return value == result


def encrypt_this(text):
    li = list(text.split(' '))
    new_list = []

    for word in li:
        if len(word) == 0:
            return ""
        if len(word) == 1:
            word = str(ord(word[0]))
        elif len(word) == 2:
            word = str(ord(word[0])) + word[1]
        elif len(word) == 3:
            word = str(ord(word[0])) + word[-1] + word[1]
        else:
            word = str(ord(word[0])) + word[-1] + word[2:-1] + word[1]
        new_list.append(word)
    return " ".join(new_list)


def is_valid_IP(string):

    a = string.split(".")
    array = []
    if string == "":
        return False
    else:
        for i in a:
            if i.isalpha():
                return False
            elif " " in i:
                return False
            else:
                if 0 <= int(i) <= 255:
                    array.append(i)
        if len(array) == 3:
            return False
        if len(array) == 4:
            if len(array[0]) == len(array[1]) == len(array[2]) == len(array[3]) == 3:
                return False
            else:
                return True
        else:
            return False


def pig_it(text):
    result = []
    text_list = text.split(" ")
    for i in text_list:
        if i.isalpha():
            i = i[1:] + i[0] + "ay"
            result.append(i)
        else:
            result.append(i)
    return (" ".join(result))


def to_jaden_case(string):
    result = []
    array = quote.split(" ")
    for i in array:
        result.append(i.capitalize())
    return " ".join(result)


def search(titles, term):
    result = []
    for i in titles:
        if term in i.lower():
            result.append(i)
    return result


def average_string(s):
    dictionary = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
                  'seven': 7, 'eight': 8, 'nine': 9}

    array = s.split(" ")
    numbers = []
    for i in array:
        if i in dictionary:
            numbers.append(dictionary.get(i))
        else:
            return 'n/a'

    result = sum(numbers) / len(numbers)

    for k, v in dictionary.items():
        if v == int(result):
            return k


def encode(st):
    pattern = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    list_of_letters = [letter for letter in st]
    result_letter_list = []
    for letter in list_of_letters:
        if letter in pattern.keys():
            letter = pattern[letter]
            result_letter_list.append(letter)
        else:
            letter = letter
            result_letter_list.append(letter)

    return "".join(result_letter_list)


def decode(st):
    pattern = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    array = [i for i in st]
    result = []
    for i in array:
        if i in pattern.keys():
            i = pattern[i]
            result.append(i)
        else:
            i = i
            result.append(i)

    return "".join(result)


def max_diff(lst):
    if(len(lst) > 0):
        return max(lst) - min(lst)
    else:
        return 0


def max_rot(n):
    finalList = []
    listOfNumbers = []
    stringNumber = str(n)
    for i in stringNumber:
        listOfNumbers.append(i)

    finalList.append(n)

    for i in range(len(listOfNumbers)-1):
        listOfNumbers.insert(len(listOfNumbers), listOfNumbers[i])
        del listOfNumbers[i]
        finalList.append(int("".join(listOfNumbers)))

    return max(finalList)

    def vowel_2_index(string):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    stringList = [char for char in string]
    result = ""
    for index, char in enumerate(stringList):
        if char in vowel_list:
            print(char)
            result = result + str(index+1)
        else:
            result += stringList[index]
    return result

    def pattern(n):
    result = ""

    if n < 0:
        return ""

    for index in range(1, n+1):
        for number in range(index, n+1):
            result += str(number)
        if index < n:
            result += "\n"

    return result


def men_from_boys(arr):
    boys = []
    mens = []

    for i in arr:
        if i % 2 == 0:
            boys.append(i)
        else:
            mens.append(i)
    boys.sort(reverse=False)
    mens.sort(reverse=True)

    return list(dict.fromkeys(boys + mens))
