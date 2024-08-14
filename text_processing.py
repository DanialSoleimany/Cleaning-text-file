def read_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines

def process_lines(lines):
    processed_lines = []
    for line in lines:
        processed_line = ""
        for char in line:
            if char.isalpha() or char.isspace():
                processed_line += char
        processed_lines.append(processed_line.capitalize())
    return processed_lines

def write_file(lines, dest_path):
    with open(dest_path, "a") as f:
        for line in lines:
            f.write(line)