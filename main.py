from text_processing import * 

lines = read_file("data.txt")
processed_lines = process_lines(lines)
write_file(processed_lines, "processed_data.txt")