def getAsBrackects(lineedit_as: str):
    if "[" in lineedit_as and "]" in lineedit_as:
        return lineedit_as
    else:
        lineedit_as = "[", lineedit_as, "]"
        return "".join(list(lineedit_as))
