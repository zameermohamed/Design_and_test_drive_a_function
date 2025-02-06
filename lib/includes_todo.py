def includes_todo(notes):
    if len(notes)==0:
        raise Exception ("Can not check an empty string")
    return "#TODO" in notes
    