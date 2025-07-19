def get_names_from_file(file_path):
    with open(file_path, encoding="utf8") as file:
        content = file.read()
    raw_names = content.split("\n")
    clean_names = []
    for raw_name in raw_names:
        clean_name = ""
        for symbol in raw_name:
            if symbol.isalpha():
                clean_name += symbol
        if clean_name:
            clean_names.append(clean_name)
    return clean_names

if __name__ == '__main__':
    names = get_names_from_file("../data/names.txt")

    print(names)