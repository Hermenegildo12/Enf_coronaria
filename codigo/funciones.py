def rango (e):
    if e<120:
        return "Óptimo"
    elif 120<=e<130:
        return "Normal"
    elif 130<=e<140:
        return "ligeramente elevada"
    elif 140<=e<160:
        return "HTA Grado 1"
    elif 160<=e<180:
        return "HTA Grado 2"
    elif e>=180:
        return "HTA Grado 3"
    else:
        return "Error"