
checksum = 0

with open("checksum_sample.txt", "w") as file:
    for line in file:
        line = line.strip()
        values = line.split()
        numbers = []
        for v in values:
            numbers.append(int(v))
        largest = max(numbers)
        smallest = min(numbers)
        difference = largest - smallest
        checksum += difference
        print(difference)
print("Checksum:", checksum)
