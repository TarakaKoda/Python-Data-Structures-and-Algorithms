# Factorial using recursion method
def factorial(n: int):
    assert n > 0 and int(n) == n, "n must be positive integer"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))


# Factorial using iteration (for loop)
def fact(n: int) -> int:
    assert n >=0 and int(n) == n,"n must be positive integer"
    result = 1
    for i  in range(1, n+1):
        result *= i
    return result

# print(fact(10))


def fibonacci(n: int):
    a,b = 0,1
    for _ in range(n):
        print(b)
        a,b = b, a+b
# fibonacci(5)

def recursive_fibonacci(n: int) -> int:
    assert n >=0 and int(n) == n, "fibonacci number cannot be negative or non integer"
    if n in [1,0]:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# print(recursive_fibonacci(6))

def sum_of_digits(n):
    assert n >=0 and int(n) == n,"n must be positive integer only!"
    if n in [1,0]:
        return n
    else:
        return n%10 + sum_of_digits(int(n/10))

# print(sum_of_digits())

def power(base,exp):
    assert exp >= 0 and int(exp) == exp, "base must be positive integer only!"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base,exp-1)

# print(power(3, 4))

def gcd(a,b):
    assert int(a)==a and int(b)==b, "The numbers must be integers only!"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

# print(gcd(12, 3))

def decimal_to_binary(n:int | float) -> int | float:
    assert int(n) == n, f"the parameter {n} must be an integer only!"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimal_to_binary(int(n/2))


# print(decimal_to_binary(1.5))

def flatten(arr):
    resultarr = []
    for custItem in arr:
        if isinstance(custItem, list):
            resultarr.extend(flatten(custItem))
        else:
            resultarr.append(custItem)
    return resultarr


# print(flatten([1,2,3, [4,5],[[[6,7,8,[9]]]]]))

def recursive_range(n):
    if n == 0:
        return 0
    else:
        n + recursive_range(n-1)

# print(recursive_range(4))

def recursive_range_step(start, stop, step=1):
    if start >= stop:
        return []
    else:
        return [start] + recursive_range_step(start+step, stop, step)

# print(recursive_range_step(-1, 10, 2))


# product of the array

def product_of_arr(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * product_of_arr(arr[1:])

# print(product_of_arr([1,4,5]))


def is_palindrome(string):
    if len(string) == 0:
        return True
    if string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])


# print(is_palindrome("malayalam"))

def calculating_power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * calculating_power(base, exp-1)

# print(calculating_power(2,5))

def captalize_first(arr):
    result = []
    if len(arr) == 0:
        return result
    else:
        result.append(arr[0][0].upper() + arr[0][1:])
        return result + captalize_first(arr[1:])

# print(captalize_first(["srinu", "pavan", "naruto"]))


def some_recursive(arr, cb):
    if len(arr) == 0:
        return False
    if not (cb(arr[0])):
        return some_recursive(arr[1:], cb)
    return True

def is_odd(num):
    if num%2 == 0:
        return False
    else:
        return True

# print(some_recursive([6,4,2], is_odd))


def factorial_num(num):
    if num < 1:
        return 1
    else:
        return num * factorial_num(num-1)

# print(factorial_num(5))

