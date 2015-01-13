## String to Integer (atoi)
def atoi(str):
    new_str = str.strip()
    end = ""

    for id,val in enumerate(new_str):
        if val in ['+','-'] and id == 0:
            end += val
        elif val.isdigit():
            end += val
        else:
            break

    if end in ['+','-']:
        end = ""
    end = int(end) if end else 0

    if end > 2147483647:
        return 2147483647
    if end < -2147483648:
        return -2147483648
    return end
