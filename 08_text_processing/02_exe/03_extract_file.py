os_path = input().split('\\')
split_name_and_extension = os_path[-1].split('.')

file_name = split_name_and_extension[0]
extension = split_name_and_extension[1]

print(f'File name: {file_name}\nFile extension: {extension}')
