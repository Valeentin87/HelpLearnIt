def make_list_name_blocks():
    with open("name_blocks.txt", "r+") as file:
        s=file.read()
        name_blocks=s.split("|")
    return name_blocks

list_name_blocks = make_list_name_blocks()
print(list_name_blocks[:-1])