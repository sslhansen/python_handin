import csv
import platform

def write_list_to_file(output_file, lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    with open(output_file, 'a', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        [output_writer.writerow(value) for value in lst]


def write_list_to_file_strings(output_file, lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    with open(output_file, 'a', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(lst)

    

def print_file_content(file):
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))

def read_csv(input_file):
        return_list = []
        with open(input_file) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for row in reader:
                return_list.append(str(row))
        return return_list