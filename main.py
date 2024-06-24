def removeInterrogation(sheet):
    for letter in sheet:
        if letter == "?":
            sheet = sheet.replace(letter, "")
    return sheet
