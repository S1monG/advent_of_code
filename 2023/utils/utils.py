
def starts_with(string, prefix):
    return string[:len(prefix)] == prefix

def ends_with(string, suffix):
    return string[-len(suffix):] == suffix