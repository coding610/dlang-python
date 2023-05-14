import compile_dlg
import copy


def main():
    content_class = get_contents("dlg/main.dlg")
    content = [l for l in content_class]
    content = trim(content)
    content = parse(content)
    compile_dlg.compile(content)


    

def get_contents(file_path):
    file_content = open(file_path, "r")
    return file_content

# Trims \n of strings in list
def trim(content):
    return [l[:len(l) - 1] for l in content]

def parse(content):
    for l in range(len(content)):
        content[l] = content[l].split(" ")

        # Remove unnessesary spaces
        for w in content[l]:
            if w == "":
                content[l].remove(w)

    # Remove unnecessary lines
    parsed_content = copy.deepcopy(content)
    for l in content:
        if l == []:
            parsed_content.remove(l)


    return parsed_content
        

if __name__ == "__main__":
    main()
