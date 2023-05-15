from error import error_crash, unknown


# No support for vars
def old_print(l, is_debug):
    try:
        if l[0] == "print":
            print_content = l[1:]
            pritty_print(print_content, is_debug)
    except IndexError:
        pass
    except:
        error_crash("old_print", l, unknown, is_debug)

def new_print(l, next_l, vars, is_debug):
    try:
        if l[0] == "print":
            print_content = []
            for w in next_l:
                if w != " " and w != "" and w != "  ":
                    if w[0] == "$":
                        print_content.append(vars[w[1:]][1])
                    else:
                        print_content.append(w)

            pritty_print(print_content, is_debug)
    except IndexError:
        pass
    except:
        error_crash("new_print", l, unknown, is_debug)


def pritty_print(print_content, is_debug):
    try:
        for print_w in print_content:
            if print_content.index(print_w) != len(print_content)-1:
                print(print_w, end=" ")
            else:
                print(print_w)
    except IndexError:
        pass
    except:
        error_crash("print_content", unknown, unknown, is_debug)
