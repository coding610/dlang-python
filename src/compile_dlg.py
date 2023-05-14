def compile(content):
    rules = {
            "Allow": {
                "old_print": False
                }
            }

    # Print hello world using dlg
    for l in content:
        rules = check_rules(l, rules)

        if rules["Allow"]["old_print"]:
            old_print(l)
        else:
            try:
                new_print(l, content[content.index(l)+1])
            except:
                # Just last line
                pass

def check_rules(l, rules):

    for w in l:
        try:
            if w[0] == "#":
                allow_contents = w[1:]
                if allow_contents == "old_print":
                    rules["Allow"]["old_print"] = True
        except:
            # This is when we get a tab as a word
            pass
            
    return rules


def old_print(l):
    try:
        if l[0] == "print":
            print_content = l[1:]
            pritty_print(print_content)
    except:
        pass

def new_print(l, next_l):
    try:
        if l[0] == "print":
            print_content = []
            for w in next_l:
                if w != " " and w != "" and w != "  ":
                    print_content.append(w)

            pritty_print(print_content)
    except:
        pass


def pritty_print(print_content):
    try:
        for print_w in print_content:
            if print_content.index(print_w) != len(print_content)-1:
                print(print_w, end=" ")
            else:
                print(print_w)
    except:
        pass
