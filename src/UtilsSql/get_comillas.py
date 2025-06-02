def get_comillas(texto: str):
    comillas = "'"
    Comillas = '"'
    if Comillas in texto:
        return "'" + texto + "'"
    elif comillas in texto:
        return '"' + texto + '"'
    else:
        return "'" + texto + "'"
