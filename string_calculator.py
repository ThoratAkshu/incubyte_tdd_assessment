def add(numbers):
    if numbers == "":
        return 0
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
        nums = numbers.split(delimiter) #support custom delimiters
    else:
        numbers = numbers.replace("\n", ",")
        nums = numbers.split(",")
    return sum(int(num) for num in nums)
