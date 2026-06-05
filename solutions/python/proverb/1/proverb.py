def proverb(*input_data, qualifier):
    if not input_data:
        return []
    
    lines = []
    for i in range(len(input_data) - 1):
        lines.append(f"For want of a {input_data[i]} the {input_data[i+1]} was lost.")
    if qualifier:
        lines.append(f"And all for the want of a {qualifier} {input_data[0]}.")
    else:
        lines.append(f"And all for the want of a {input_data[0]}.")
    return lines
    