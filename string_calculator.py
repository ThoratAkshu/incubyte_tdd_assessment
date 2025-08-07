def add(numbers):
    if numbers == "":
        return 0
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
        nums = numbers.split(delimiter)
    else:
        numbers = numbers.replace("\n", ",")
        nums = numbers.split(",")
    # throw exception on negative numbers
    negatives = [num for num in nums if int(num) < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(negatives)}")
    return sum(int(num) for num in nums)
