def split_text(texto):
    if len(texto) > 190:
        words = texto.split()
        above = " ".join(words[: len(words) // 3])
        half = " ".join(words[len(words) // 3: (len(words) // 3) * 2])
        below = " ".join(words[(len(words) // 3) * 2:])
        return above + "\n" + half + "\n" + below
    elif len(texto) > 90:
        words = texto.split()
        above = " ".join(words[: len(words) // 2])
        below = " ".join(words[len(words) // 2:])
        return above + "\n" + below
    else:
        return texto
