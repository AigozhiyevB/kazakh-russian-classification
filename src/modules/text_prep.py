def char_clean(s):
    return ''.join([i for i in s if (i.isalpha() or i==' ')]).lower()

def remove_substr(s, substr):
    tmp_lst = s.split(substr)
    output = ''.join(tmp_lst)
    return output