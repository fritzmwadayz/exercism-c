def answer(question):
    if not question.startswith("What is") or not question.endswith("?"):
        raise ValueError("syntax error")

    tokens = question.removeprefix("What is").removesuffix("?").split()
    if len(tokens) == 0:
        raise ValueError("syntax error")
        
    try:
        acc = int(tokens[0])
    except ValueError:
        raise ValueError("syntax error")
        
    i = 1
    while i < len(tokens):
        op = tokens[i]
        
        if op in ("plus", "minus"):
            if i+1 >= len(tokens):
                raise ValueError("syntax error")
            try:
                num = int(tokens[i+1])
            except ValueError:
                raise ValueError("syntax error")
            if op == "plus":
                acc += num
            else:
                acc -= num
            i += 2
            
        elif op in ("multiplied", "divided"):
            if i+2 >= len(tokens) or tokens[i+1] != "by":
                raise ValueError("syntax error")
            try:
                num = int(tokens[i+2])
            except ValueError:
                raise ValueError("syntax error")
            if op == "multiplied":
                acc *= num
            else:
                acc //= num
            i += 3
        
        else:
            try:
                int(op)
                raise ValueError("syntax error")
            except ValueError as e:
                if "syntax error" in str(e):
                    raise
                raise ValueError("unknown operation")
    
    return acc
