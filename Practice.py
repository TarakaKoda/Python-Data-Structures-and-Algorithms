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

class Node3:

    len = -1
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None
        Node3.len += 1


class Doubly_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None

    def create_doubly_linked_list(self, node_value):
        node = Node3(node_value)
        self.head = node
        self.tail = node

    def insert(self, value, location):
        new_node = Node3(value)
        if self.head == None:
            print("doubly linked list does not exist")
        else:
            if location == 0:
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
                new_node.previous = None
            elif location >= Node3.len or location == -1:
                self.tail.next = new_node
                new_node.previous = self.tail
                new_node.next = None
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.previous = temp_node
                new_node.next = next_node
                next_node.previous = new_node

    def traversing(self):
        if self.head == None:
            print("Doubly Linked List does not exist")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next

    def reverse_traversing(self):
        if self.head == None:
            print("Doubly Linked List does not exist")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.previous

    def deletion(self, location):
        if self.head  == None:
            print("Doubly Linked List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.next.previous = None
            elif location >= Node3.len or location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = None
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
                next_node.next.previous = temp_node

    def delete_entire_doubly_linked_list(self):
        if self.head is None:
            print("Doubly Linked List does not exist")
        else:
            self.head = None
            self.tail = None
            print("Doubly Linked List has been Deleted")

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


doubly_linked_list = Doubly_linked_list()

doubly_linked_list.create_doubly_linked_list(2)
doubly_linked_list.insert(1,0)
doubly_linked_list.insert(3,-1)
doubly_linked_list.insert(4,4)
# print([node.value for node in doubly_linked_list])
# doubly_linked_list.traversing()
# doubly_linked_list.reverse_traversing()
doubly_linked_list.deletion(1)
doubly_linked_list.deletion(-1)
doubly_linked_list.deletion(-1)
# print([node.value for node in doubly_linked_list])
# doubly_linked_list.delete_entire_doubly_linked_list.()
# doubly_linked_list.delete_entire_doubly_linked_list()

class Node4:

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


class Circular_Doubly_Linked_List:

    def __inti__(self):
        self.head = None
        self.tail = None

    def create_circular_doubly_linked_list(self, node_value):
        node = Node(node_value)
        self.head = node
        self.tail = node
        self.next = node
        self.previous = node

    def insertion(self, value, location):
        new_node = Node(value)
        if self.head == None:
            print("Circular Doubly Linked List does not exist")
        else:
            if location == 0:
                self.head.previous = new_node
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
                new_node.next = self.head
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.previous = temp_node
                new_node.next = next_node
                next_node.previous = new_node

    def traversing(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break

    def reverse_traversing(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.previous
            if node == self.head.previous:
                break

    def searching(self, value):
        if self.head is None:
            print("Circular Doubly Linked List does not exist")
        node = self.head
        while node:
            if node.value == value:
                return print(f"{value} found in the Circular Doubly Linked List")
            node = node.next
            if node == self.tail.next:
                break
        return print(f"{value} does not exist in the Circular Doubly Linked List")

    def delete(self, location):
        if self.head is None:
            print("Circular Doubly Linked List does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.next = None
                    self.previous = None
                else:
                    self.head = self.head.next
                    self.head.next.previous = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.next = None
                    self.previous = None
                else:
                    self.tail = self.tail.previous
                    self.tail.next = self.head
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
                next_node.next.previous = temp_node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

circular_doubly_linked_list = Circular_Doubly_Linked_List()


circular_doubly_linked_list.create_circular_doubly_linked_list(2)
circular_doubly_linked_list.insertion(1, 0)
circular_doubly_linked_list.insertion(0, 0)
circular_doubly_linked_list.insertion(4, -1)
circular_doubly_linked_list.insertion(3, 3)
# print([node.value for node in circular_doubly_linked_list])
# circular_doubly_linked_list.traversing()
# circular_doubly_linked_list.reverse_traversing()
# circular_doubly_linked_list.searching(4)
circular_doubly_linked_list.delete(2)
circular_doubly_linked_list.delete(0)
circular_doubly_linked_list.delete(0)
circular_doubly_linked_list.delete(0)
circular_doubly_linked_list.delete(0)
# print([node.value for node in circular_doubly_linked_list])

# finding the unique numbers in a list/array
def find_unique_numbers(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    unique_list = []
    for num in frequency:
        if frequency[num] == 1:
            unique_list.append(num)
    return unique_list


# print(find_unique_numbers([1,2,3,1,4,3,2]))

# Linked List class
from random import randint
class Node6:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.value)

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        values = [str(node.value) for node in self]
        return "->".join(values)

    def __len__(self):
        result = 0
        temp_node = self.head
        while temp_node:
            result += 1
            temp_node = temp_node.next
        return result

    def add(self, value):
        if self.head is None:
            new_node = Node6(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node6(value)
            self.tail = self.tail.next
        return self.tail
    def generate(self, n ,max_value, min_vlue):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_vlue, max_value))
        return self

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


# remove duplicate values in the linked list

def remove_duplicate(linked_list):
    if linked_list.head is None:
        return
    else:
        current_node = linked_list.head
        unique_value = {current_node.value}

        while current_node.next:
            if current_node.next.value in unique_value:
                current_node.next = current_node.next.next
            else:
                unique_value.add(current_node.next.value)
                current_node = current_node.next
        return linked_list

# without using the temporary buffer
def remove_duplicates(linked_list):
    if linked_list.head is None:
        return
    else:
        current_node = linked_list.head
        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                runner = runner.next
            current_node = current_node.next
        return linked_list


linked_list = Linked_List()

linked_list.generate(10, 99, 1)
# print(linked_list)
# print(len(linked_list))
# print(remove_duplicates(linked_list))
# print(len(remove_duplicate(linked_list)))

# Find nth value from the last using iteration method
def nth_value_from_last(linked_list, n):
    if n > len(linked_list):
        return None
    elif linked_list.head is None:
        return
    else:
        pointer1 = linked_list.head
        pointer2 = linked_list.head

        for _ in range(n):
            pointer2 = pointer2.next
            if pointer2 is None:
                return pointer1

        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1

# print(nth_value_from_last(linked_list, 10))

# finding the nth value from the last using recursion method
def nth_value_last_recursive(linked_list, n):
    if n == 1:
        return linked_list.tail
    else:
        temp_node = linked_list.head
        while temp_node:
            if temp_node.next == linked_list.tail:
                break
            temp_node = temp_node.next
        temp_node.next = None
        linked_list.tail = temp_node
        return nth_value_from_last(linked_list, n-1)

# print(nth_value_last_recursive(linked_list,9))

# partition of  linked list based on value

def partition(linked_list, value):
    if linked_list.head is None:
        return None
    else:
        current_node = linked_list.head
        linked_list.tail = linked_list.head

        while current_node:
            next_node = current_node.next
            current_node.next = None
            if current_node.value < value:
                current_node.next = linked_list.head
                linked_list.head = current_node
            else:
                linked_list.tail.next = current_node
                linked_list.tail = current_node
            current_node = next_node
        if linked_list.tail.next:
            linked_list.tail.next = None
        return linked_list

# print(partition(linked_list,30))

# sum of two linked list

def sum_of_linked_list(linked_list1, linked_list2):
    current_node1 = linked_list1.head
    current_node2 = linked_list2.head
    carry = 0
    result_linked_list = Linked_List()

    while current_node1 or current_node2:
        result = carry
        if current_node1:
            result += current_node1.value
            current_node1 = current_node1.next

        if current_node2:
            result += current_node2.value
            current_node2 = current_node2.next

        result_linked_list.add(int(result % 10))
        carry = result/10
    return result_linked_list


linked_list1 = Linked_List()
linked_list2 = Linked_List()

linked_list1.add(2)
linked_list1.add(1)
linked_list1.add(3)

linked_list2.add(5)
linked_list2.add(9)
linked_list2.add(2)
linked_list2.add(3)

# print(linked_list1)
# print(linked_list2)
# print(sum_of_linked_list(linked_list1, linked_list2))


def intersection(linked_list1, linked_list2):
    if linked_list1.tail is not linked_list2.tail:
        return False

    ll1 = len(linked_list1)
    ll2 = len(linked_list2)

    shorter = linked_list1 if ll1 < ll2 else linked_list2
    longer = linked_list2 if ll1 < ll2 else linked_list1

    difference = len(longer) - len(shorter)

    longer_node = longer.head
    shorter_node = shorter.head

    for _ in range(difference):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next
    return longer_node


# helper function to create a intersection between the two linked list

def adding_insertion_between_linked_list(linked_list1, linked_list2, value):
    new_node = Node6(value)
    linked_list1.tail.next = new_node
    linked_list1.tail = new_node
    linked_list2.tail.next = new_node
    linked_list2.tail = new_node

linked_list_temp1 = Linked_List()
ll1 = linked_list_temp1.generate(4,99,1)

linked_list_temp2 = Linked_List()
ll2 = linked_list_temp2.generate(7,99,2)

adding_insertion_between_linked_list(ll1,ll2, 5)
adding_insertion_between_linked_list(ll1,ll2, 88)

# print(ll1)
# print(ll2)
# print(intersection(ll1,ll2))

# list as a stack

class Stack:

    def __init__(self):
        self.list = []

    def __str__(self):
        if self.list is None:
            return "Stack deleted"
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None

# stack = Stack()
#
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.pop()
# print(stack.peek())
# stack.delete()
# stack.is_empty()
# print(stack)

class Stack_with_maximum_limit:
    def __init__(self, max_value):
        self.max_value = max_value
        self.list = []

    def __str__(self):
        if self.list is None:
            return "Stack is Deleted"
        elif self.list == []:
            return "Stack is empty"
        else:
            values = self.list.reverse()
            values = [str(x) for x in self.list]
            return "\n".join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def is_full(self):
        if len(self.list) == self.max_value:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return "Stack is full"
        else:
            self.list.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        else:
            return self.list.pop()
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None

# stack = Stack_with_maximum_limit(5)
#
# stack.push(9)
# stack.push(12)
# stack.push(8)
# stack.push(4)
# stack.push(6)
# print(stack)
# print(stack.push(1))
# print(stack.pop())
# print(stack.peek())
# print(stack.is_full())
# print(stack.is_empty())
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)

class Node7:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class Linked_List:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack_Using_Linked_List:
    def __init__(self):
        self.linked_list = Linked_List()

    def __str__(self):
        if self.linked_list.head is None:
            return "Stack is empty"
        values = [str(node.value) for node in self.linked_list]
        return "\n".join(values)

    def is_empty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False
    def push(self, value):
        new_node = Node7(value)
        if self.is_empty():
            self.linked_list.head = new_node
            new_node.next = None
        else:
            new_node.next = self.linked_list.head
            self.linked_list.head = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            popped_node = self.linked_list.head
            self.linked_list.head = self.linked_list.head.next
            return popped_node.value

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None

stack = Stack_Using_Linked_List()
# print(stack.is_empty())
# stack.push(1)
# stack.push(10)
# stack.push(11)
# stack.push(90)
# stack.push(99)
# print(stack)
# print("---popped values-----")
# print(stack.pop())
# print(stack.pop())
# print("-----peek value------")
# print(stack.peek())
# print("-----stack-----")
# print(stack)
# stack.delete()
# print(stack)


class Stack_Three_in_One:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack = [0] * (self.number_of_stacks * stack_size)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def is_full(self, stack_number):
        if self.sizes[stack_number] == self.stack_size:
            return True
        else:
            return False

    def is_empty(self, stack_number):
        if self.sizes[stack_number] == 0:
            return True
        else:
            return False

    def index_of_top(self,  stack_number):
        offset = stack_number * self.stack_size
        return offset + self.sizes[stack_number] -1


    def push(self, value,stack_number):
        if self.is_full(stack_number):
            return "Stack is full"
        else:
            self.sizes[stack_number] += 1
            self.stack[self.index_of_top(stack_number)] = value

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return "Stack is empty"
        else:
            value = self.stack[self.index_of_top(stack_number)]
            self.stack[self.index_of_top(stack_number)] = 0
            return value

    def peek(self, stack_number):
        if self.is_empty(stack_number):
            return "Stack is empty"
        else:
            return self.stack[self.index_of_top(stack_number)]

    def __str__(self):
        # value = self.stack.reverse()
        value = [str(values) for values in self.stack]
        return "\n".join(value)


three_in_one_stack = Stack_Three_in_One(3)

# three_in_one_stack.push(4,2)
# three_in_one_stack.push(6,2)
# three_in_one_stack.push(8, 1)
# three_in_one_stack.push(8,0)
# print(three_in_one_stack.peek(0))
# print(three_in_one_stack)

#   Create Stack with min method

class Node8:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        string = self.value
        string += "," + str(self.next)
        return string

class Stack_Min:
    def __init__(self):
        self.top = None
        self.min_node = None

    def min(self):
        if self.min_node is None:
            return None
        else:
            return self.min_node.value

    def push(self, value):
        if self.min_node and (self.min_node.value < value):
            self.min_node = Node8(value=self.min_node.value, next=self.min_node)
        else:
            self.min_node = Node8(value=value, next=self.min_node)
        self.top = Node8(value=value, next=self.top)

    def pop(self):
        if self.top is None:
            return "Stack is empty"
        else:
            self.min_node = self.min_node.next
            top_value = self.top
            self.top = self.top.next
            return top_value


stack_min = Stack_Min()

# if __name__  == "__main__":
#     print(stack_min.min())
#     stack_min.push(9)
#     stack_min.push(5)
#     stack_min.push(3)
#     print(stack_min.min())
#     stack_min.pop()
#     print(stack_min.min())


class Tree_Node:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        result = " " * level + str(self.data) + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result

    def add_child(self, tree_node):
        self.children.append(tree_node)


# tree = Tree_Node("Drinks", [])
# cold = Tree_Node("cold", [])
# hot = Tree_Node("hot", [])
# tree.add_child(cold)
# tree.add_child(hot)
# alcoholic = Tree_Node("Alcoholic", [])
# non_alcoholic = Tree_Node("Non-Alcoholic", [])
# cold.add_child(alcoholic)
# cold.add_child(non_alcoholic)
# tea = Tree_Node("Tea", [])
# coffee = Tree_Node("Coffee", [])
# hot.add_child(tea)
# hot.add_child(coffee)
# beer = Tree_Node("Beer", [])
# wine = Tree_Node("Wine", [])
# whiskey = Tree_Node("Whiskey", [])
# vodka = Tree_Node("Vodka", [])
# alcoholic.add_child(beer)
# alcoholic.add_child(wine)
# alcoholic.add_child(whiskey)
# alcoholic.add_child(vodka)
# soda = Tree_Node("Soda", [])
# cola = Tree_Node("Cola", [])
# fanta = Tree_Node("Fanta", [])
# non_alcoholic.add_child(soda)
# non_alcoholic.add_child(cola)
# non_alcoholic.add_child(fanta)
# print(tree)

class Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_children(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child


# root_node = Binary_Tree("Drinks")
# left_node = Binary_Tree("Hot")
# right_node = Binary_Tree("Cold")
#
# root_node.add_children(left_node, right_node)
#
# left_hot_node = Binary_Tree("Tea")
# right_hot_node = Binary_Tree("Coffee")
#
# left_node.add_children(left_hot_node, right_hot_node)
#
# left_cold_node = Binary_Tree("Soda")
# right_cold_node = Binary_Tree("Cola")
#
# right_node.add_children(left_cold_node, right_cold_node)



# from Queue import Queue

# class Binary_Tree:
#     def __init__(self, data):
#         self.data = data
#         self.left_child = None
#         self.right_child = None
#
#     def add_children(self, left_child, right_child):
#         self.left_child = left_child
#         self.right_child = right_child
#
#
#
# root_node = Binary_Tree("Drinks")
# left_node = Binary_Tree("Hot")
# right_node = Binary_Tree("Cold")
#
# root_node.add_children(left_node, right_node)
#
# left_hot_node = Binary_Tree("Tea")
# right_hot_node = Binary_Tree("Coffee")
#
# left_node.add_children(left_hot_node, right_hot_node)
#
# left_cold_node = Binary_Tree("Soda")
# right_cold_node = Binary_Tree("Cola")
#
# right_node.add_children(left_cold_node, right_cold_node)
#
# # PreOder Traversal: root node -> left child -> right child
# def preOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         print(root_node.data)
#         preOrder_traversal(root_node.left_child)
#         preOrder_traversal(root_node.right_child)
#
# # InOrder Traversal: left child -> root node -> right child
# def inOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         inOrder_traversal(root_node.left_child)
#         print(root_node.data)
#         inOrder_traversal(root_node.right_child)
#
# # PostOrder Traversal: left child -> right child -> root node
# def postOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         postOrder_traversal(root_node.left_child)
#         postOrder_traversal(root_node.right_child)
#         print(root_node.data)
#
# # LevelOrder Traversal: we visit all nodes at a given level before moving to the next level.
# def levelOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         queue = Queue()
#         queue.enqueue(root_node)
#         while not queue.is_empty():
#             root = queue.dequeue()
#             print(root.data)
#             if root.left_child:
#                 queue.enqueue(root.left_child)
#             if root.right_child:
#                 queue.enqueue(root.right_child)
#
#
# # if __name__ == "__main__":
# #     print("PreOrder Traversal:")
# #     preOrder_traversal(root_node)
# #     print("\nInOrder Traversal:")
# #     inOrder_traversal(root_node)
# #     print("\nPostOrder Traversal:")
# #     postOrder_traversal(root_node)
# #     print("\nLevelOrder Traversal:")
# #     levelOrder_traversal(root_node)
#
# '''
# Import queue (using Linked List data structure) as a helper function to levelOrder traversal and searching in  Binary Tree
# '''
# # from Queue import Queue
# class Binary_Tree:
#     def __init__(self, data):
#         self.data = data
#         self.left_child = None
#         self.right_child = None
#
#     def add_children(self, left_child, right_child):
#         self.left_child = left_child
#         self.right_child = right_child
#
#
# root_node = Binary_Tree("Drinks")
# left_node = Binary_Tree("Hot")
# right_node = Binary_Tree("Cold")
#
# root_node.add_children(left_node, right_node)
#
# left_hot_node = Binary_Tree("Tea")
# right_hot_node = Binary_Tree("Coffee")
#
# left_node.add_children(left_hot_node, right_hot_node)
#
# left_cold_node = Binary_Tree("Soda")
# right_cold_node = Binary_Tree("Cola")
#
# right_node.add_children(left_cold_node, right_cold_node)
#
#
# # PreOder Traversal: root node -> left child -> right child
# def preOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         print(root_node.data)
#         preOrder_traversal(root_node.left_child)
#         preOrder_traversal(root_node.right_child)
#
# # InOrder Traversal: left child -> root node -> right child
# def inOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         inOrder_traversal(root_node.left_child)
#         print(root_node.data)
#         inOrder_traversal(root_node.right_child)
#
# # PostOrder Traversal: left child -> right child -> root node
# def postOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         postOrder_traversal(root_node.left_child)
#         postOrder_traversal(root_node.right_child)
#         print(root_node.data)
#
# # LevelOrder Traversal: we visit all nodes at a given level before moving to the next level.
# def levelOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         queue = Queue()
#         queue.enqueue(root_node)
#         while not queue.is_empty():
#             root = queue.dequeue()
#             print(root.data)
#             if root.left_child:
#                 queue.enqueue(root.left_child)
#             if root.right_child:
#                 queue.enqueue(root.right_child)
#
# def searching_node(root_node, value):
#     if not root_node:
#         return
#     queue = Queue()
#     queue.enqueue(root_node)
#     while not queue.is_empty():
#         root = queue.dequeue()
#         if root.data == value:
#             return "Success"
#         if root.left_child:
#             queue.enqueue(root.left_child)
#         if root.right_child:
#             queue.enqueue(root.right_child)
#     return f"{value} does not exit in the Binary Tree"
#
# # if __name__ == "__main__":
# #     levelOrder_traversal(root_node)
# #     print(searching_node(root_node, "Cola"))
# #     print(searching_node(root_node, "Chocolate"))
#
# '''
# Import queue (using Linked List data structure) as a helper function to levelOrder traversal, searching, inserting in  Binary Tree
# '''
# # from Queue import Queue
#
#
# class Binary_Tree:
#     def __init__(self, data):
#         self.data = data
#         self.left_child = None
#         self.right_child = None
#
#     def add_children(self, left_child, right_child):
#         self.left_child = left_child
#         self.right_child = right_child
#
#
# root_node = Binary_Tree("Drinks")
# left_node = Binary_Tree("Hot")
# right_node = Binary_Tree("Cold")
#
# root_node.add_children(left_node, right_node)
#
# left_hot_node = Binary_Tree("Tea")
# right_hot_node = Binary_Tree("Coffee")
#
# left_node.add_children(left_hot_node, right_hot_node)
#
# left_cold_node = Binary_Tree("Soda")
# right_cold_node = Binary_Tree("Cola")
#
# right_node.add_children(left_cold_node, right_cold_node)
#
#
# # PreOder Traversal: root node -> left child -> right child
# def preOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         print(root_node.data)
#         preOrder_traversal(root_node.left_child)
#         preOrder_traversal(root_node.right_child)
#
# # InOrder Traversal: left child -> root node -> right child
# def inOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         inOrder_traversal(root_node.left_child)
#         print(root_node.data)
#         inOrder_traversal(root_node.right_child)
#
# # PostOrder Traversal: left child -> right child -> root node
# def postOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         postOrder_traversal(root_node.left_child)
#         postOrder_traversal(root_node.right_child)
#         print(root_node.data)
#
# # LevelOrder Traversal: we visit all nodes at a given level before moving to the next level.
# def levelOrder_traversal(root_node):
#     if not root_node:
#         return
#     else:
#         queue = Queue()
#         queue.enqueue(root_node)
#         while not queue.is_empty():
#             root = queue.dequeue()
#             print(root.data)
#             if root.left_child:
#                 queue.enqueue(root.left_child)
#             if root.right_child:
#                 queue.enqueue(root.right_child)
#
# def searching_node(root_node, value):
#     if not root_node:
#         return
#     queue = Queue()
#     queue.enqueue(root_node)
#     while not queue.is_empty():
#         root = queue.dequeue()
#         if root.data == value:
#             return "Success"
#         if root.left_child:
#             queue.enqueue(root.left_child)
#         if root.right_child:
#             queue.enqueue(root.right_child)
#     return f"{value} does not exit in the Binary Tree"
#
# def insert_node(root_node, node):
#     if not root_node:
#         root_node.data = node
#         return "New node inserted"
#     else:
#         queue = Queue()
#         queue.enqueue(root_node)
#         while not queue.is_empty():
#             root = queue.dequeue()
#             if root.left_child:
#                 queue.enqueue(root.left_child)
#             else:
#                 root.left_child = node
#                 return "New node has been inserted"
#             if root.right_child:
#                 queue.enqueue(root.right_child)
#             else:
#                 root.right_child = node
#                 return "New node has been inserted"
#
# new_node = Binary_Tree("Biscuit")
#
# if __name__ == "__main__":
#     levelOrder_traversal(root_node)
#     print(insert_node(root_node, new_node))
#     levelOrder_traversal(root_node)

# class Binary_Tree:
#     def __init__(self, size):
#         self.list = [None] * size
#         self.last_used_index = 0
#         self.maximum_size = size
#
#     def insert(self, value):
#         if self.last_used_index+1 == self.maximum_size:
#             return "Tree is full"
#         else:
#             self.list[self.last_used_index+1] = value
#             self.last_used_index += 1
#             return "Successfully inserted"
#
#     def searching(self, value):
#         if self.last_used_index == 0:
#             return "Binary Tree is empty"
#         else:
#             for i in range(1, self.maximum_size):
#                 if self.list[i] == value:
#                     return "Found"
#             return "value does not exist in Binary Tree"
#
#     def preOrder_traversal(self, index):
#         if index > self.last_used_index:
#             return
#         else:
#             print(self.list[index])
#             self.preOrder_traversal(index*2)
#             self.preOrder_traversal(index*2+1)
#
#     def inOrder_traversal(self, index):
#         if index > self.last_used_index:
#             return
#         else:
#             self.inOrder_traversal(index * 2)
#             print(self.list[index])
#             self.inOrder_traversal(index * 2 + 1)
#
#     def postOrder_traversal(self, index):
#         if index > self.last_used_index:
#             return
#         else:
#             self.postOrder_traversal(index * 2)
#             self.postOrder_traversal(index * 2 + 1)
#             print(self.list[index])
#
#     def levelOrder_traversal(self, index):
#         if index > self.last_used_index:
#             return
#         else:
#             for i in range(index, self.last_used_index+1):
#                 print(self.list[i])
#
#     def delete_node(self, value):
#         if self.last_used_index == 0:
#             return "There is not node to delete in binary tree"
#         for i in range(self.last_used_index+1):
#             if self.list[i] == value:
#                 self.list[i] = self.list[self.last_used_index]
#                 self.list[self.last_used_index] = None
#                 self.last_used_index -= 1
#                 return "The node has been successfully deleted"
#
#     def delete_entire_binary_tree(self):
#         self.list = None
#         return "Successfully deleted entire binary tree"
#
#
# binary_tree = Binary_Tree(8)
# binary_tree.insert("Drinks")
# binary_tree.insert("Hot")
# binary_tree.insert("Cold")
# binary_tree.insert("Tea")
# binary_tree.insert("Coffee")
# binary_tree.insert("Soda")
# binary_tree.insert("Cola")
#
#
#     binary_tree.preOrder_traversal(1)
#     binary_tree.inOrder_traversal(1)
#     binary_tree.postOrder_traversal(1)
#     binary_tree.levelOrder_traversal(1)
#     binary_tree.delete_node("Tea")
#     binary_tree.delete_entire_binary_tree()





from Queue import Queue
class Binary_Search_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert(root_node, value):
    if root_node.data is None:
        root_node.data = value
    else:
        if value <= root_node.data:
            if root_node.left_child is None:
                root_node.left_child = Binary_Search_Tree(value)
            else:
                insert(root_node.left_child, value)
        else:
            if root_node.right_child is None:
                root_node.right_child = Binary_Search_Tree(value)
            else:
                insert(root_node.right_child, value)
    return "value successfully inserted"

def preOrder_traversal(root_node):
    if not root_node:
        return
    else:
        print(root_node.data)
        preOrder_traversal(root_node.left_child)
        preOrder_traversal(root_node.right_child)

def inOrder_traversal(root_node):
    if not root_node:
        return
    else:
        inOrder_traversal(root_node.left_child)
        print(root_node.data)
        inOrder_traversal(root_node.right_child)

def postOrder_traversal(root_node):
    if not root_node:
        return
    else:
        postOrder_traversal(root_node.left_child)
        postOrder_traversal(root_node.right_child)
        print(root_node.data)

def levelOrder_traversal(root_node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            root = queue.dequeue()
            print(root.data)
            if root.left_child:
                queue.enqueue(root.left_child)
            if root.right_child:
                queue.enqueue((root.right_child))

def searching(root_node, value):
    if root_node is None:
        print("value does not exist")
    elif root_node.data == value:
        print("Found")
    elif value < root_node.data:
        if root_node.left_child == value:
            print("Found")
        else:
            searching(root_node.left_child, value)
    else:
        if root_node.right_child == value:
            print("Found")
        else:
            searching(root_node.right_child, value)

def minValueNode(bstNode):
    current = bstNode
    while (current.left_child is not None):
        current = current.left_child
    return current

def delete_node(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.left_child = delete_node(rootNode.left_child, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.right_child = delete_node(rootNode.right_child, nodeValue)
    else:
        if rootNode.left_child is None:
            temp = rootNode.right_child
            rootNode = None
            return temp

        if rootNode.right_child is None:
            temp = rootNode.left_child
            rootNode = None
            return temp

        temp = minValueNode(rootNode.right_child)
        rootNode.data = temp.data
        rootNode.right_child = delete_node(rootNode.right_child, temp.data)
    return rootNode


def delete_entire_binary_search_tree(rootNode):
    rootNode.data = None
    rootNode.left_child = None
    rootNode.right_child = None
    return "The BST has been successfully deleted"

binary_search_tree = Binary_Search_Tree(None)

# insert(binary_search_tree, 50)
# insert(binary_search_tree, 60)
# insert(binary_search_tree, 40)
# insert(binary_search_tree, 30)
# insert(binary_search_tree, 80)
# levelOrder_traversal(binary_search_tree)
# delete_node(binary_search_tree, 40)
# levelOrder_traversal(binary_search_tree)
# delete_entire_binary_search_tree(binary_search_tree)
# levelOrder_traversal(binary_search_tree)

from Queue import Queue
class AVL_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

def preOrder_traversal(root_node):
    if not root_node:
        return
    else:
        print(root_node.data)
        preOrder_traversal(root_node.left_child)
        preOrder_traversal(root_node.right_child)

def inOrder_traversal(root_node):
    if not root_node:
        return
    else:
        inOrder_traversal(root_node.left_child)
        print(root_node.data)
        inOrder_traversal(root_node.right_child)

def postOrder_traversal(root_node):
    if not root_node:
        return
    else:
        postOrder_traversal(root_node.left_child)
        postOrder_traversal(root_node.right_child)
        print(root_node.data)

def levelOrder_traversal(root_node):
    if not root_node:
        return
    else:
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            root = queue.dequeue()
            print(root.data)
            if root.left_child:
                queue.enqueue(root.left_child)
            if root.right_child:
                queue.enqueue(root.right_child)

def searching(root_node, value):
    if root_node is None:
        return "not found"
    elif root_node.data == value:
        return "found"
    elif value < root_node.data:
        if root_node.left_child.data == value:
            return "found"
        else:
            searching(root_node.left_child, value)
    else:
        if root_node.right_child.data == value:
            return "found"
        else:
            searching(root_node.right_child, value)

def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def right_rotation(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def left_rotation(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)

def insert(root_node, value):
    if not root_node:
        return AVL_Tree(value)
    elif value <= root_node.data:
        root_node.left_child = insert(root_node.left_child, value)
    else:
        root_node.right_child = insert(root_node.right_child, value)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1 and value < root_node.left_child.data:
        return right_rotation(root_node)
    if balance > 1 and value > root_node.left_child.data:
        root_node.left_child = left_rotation(root_node.left_child)
        return right_rotation(root_node)
    if balance < -1 and value > root_node.right_child.data:
        return left_rotation(root_node)
    if balance < -1 and value < root_node.right_child.data:
        root_node.right_child = right_rotation(root_node.right_child)
        return left_rotation(root_node)
    return root_node

def minimum_value(root_node):
    current = root_node
    while current.left_child:
        current = current.left_child
    return current

def delete(root_node, value):
    if not root_node:
        return
    elif value < root_node.data:
        root_node.left_child = delete(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete(root_node.right_child, value)
    else:
        if root_node.left_child is None:
            return root_node.right_child
        if root_node.right_child is None:
            return root_node.left_child

        temp = minimum_value(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete(root_node.right_child, temp.data)

        balance = get_balance(root_node)

        if balance > 1 and get_balance(root_node.left_child) >= 0:
            return right_rotation(root_node)
        if balance < -1 and get_balance(root_node.right_childd) <= 0:
            return left_rotation(root_node)
        if balance > 1 and get_balance(root_node.left_child) < 0:
            root_node.left_child = left_rotation(root_node.left_child)
            return right_rotation(root_node)
        if balance < -1 and get_balance(root_node.right_child) > 0:
            root_node.right_child = right_rotation(root_node.right_child)
            return right_rotation(root_node)
        return root_node

def delete_entire_avl_tree(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "AVL Tree has been deleted"

avl_tree = AVL_Tree(5)

# if __name__ == "__main__":
#     avl_tree = insert(avl_tree, 10)
#     avl_tree = insert(avl_tree, 20)
#     avl_tree = insert(avl_tree, 40)
#     avl_tree = insert(avl_tree, 50)
#     avl_tree = insert(avl_tree, 60)
#     avl_tree = insert(avl_tree, 80)
#     delete(avl_tree, 60)
#     # avl_tree = insert(avl_tree, 60)
#     levelOrder_traversal(avl_tree)
#     print(delete_entire_avl_tree(avl_tree))
#     levelOrder_traversal(avl_tree)

class Bubble:

    @staticmethod
    def sort(array, reverse=False):
        if not array:
            return None
        if len(array) == 1:
            return array
        elif not reverse:
            for i in range(len(array)):
                for j in range(len(array)-i-1):
                    if array[j] > array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]

        else:
            for i in range(len(array)):
                for j in range(len(array)-i-1):
                    if array[j] < array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
        return array

    @staticmethod
    def optimized(array, reverse=False):
        if array is None:
            return None
        if len(array) == 1:
            return array
        swap = False
        if reverse is False:
            for i in range(len(array)):
                for j in range(len(array)-i-1):
                    if array[j] > array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
                        swap = True
                if not swap:
                    break
        else:
            for i in range(len(array)):
                for j in range(len(array)-i-1):
                    if array[j] < array[j+1]:
                        array[j], array[j+1] = array[j+1], array[j]
                        swap = True
                if not swap:
                    break
        return array
    @staticmethod
    def recursive(array, n=None):
        if n == None:
            n = len(array)
        if n == 1:
            return array
        swap = False
        for i in range(n-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] =  array[i + 1], array[i]
                swap = True
        if swap is None:
            return
        Bubble.recursive(array, n-1)


numbers = [9,5,6,4,3,2,8,1,7]

# if __name__ == "__main__":
#     print(Bubble.sort(numbers, True))
#     print(Bubble.optimized(numbers, True))
#     Bubble.recursive(numbers)
#     print(numbers)

class Selection:
    @staticmethod
    def sort(array, reverse=False):
        if len(array) == 1:
            return array
        elif not reverse:
            for i in range(len(array)):
                minimum_value = i
                for j in range(i+1, len(array)):
                    if array[minimum_value] > array[j]:
                        minimum_value = j
                array[i] , array[minimum_value] = array[minimum_value], array[i]
        else:
            for i in range(len(array)):
                minimum_value = 1
                for j in range(i+1, len(array)):
                    if array[minimum_value] < array[j]:
                        minimum_value = j
                array[i],  array[minimum_value], = array[minimum_value], array[i]
        return array

numbers = [2,3,1,4,6,5,7,9,8]

if __name__ == "__main__":
    print(Selection.sort(numbers, True))












