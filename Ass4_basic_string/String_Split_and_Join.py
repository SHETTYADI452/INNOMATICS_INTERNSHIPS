def split_and_join(line):
    # write your code here
    split=line.split(" ")
    new_line="-".join(split)
    
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)