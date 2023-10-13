def group_by_extension(file_names):
    file_groups = {}
    files = file_names.split(', ')

    for file in files:
        name, extension = file.rsplit('.', 1)
        if extension in file_groups:
            file_groups[extension].append(file)
        else:
            file_groups[extension] = [file]

    grouped_files = []
    for extension, group in file_groups.items():
        grouped_files.append(', '.join(group))

    return '\n'.join(grouped_files)


file_names = "file1.jpg, file2.gif, file3.mid, file4.jpg"
result = group_files_by_extension(file_names)
print(result)
