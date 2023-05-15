from compile_dlg.print import old_print, new_print
from compile_dlg.rule_handler import check_rules
from compile_dlg.var import new_var
from error import error_crash, unknown

def compile(content):
    vars = {
        "int": {},
        "str": {},
        "bool": {},
    }

    rules = {
        "allow": {
            "old_print": False,
            "debug": False,
            "compile_debug": False,
        },
        "warning": {
            "compile": False,
        }
    }

    # Print hello world using dlg
    for l, li in zip(content, range(len(content))):
        rules = check_rules(l, rules, rules["allow"]["debug"])

        if rules["allow"]["old_print"]:
            old_print(l)
        else:
            try:
                new_print(l, content[li+1], vars, rules["allow"]["debug"])
            except IndexError:
                # Just last line
                pass
            except:
                if rules["allow"]["compile_debug"]:
                    if rules["warning"]["compile"]:
                        print("Be warned, this message shows either if their is a error in the code of dlg itself") 
                        print("But it will always show, if their is an error inside the function compile is running.")
                        print("Remove this kind of hint by setting warning compile")
                    error_crash("compile.new_print", l, unknown, True)

        try:
            vars = new_var(l, content[li+1], content[li+2], vars, rules["allow"]["debug"])
        except IndexError:
            pass # Index error, when last line and attempting to create a new one
        except:
            if rules["allow"]["compile_debug"]:
                if rules["warning"]["compile"]:
                    print("Be warned, this message shows either if their is a error in the code of dlg itself") 
                    print("But it will always show, if their is an error inside the function compile is running.")
                    print("Remove this kind of hint by setting warning compile")
                error_crash("compile.new_var", l, unknown, True)
            
    return rules
