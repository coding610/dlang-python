from error import error_crash


def new_var(l, next1_l, next2_l, vars, is_debug):
    for w in l:
        if w == "let":
            var_name = l[l.index(w)+1]

            var_type = 0
            for w in next1_l:
                if w != " " and w != "" and w != "  ":
                    if (w == "str" or w == "int" or w == "bool" or w == "float"):
                        var_type = w
                    else:
                        error_crash("new_var.(loop)w1", next1_l, w, is_debug)
            
            var_content = 0
            for w2 in next2_l:
                if w2 != " " and w2 != "" and w2 != "  ":
                    if var_type == "int":
                        if w2.isdigit(): var_content = w2
                        else: error_crash("new_var.(loop)w2", next2_l, w2, is_debug)
                    elif var_type == "float":
                        # Is no good way of doing this
                        if isfloat(w2): var_content = w2
                        else: error_crash("new_var.(loop)w2", next2_l, w2, is_debug)
                    elif var_type == "bool":
                        if w2 == "true" or w2 == "false": var_content = w2
                        else: error_crash("new_var.(loop)w2", next2_l, w2, is_debug)
                    else: # Var type must be string now
                        #print("its a me string")
                        pass


            vars[var_name] = [var_type, var_content]

    return vars



def isfloat(inp_string):
    try:
        float(inp_string)
        return True
    except:
        return False
