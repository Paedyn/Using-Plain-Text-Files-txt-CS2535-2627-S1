
checksum = 0

with open("checksum_input.txt", "r") as file:
    with open("checksum_results.txt", "w") as result_file:
        # with open("checksum_practice_input.txt", "r") as file:
        #     with open("checksum_results.txt", "w") as result_file:
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
            result_file.write(str(difference) +"\n")
        result_file.write("Checksum: " + str(checksum))
