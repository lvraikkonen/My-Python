# 1 is_even
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print is_even(3)
print is_even(4)


# 2 is_int
import math

def is_int(x):
    diff = x - math.floor(x)
    if diff > 0:
        return False
    else:
        return True

print is_int(7.0)   # True
print is_int(7.5)   # False
print is_int(-1)    # True 


# 3 digit_sum
def digit_sum(n):
    sum = 0
    str_num = str(n)
    for num in str_num:
        sum += int(num)
    return sum

print digit_sum(1234)


# 4 factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print factorial(3)


# 5 is_prime
def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2,x):
            if x % n == 0:
                return False
        else:
            return True

print is_prime(1)
print is_prime(2)
print is_prime(3)
print is_prime(9)


# 6 reverse
def reverse(text):
    if len(text) == 1:
        return text
    else:
        return reverse(text[1:]) + text[0]

print reverse("Python!")

#6 reverse
def reverse(text):
    i = len(text) - 1
    new = []
    while i >= 0:
        new.append(text[i])
        i -= 1
    return ''.join(new)

print reverse("Python!")


# 7 anti_vowel
def anti_vowel(text):
    vowels = "aeiou"
    new = []
    for i in text:
        if i.lower() not in vowels:
            new.append(i)
    return ''.join(new)

print anti_vowel("Hey You!")


# 8 scrabble_score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    keys = []
    for w in word:
        keys.append(w.lower())
    for key in keys:
        total += score[key]
    return total

print scrabble_score("Helix")


# 9 censor
def censor(text,word):
    asterisks_num = len(word)

    tmlist = text.split(" ")
    for i in tmlist:
        if i == word:
            ## because it changes the value may be the same
            tmlist[tmlist.index(i)] = "*" * asterisks_num

    return " ".join(tmlist)

print censor("this hack is wack hack", "hack")


# 10 count
def count(sequence,item):
    result = 0
    for i in sequence:
        if i == item:
            result += 1
    return result

print count([1,2,1,1],1)


# 11 purify
def purify(lst):
    new = []
    for i in lst:
        if i % 2 ==0:
            new.append(i)
    return new

print purify([1,2,3])


## 12 product
def product(lst):
    result = 1
    for i in lst:
        result *= i
    return result

print product([4,5,5])

lst = []

# 13 remove_duplicates
def remove_duplicates(lst):
    new = []
    for item in lst:
        if item not in new:
            new.append(item)
    return new

print remove_duplicates([1,1,2,2,4])


 14 median
def median(lst):
    result = 0
    lst = sorted(lst)
    length = len(lst)
    if length % 2 == 0:
        result = (lst[length/2 - 1] + lst[length/2])/2.0
    else:
        result = lst[length/2]
    return result

print median([1,1,2])
