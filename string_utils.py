def split_before_each_uppercases(formula):
    start = 0
    end = 1
    split_formula = []
    
    for char in formula[1:]:
        if char.isupper():
            split_formula.append(formula[start:end])
            start = end
        end += 1
    
    split_formula.append(formula[start:end])
    
    return split_formula


def split_before_each_uppercases(formula):
    # Handle empty string right away
    if formula == "":
        return []
    
    split_formula = []
    start = 0
    end = 1
    
    # Loop from second character onward
    for char in formula[1:]:
        if char.isupper():
            split_formula.append(formula[start:end])
            start = end
        end += 1
    
    # Append last segment
    split_formula.append(formula[start:end])
    
    return split_formula
