# for questions see the respective pdf

# q1
def max_2():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    max_num = max(num1, num2)
    print(max_num)
    return max_num

# max_2()

# q2
def max_3():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    num3 = float(input('Enter third number: '))
    max_num = max(num1, num2, num3)
    print(max_num)
    return max_num

# max_3()

# q3
def neg_zero_pos():
    num = float(input('Enter your number: '))
    val = 'Negative' if num<0 else 'Zero' if num==0 else 'Positive'
    print(val)
    return(val)
# neg_zero_pos()

# q4
def devisible_511():
    num = int(input('Enter your number: '))
    res = 'Yes' if num%5==0 or num%11==0 else 'No'
    print(res)
    return(res)

# devisible_511()

# q5
def even_odd():
    num = int(input('Enter your number: '))
    res = 'Even' if num%2==0 else 'Odd'
    print(res)
    return(res)

# even_odd()

#  q6
def is_leap_year():
    year = int(input('Enter year: '))
    if year%400==0:
        res = True
    elif year%100==0:
        res = False
    elif year%4==0:
        res = True
    else:
        res = False

    print('{} is a leap year.'.format(year) if res else '{} is not a leap year.'.format(year))
    return res

# is_leap_year()

# q7
def is_alphabet():
    letter = input('Enter character: ')

    # res = letter.isalpha() #1

    res = True if letter.lower() >= 'a' and letter.lower() <= 'z' else False #2

    print(f'{letter} is alphabet.' if res else f'{letter} is not alphabet.')
    return res

# is_alphabet()

# q8
def consonent_vowel():
    letter = input('Enter letter: ')

    res = 'Vowel' if letter.lower() in 'aeiou' else 'Consonent'

    print(f'{letter} is a {res}.')

# consonent_vowel()

# q9
def alpha_dig_char():
    char = input('Enter character: ')

    res = 'Alphabet' if char.isalpha() else 'Digit' if char.isdigit() else 'Special Character'

    print(f'{char} is a {res}.')

# alpha_dig_char()

# q10
def upper_lower():
    word = input('Enter word: ')

    res = 'Upper' if word.isupper() else 'Lower' if word.islower() else 'Mix'

    print(res)
    return res

# upper_lower()

# q11
def list_elm(lst):
    for elm in lst:
        print(elm)

# list_elm([1, 2, 3, 4, 5])

# q12
def neg_elm(lst):
    neg_lst = [i for i in lst if i<0]
    for elm in neg_lst:
        print(elm)

# neg_elm([1, -2, 3, -4, 5])

# q13   
def sum_list(lst):
    res = sum(lst)
    print(res)

# sum_list([1, -2, 3, -4, 5])

# q14
def list_min_max(lst):
    list_min = min(lst)
    list_max = max(lst)
    print(f"Minimum Value in List: {list_min}")
    print(f"Maximum Value in List: {list_max}")

# list_min_max([1, -2, 3, -4, 5])

# q15
def list_max2(lst):
    sorted_list = sorted(lst)
    print(f'Second Maximum Element is: {sorted_list[-2]}')

# list_max2([1, -2, 3, 4, 5])

# q16
def list_even_odd(lst):
    lst_even = [i for i in lst if i%2==0]
    lst_odd = [i for i in lst if i%2!=0]
    print('Total Even items in the list: ', len(lst_even))
    print('Total Odd items in the list: ', len(lst_odd))

# list_even_odd([1, 2, 3, 4, 5])

# q17
def list_negs(lst):
    neg_list = [i for i in lst if i<0]
    print('Number of negative numbers in the list: ', len(neg_list))

# list_negs([1, -2, -1, 3, -4, 5])

# q18
def list_uniques(lst):
    list_unique = list(set(lst))
    print('Uniques items in the list are: ', list_unique)

# list_uniques([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

# q19
def elm_freq(lst):
    item_freq = {i:lst.count(i) for i in lst}
    for item in item_freq:
        print(f'Frequency of {item} is: {item_freq[item]}')

# elm_freq([1, 2, 2, 3, 4, 5, 1, 2, 3, 4, 5])



def cpc1():
    q = int(input('Enter the question number to check the function: '))
    
    # match-case is implemented in python v3.10 and onwards
    # match q:
    #     case 1:
    #         max_2()
    #     case 2:
    #         max_3()
    #     case 3:
    #         neg_zero_pos()
    #     case 4:
    #         devisible_511()
    #     case 5:
    #         even_odd()
    #     case 6:
    #         is_leap_year()
    #     case 7:
    #         is_alphabet()
    #     case 8:
    #         consonent_vowel()
    #     case 9:
    #         alpha_dig_char()
    #     case 10:
    #         upper_lower()
    #     case 11:
    #         lst = [1, 2, 3, 4, 5]
    #         print('Given List: ', lst)
    #         list_elm(lst)
    #     case 12:
    #         lst = [-1, -2, -3, -4, -5]
    #         print('Given List: ', lst)
    #         neg_elm(lst)
    #     case 13:
    #         lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #         print('Given List: ', lst)
    #         sum_list(lst)
    #     case 14:
    #         lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #         print('Given List: ', lst)
    #         list_min_max(lst)
    #     case 15:
    #         lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #         print('Given List: ', lst)
    #         list_max2(lst)
    #     case 16:
    #         lst = [1, 2, 3, 4, 5]
    #         print('Given List: ', lst)
    #         list_even_odd(lst)
    #     case 17:
    #         lst = [1, -2, 3, -4, 5]
    #         print('Given List: ', lst)
    #         list_negs(lst)
    #     case 18:
    #         lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    #         print('Given List: ', lst)
    #         list_uniques(lst)
    #     case 19:
    #         lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    #         print('Given List: ', lst)
    #         elm_freq(lst)
    #     case _:
    #         print('Program Aborted.')
    # return(q)   


    if q == 1:
        max_2()
    elif q == 2:
        max_3()
    elif q == 3:
        neg_zero_pos()
    elif q == 4:
        devisible_511()
    elif q == 5:
        even_odd()
    elif q == 6:
        is_leap_year()
    elif q == 7:
        is_alphabet()
    elif q == 8:
        consonent_vowel()
    elif q == 9:
        alpha_dig_char()
    elif q == 10:
        upper_lower()
    elif q == 11:
        lst = [1, 2, 3, 4, 5]
        print('Given List: ', lst)
        list_elm(lst)
    elif q == 12:
        lst = [-1, -2, -3, -4, -5]
        print('Given List: ', lst)
        neg_elm(lst)
    elif q == 13:
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print('Given List: ', lst)
        sum_list(lst)
    elif q == 14:
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print('Given List: ', lst)
        list_min_max(lst)
    elif q == 15:
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print('Given List: ', lst)
        list_max2(lst)
    elif q == 16:
        lst = [1, 2, 3, 4, 5]
        print('Given List: ', lst)
        list_even_odd(lst)
    elif q == 17:
        lst = [1, -2, 3, -4, 5]
        print('Given List: ', lst)
        list_negs(lst)
    elif q == 18:
        lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
        print('Given List: ', lst)
        list_uniques(lst)
    elif q == 19:
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        print('Given List: ', lst)
        elm_freq(lst)
    else :
        print('Program Aborted.')     

cpc1()