import re

def strip_comments(string: str, markers: list):
    if not markers:
        return string
    string = string.splitlines()
    pattern = "[\\" + "\\".join(markers) + "]"
    pattern = re.compile(pattern)
    
    res = []
    for line in string:
        index = pattern.search(line)
        if index is None:
            res.append(line.rstrip())
        else:
            res.append(line[:index.span()[0]].rstrip())
    return "\n".join(res)
        
        


if __name__ == "__main__":
    string = '\tcherries watermelons ^ lemons = apples\n,\ncherries strawberries @ apples bananas\navocados'
    markers = ['.', ',', '-', '#', "'", '=', '@', '!']
    print(strip_comments(string, markers))