def reverse(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + reverse(string[:-1])

# print(reverse("srinu"))

def captilize_words(arr):
    result = []
    if len(arr) == 1:
        return [arr[0].upper()]
    else:
        result.append(arr[0].upper())
        return result + captilize_words(arr[1:])

# print(captilize_words(["i", "am", "srinu"]))


def fibonacci_series(num):
    assert int(num) == num and num >= 0, "num must be an positive integer only!"
    if num in [1,0]:
        return num
    else:
        return fibonacci_series(num-1) + fibonacci_series(num-2)

# print(fibonacci_series(5))


def stringify_number(obj):
    new_obj = obj
    for key in new_obj:
        if isinstance(new_obj[key], int):
            new_obj[key] = str(new_obj[key])
        if isinstance(new_obj[key], dict):
            new_obj[key] = stringify_number(new_obj[key])
    return new_obj




obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

# print(stringify_number(obj))

def collect_string(obj):
    result = []
    for key in obj:
        if isinstance(obj[key], str):
            result.append(obj[key])
        else:
            if isinstance(obj[key], dict):
                return result + collect_string(obj[key])

    return result

obj1 = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

# print(collect_string(obj1))


def nested_even_sum(obj):
    result = 0
    for key in obj:
        if isinstance(obj[key], int):
            if obj[key]%2 == 0:
                result+= obj[key]
        else:
            if isinstance(obj[key], dict):
                result += nested_even_sum(obj[key])
    return result

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 2,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

# print(nested_even_sum(obj2))


# factorial

def factorial1(num):
    assert num >= 0 and int(num) == num, "num must be a positive integer only!"
    if num in [1,0]:
        return num
    return num * factorial(num-1)

# print(factorial1(5))

# fibonacci
def fibonacci_series1(num):
    if num in [1, 0]:
        return num
    else:
        return fibonacci_series1(num-1) +fibonacci_series1(num-2)

# print(fibonacci_series1(6))

# sum of two digits

def SumOfDigits(num):
    assert num >= 0 and int(num) == num, "num must ba an positive integer only!"
    if num <= 1:
        return num
    else:
        return num%10 + SumOfDigits(int(num/10))

# print(SumOfDigits(11))

# power

def power1(base, exp):
    assert exp >= 0 and int(exp) == exp, "exp must be positive integer only!"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power1(base, exp-1)

# print(power1(2, 5))

# greatest common divisor

def greatest_common_divisor(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a%b)

# print(greatest_common_divisor(0, -24))

# decimal to binary

def decimal_to_binary1(num):
    assert num >= 0 and int(num) == num, "num must be a positive integer only!"
    if num == 0:
        return 0
    else:
        return num%2 + 10 * decimal_to_binary1(int(num/2))

# print(decimal_to_binary1(10))

# power

def pow(base, exp):
    assert exp >= 0 and int(exp) == exp, "exp must be an positive integer only!"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * pow(base, exp-1)

# print(pow(3,3))

# factorial

def facto(num):
    assert num >= 0 and int(num) == num, "num must be an positive integer only!"
    if num in [1,0]:
        return num
    else:
        return num * facto(num-1)

# print(facto(5))

# product of array

def poa(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] * poa(arr[1:])

# print(poa([1,2,4]))

# recursive range

def recursive_range1(num):
    assert num >= 0 and int(num) == num, "num must be positive integer only!"
    if num == 0:
        return num
    else:
        return num + recursive_range1(num-1)

# print(recursive_range1(4))

# printing the range of numbers using recursion

def range_of_numbers(start, stop, step=1):
    if start >= stop:
        return []
    else:
        return [start] + range_of_numbers(start+step, stop, step)

# print(range_of_numbers(1, 10, 2))

# fibonacci

def fib(num):
    assert num >= 0 and int(num) == num,"num must be positive integer only!"
    if num in [1,0]:
        return num
    else:
        return fib(num-1) + fib(num-2)

# print(fib(4))

# reverse

def reverse1(string):
    if len(string) == 1:
        return string[0]
    else:
        return string[-1] + reverse1(string[:-1])

# print(reverse1("srinu"))

# is palindrome or not

def isPalindrome(string):
    if len(string) == 1:
        return True
    if string[0] != string[-1]:
        return False
    else:
        return isPalindrome(string[1:-1])

# print(isPalindrome("markram"))

# some recursive using call back function

def someRecursive(arr, cb):
    if len(arr) < 1:
        return False
    if not(cb(arr[0])):
        return some_recursive(arr[1:], cb)
    else:
        return True

def isodd(num):
    if num%2 != 0:
        return True
    else:
        return False

# print(someRecursive([2,6,4], isodd))


# flatten

def flatten1(arr):
    result = []
    if len(arr) < 0:
        return []
    for items in arr:
        if isinstance(items, list):
            result.extend(flatten(items))
        else:
            result.append(items)
    return result

# print(flatten1([1,2,[3,4,5],[6]]))

# capitalize first

def capitalize_first1(arr):
    result = []
    if len(arr) == 1:
        result.append(arr[0][0].upper())
    else:
        result.append(arr[0][0].upper())
        return result + captalize_first(arr[1:])
    return result

# print(capitalize_first1(["i", "am", "srinu"]))


# nested even sum

def nested_even_sum1(obj):
    result = 0
    new_obj = obj
    for key in new_obj:
        if isinstance(new_obj[key], int):
            if new_obj[key]%2 == 0:
                result += new_obj[key]
        if isinstance(new_obj[key], dict):
            result += nested_even_sum1(new_obj[key])
    return result

# print(nested_even_sum1(obj2))

# capitalize the first word in an array of strings

def capitalize_word(arr):
    result = []
    if len(arr) == 1:
        result.append(arr[0].upper())
    else:
        result.append(arr[0].upper())
        return result + capitalize_word(arr[1:])
    return result

# print(capitalize_word(["srinu", "pavan", "naruto"]))

# stringify number

def string_to_number(obj):
    new_obj = obj
    for key in new_obj:
        if isinstance(new_obj[key], str):
            new_obj[key] = int(new_obj[key])
        else:
            if isinstance(new_obj[key], dict):
                new_obj[key] = string_to_number(new_obj[key])
    return new_obj

# print(string_to_number(obj))

def collect_string1(obj):
    result = []
    new_obj = obj
    for key in new_obj:
        if isinstance(new_obj[key], str):
            result.append(new_obj[key])
        else:
            if isinstance(new_obj[key], dict):
                return result + collect_string(new_obj[key])
    return result

# print(collect_string1(obj1))

def product_and_sum(arr):
    sum, product = 0, 1
    if len(arr) == 1:
        return print(arr)
    else:
        for items in arr:
            sum += items
            product *= items

        print(f"sum of arr: {sum} and product of array: {product} time complexity is: O(n)")

# product_and_sum([1,2,4])

def maximum_number(arr, n):  # n is the length of the array
    if n == 1:
        return arr[0]
    else:
        return max(arr[n-1], maximum_number(arr, n-1))

# print(maximum_number([1,2,3], 3))

from array import *

arr1 = array("i", [1,2,3,4,5])
arr2 = array("d", [1.5, 1.6, 1.7])

arr1.insert(5,7)
# print(arr1)

def access_element(array, index):
    if index >= len(array):
        return f"This index does not have any value"
    else:
        return array[index]

# print(access_element(arr1, 1))


def searching_element(array, element):
    for i in array:
        if i == element:
            return array.index(i)
    return "element does not exit in the array"

# print(searching_element(arr1, 5))
# print(arr1)

def traverse_array(array):
    for i in array:
        print(i)

# print(traverse_array([1,2,3,4,5]))

import numpy as np

def searching_element_in_two_d_array(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f"{value} found at {i} {j}"

two_d_array = np.array([[1,2,3,4], [5,6,7,8]])

# print(searching_element_in_two_d_array(two_d_array, 8))


def traverse_using_loop(list):
    for i in list:
        print(i, end=" ")

def traverse_using_recursion(list):
    if len(list) == 1:
        print(list[0])
    else:
        print(list[0])
        traverse_using_recursion(list[1:])


# traverse_using_recursion(["milk", "cheese", "butter"])
# traverse_using_loop(["milk", "cheese", "butter"])

def searching_in_list(list, value):
    for i in list:
        if i == value:
            return "value found"
    return "value not found"

# print(searching_in_list([1,2,3,4,5], 4))

def calculating_average():
    list = []
    while True:
        num = input("Enter The Number: ")
        if num.lower() == "done":
            break
        else:
            list.append(int(num))
    average = sum(list)/len(list)
    return f"Average: {average}"

# print(calculating_average())

def calculating_temperature():
    num = int(input("How many day's temperature? "))
    my_list = []
    for i in range(1, num+1):
        temp =int(input(f"Enter the maximum temperature of Day {i}: "))
        my_list.append(temp)
    average = round(sum(my_list)/num, 2)
    above_average = 0
    for i in my_list:
        if i > average:
            above_average += 1
    return f"Average: {average}\n{above_average} day(s) are above average temperature"

# print(calculating_temperature())

# missing number

def missing_number(list):
    sum1 = (len(list)+1) * (len(list)+2) / 2
    sum2 = sum(list)
    return int(sum1 - sum2)

my_list = [x for x in range(1, 101)]
my_list.remove(73)
# print(missing_number(my_list))


def maximum_product_two_integers(array):
    max = 0
    pairs = ""
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > max:
                max = array[i] * array[j]
                pairs = f"{array[i]}, {array[j]}"
    print(pairs)
    return max

my_array = np.array([1,25,65,3,2,4,5,9,8,44,2,5,24,69])
    
# print(maximum_product_two_integers(my_array))

def is_unique(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
        else:
            print(i)
            return False
    return True

my_list = [1,2,3,4,5,6,6,7,7,8]
unique_list = [1,2,3,4,5,6,7,8]

# print(is_unique(my_list))

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

my_list_string = ['a', 'b', 'c', 'd']
my_list_string1 = ["d", "b", "e", "a"]

# print(permutation(my_list_string, my_list_string1))

my_array2 = np.array([[1,2,3,4], [4,5,6,7],[7,8,9,10],[11,12,13,14]])

# print(my_array2)


def rotate(array):
    n = len(array)
    for layer in range(n//2):
        first = layer
        last = n-1-layer
        for i in range(first, last):
            top = array[layer][i]
            array[layer][i] = array[-i-1][layer]
            array[-i-1][layer] = array[-layer-1][-i-1]
            array[-layer-1][-i-1] = array[i][-layer-1]
            array[i][-layer-1] = top
    return array


# print(rotate(my_array2))

# Creating a singly linked list

class Node:

    def __init__(self, value=None):
        self.value = value
        self.next = None

class Singly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def inserting(self,value, location):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def traversing(self):
        if self.head == None:
            print("Singly Linked List does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def searching(self, value):
        node = self.head
        while node:
            if node.value == value:
                return f"{value} found in the Singly LInked List"
            else:
                node = node.next
        return f"{value} does not exist in the Singly Linked List"

    def deletion(self, location):
        if self.head == None:
            return print("The Singly Linked List is Empty")
        else:
            if location == 0:
                if self.head.next == None:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head.next ==  None:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next =  next_node.next

    def delete_entire_Singly_Linked_List(self):
        if self.head == None:
            print("Singly Linked List does not exist")
        else:
            self.head = None
            self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next



# singly_linked_list = Singly_Linked_List()

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
#
# singly_linked_list.head = node1
# singly_linked_list.head.next = node2
# singly_linked_list.head.next.next = node3
# singly_linked_list.tail = node3
# singly_linked_list.inserting(2,0)
# singly_linked_list.inserting(3,-1)
# singly_linked_list.inserting(4,-1)
# singly_linked_list.inserting(1,2)
# singly_linked_list.inserting(1,3)
# singly_linked_list.inserting(3,4)
# singly_linked_list.inserting(2,1)
# print([node.value for node in singly_linked_list])
# # print(singly_linked_list.searching(9))
# singly_linked_list.deletion(-1)
# singly_linked_list.deletion(0)
# singly_linked_list.deletion(-1)
# singly_linked_list.deletion(1)
# singly_linked_list.delete_entire_Singly_Linked_List()
# print([node.value for node in singly_linked_list])



class Node1:

    def __init__(self, value=None):
        self.value = value
        self.next = None

class Singly_Linked_List1:

    def __init__(self):
        self.head = None
        self.tail = None

    def creating_singly_linked_list(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = None
            print(f"singly linked list has been created with node value: {value}")

        else:
            print("singly linked list already exist use insert method to insert more nodes")

    def insert(self, value, location):
        new_node = Node1(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                self.tail.next = new_node
                self.tail = new_node
                new_node.next = None
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next

    def search(self, value):
        if self.head.value == value:
            return f"{value} found at first node of the singly linked list"
        elif self.tail.value == value:
            return f"{value} found at last node of the singly linked list"
        else:
            position = 1
            temp_node = self.head
            while temp_node:
                if temp_node.value == value:
                    return f"{value} fount at {position} node of the singly linked list"
                temp_node = temp_node.next
                position += 1
            return f"{value} does not exist in singly linked list"


    def delete_node(self, location):
        if self.head is None:
            return f"singly linked list is empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp_node = self.head
                    while temp_node:
                        if temp_node.next == self.tail:
                            break
                        temp_node = temp_node.next
                    self.tail = temp_node
                    temp_node.next = None
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next



singly_linked_list = Singly_Linked_List1()

# singly_linked_list.creating_singly_linked_list(2)
singly_linked_list.insert(1,0)
singly_linked_list.insert(3,-1)
singly_linked_list.insert(5,-1)
singly_linked_list.insert(4,3)
# singly_linked_list.traverse()
# print(singly_linked_list.search(1))
# print(singly_linked_list.search(6))
# print([node.value for node in singly_linked_list])
# singly_linked_list.delete_node(3)
# print([node.value for node in singly_linked_list])

class Node2:

    def __init__(self, value=None):
        self.value = value
        self.next = None

class Circular_Singly_Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def create_circular_linked_list(self, value):
        node = Node1(value)
        self.head = node
        self.tail = node
        node.next = node

    def insert(self, value, location):
        new_node = Node1(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            # print(f"Circular Singly Linked List is does not exist,So first node is created with value: {value}")
        else:
            if location == 0:
                new_node.next = self.head
                self.tail.next = new_node
                self.head = new_node
            elif location == -1:
                self.tail.next = new_node
                new_node.next = self.head
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node =temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node

    def traversing(self):
        if self.head is None:
            print("Circular Singly Linked List is empty")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node.next == self.tail.next:
                    break
                temp_node = temp_node.next

    def searching(self, value):
        if self.head is None:
            return f"Circular Singly LInked List does not exist"
        else:
            temp_node = self.head
            position = 0
            while temp_node:
                if temp_node.value == value:
                    return f"{value} is found in {position} Circular Singly Linked List"
                temp_node = temp_node.next
                position += 1
                if temp_node == self.tail.next:
                    return f"{value} does not exist in Circular Singly Linked List"

    def deletion(self, location):
        if self.head is None:
            print("Circular Singly Linked List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp_node = self.head
                    while temp_node:
                        if temp_node.next == self.tail:
                            break
                        temp_node = temp_node.next
                    temp_node.next = self.head
                    self.tail = temp_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next

    def delete_entire_circular_singly_linked_list(self):
        if self.head is None:
            print("Circular Linked List is not exist")
        else:
            self.head = None
            self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next

circular_singly_inked_list = Circular_Singly_Linked_List()

circular_singly_inked_list.insert(2,0)
circular_singly_inked_list.insert(3,-1)
circular_singly_inked_list.insert(1,0)
circular_singly_inked_list.insert(1,0)
# print([node.value for node in circular_singly_inked_list])
# circular_singly_inked_list.traversing()
# print(circular_singly_inked_list.searching(2))
# circular_singly_inked_list.deletion(2)
# circular_singly_inked_list.delete_entire_circular_singly_linked_list()
# print([node.value for node in circular_singly_inked_list])
# circular_singly_inked_list.delete_entire_circular_singly_linked_list()











