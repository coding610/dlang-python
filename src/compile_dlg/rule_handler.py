from error import error_crash, unknown


def check_rules(l, rules, is_debug):
    for w in l:
        try:
            if w[0] == "#":
                allow_contents = w[1:]
                if allow_contents == "old_print":
                    rules["allow"]["old_print"] = True
                if allow_contents == "debug":
                    rules["allow"]["debug"] = True

            if w[0] == "!":
                allow_contents = w[1:]
                if allow_contents == "debug":
                    rules["warning"]["debug"] = True
        except IndexError:
            # This is when we get a tab as a word
            pass
        except:
            error_crash("check_rules", l, unknown, is_debug)


    return rules
