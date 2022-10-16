def isPalindrome(number: int) -> bool:
    number_to_reverse = number
    reversed_number = 0
    while number > 0:
        a = number % 10
        reversed_number = reversed_number * 10 + a
        number = number // 10
    
    if number_to_reverse == reversed_number:
        return True
    return False
    

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))