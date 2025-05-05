def is_palindrome(strr):

    rev_str = strr[::-1]

    if strr==rev_str:
        return {'value': True, 
                'word':strr, 
                'reversed_string':rev_str}
    return {'value': False, 
                'word':strr, 
                'reversed_string':rev_str}

print(is_palindrome('tote'))