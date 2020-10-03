def open_file(file_name):
    with open(file_name, encoding = 'utf-8') as file:
        lines = file.readlines()
    return lines

def combine_files(result_file_name, *files):
    lines_dict = {}    
    for file in files:
        lines = open_file(file)
        lines_dict[file] = [len(lines), lines]    
    lines_dict = list(lines_dict.items())
    lines_dict.sort(key=lambda i: i[1])
    with open(result_file_name, 'a') as result_file:
        for i in range(0, len(files)):
            if i != 0:
                result_file.write(f'\n')              
            result_file.write(f'{lines_dict[i][0]}\n{str(lines_dict[i][1][0])}\n{"".join(map(str, lines_dict[i][1][1]))}')        
    print(f'Файлы объединены в {result_file_name}')
    return result_file

def main():
    combine_files("result.txt", "1.txt", "2.txt", "3.txt")
    
main()
