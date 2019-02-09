# flake8 error because of to many newlines (E303) will be ignored



def arithmetic(values):
    # flake8 error because of missing spaces (E226) will be detected
    return sum(values)/len(values)
