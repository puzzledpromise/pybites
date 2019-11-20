HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    value = str(value)
    if len(value) == column_length:
        return value
    result = ''    
    for i in range(column_length - len(value)):
        result+=fill_char

    result+=str(value)
    return result

if __name__ == '__main__':
    value1 = 1
    value2 = 20 
    value3 = 315
    value4 = 1239
    column_length = 4
    fill_char=HTML_SPACE
    print(prefill_with_character(value1, column_length, fill_char))
    print(prefill_with_character(value2, column_length, fill_char))
    print(prefill_with_character(value3, column_length, fill_char))
    print(prefill_with_character(value4, column_length, fill_char))

