def add(numbers):
    #handle empty string returning 0
    if numbers == "":
        return 0
    #handle one number
    nums = numbers.split(",")
    #handle two numbers
    return sum(int(num) for num in nums) 
