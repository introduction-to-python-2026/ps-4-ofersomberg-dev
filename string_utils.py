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
    if not formula:
        return []
    
    split_formula = []
    start = 0
    
    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i 
    
    split_formula.append(formula[start:])
    
    return split_formula
