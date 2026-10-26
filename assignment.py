# You can remove 'pass' if you written code in the function
# Exercise 1
def write_shopping_list(items, filename):
    file = open(filename,"w")
    c=1
    for i in items:
        file.write(f"{c}. {i}\n")
        c=c+1
    file.close()
    
# Exercise 2
def read_names(filename):
        file = open(filename, "r")
        names = []
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line != "":
                names.append(cleaned_line)
        file.close()
        return names
    
# Exercise 3
def append_entry(filename, text):
        file = open(filename, "a")
        file.write(text + "\n")
        file.close()
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return len(lines)

# Exercise 4
def search_file(filename, word):
        file = open(filename, "r")
        matching_lines = []
        search_term = word.lower()
        for line_num, line in enumerate(file, start=1):
            if search_term in line.lower():
                matching_lines.append(line_num)
        file.close()
        return matching_lines

# Exercise 5
def number_the_lines(source, destination):
        source_file = open(source, "r")
        lines = source_file.readlines()
        source_file.close()
        dest_file = open(destination, "w")
        count = 0
        for index, line in enumerate(lines, start=1):
            cleaned_line = line.rstrip("\n")
            dest_file.write(f"{index}: {cleaned_line}\n")
            count += 1
        dest_file.close()
        return count
