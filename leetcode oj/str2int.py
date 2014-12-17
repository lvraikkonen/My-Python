# string to int
# import re
#
# def char2int(c):
#     d = {'0':0,'1':1,'2':2,'3':3,'4':4,
# 	     '5':5,'6':6,'7':7,'8':8,'9':9}
#     if c in d.keys():
#         return d[c]
#
# def construct_num(x,y):
#     return x*10 + y
#
# ## reduce(construct_num, map(char2int,'43546432'))
# def combine_str(x,y):
#     return x + y
#
# def str2int(s):
#     tmp_str = reduce(combine_str,re.findall('\d+',s))
#
#     result = reduce(construct_num,map(char2int,tmp_str))
#     if result > 2147483647:
#         return 'INT_MAX'
#     if result < -2147483648:
#         return 'INT_MIN'
#     return result

def atoi(str):
    new_str = str.strip()
    end = ""
    for i,val in enumerate(new_str):
        if val in ['+','-'] and i==0:
            end += val
        elif val.isdigit():
            end += val
        else:
            #continue # int after strings
            break
    if end in ['+','-']:
        end = ""
    end = int(end) if end else 0
    if end > 2147483647:
        return 'INT_MAX'
    if end < -2147483648:
        return 'INT_MIN'
    return end

str = '+-313'
print atoi(str)