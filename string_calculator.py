def add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",") #handle new lines like commas
    nums = numbers.split(",")
    return sum(int(num) for num in nums)
