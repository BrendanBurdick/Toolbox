col_names = []
col_types = []

print("What file do you want the column names and types for?")
file_name = input();

with open(file_name) as file:
	for line in file:
		parsed_line = line.split()
		col_names.append(parsed_line[0])
		if(parsed_line[1] == 'NUMBER'):
			col_types.append(parsed_line[1] + parsed_line[2])
		elif(parsed_line[1] == 'VARCHAR2'):
			col_types.append(parsed_line[1] + parsed_line[2] + " " + parsed_line[3])
		else:
			col_types.append(parsed_line[1])
			
formatted_file = open("DB_OUTPUT_FILE.txt", "w")
for x in col_names:
	formatted_file.write(x + "\n")
	
formatted_file.write("\n")
	
for y in col_types:
	formatted_file.write(y + "\n")
	
print("File created.")