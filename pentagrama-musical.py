def validate_melody(melody):
    # Notas válidas
    notes_latina = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
    notes_english = ["C", "D", "E", "F", "G", "A", "B"]
    allowed_alterations = ["#", "b"]

    notes = melody.split()

    # Validar que el número de notas sea múltiplo de 4
    if len(notes) % 4 != 0:
        return False, "La cantidad de notas debe ser múltiplo de 4."

    scale_type = None
    for note in notes:
        if len(note) < 2 or len(note) > 5:  # Ajustar para nombres largos con alteraciones y octava
            return False, f"Formato incorrecto en la nota: {note}"

         # Separar base, alteración y octava
        alteration = ""
        if len(note) >= 3 and note[-2] in allowed_alterations:  # Nota con alteración
            alteration = note[-2]
            octave = note[-1]
            base_note = note[:-2]
        else:  # Nota sin alteración
            octave = note[-1]
            base_note = note[:-1]

        # Validar formato de la base
        if not base_note.isalpha():
            return False, f"Base de nota inválida: {base_note} en {note}"

        # Validar alteración (si existe)
        if alteration and alteration not in allowed_alterations:
            return False, f"Alteración inválida en la nota: {note}"

        # Validar octava
        if not octave.isdigit() or not (1 <= int(octave) <= 8):
            return False, f"La octava debe estar entre 1 y 8: {note}"

        # Validar tipo de notación
        if base_note in notes_latina:
            if scale_type is None:
                scale_type = "latina"
            elif scale_type != "latina":
                return False, "No se puede mezclar notación latina y anglosajona."
        elif base_note in notes_english:
            if scale_type is None:
                scale_type = "english"
            elif scale_type != "english":
                return False, "No se puede mezclar notación latina y anglosajona."
        else:
            return False, f"Nota inválida: {note}"

    return True, scale_type


def convert_to_english(note):
    # Conversión de notación latina a anglosajona
    notes_map = {
        "Do": "C",
        "Re": "D",
        "Mi": "E",
        "Fa": "F",
        "Sol": "G",
        "La": "A",
        "Si": "B"
    }
    base_note = note[:-1]  # Extraer base (Do, Re, etc.)
    octave = note[-1]     # Extraer octava
    alteration = ""
    if len(base_note) > 1 and base_note[-1] in ["#", "b"]:
        alteration = base_note[-1]
        base_note = base_note[:-1]
    return f"{notes_map.get(base_note, base_note)}{alteration}{octave}"


def generate_staff(melody, scale_type):
    # Rango extendido de notas
    note_positions = {
        # Notas graves (C3 a B3)
        "C3": -8, "B#2": -8,
        "C#3": -7.5, "Db3": -7.5,
        "D3": -7,
        "D#3": -6.5, "Eb3": -6.5,
        "E3": -6, "Fb3": -6,
        "E#3": -5.5, "F3": -5.5,
        "F#3": -5, "Gb3": -5,
        "G3": -4,
        "G#3": -3.5, "Ab3": -3.5,
        "A3": -3,
        "A#3": -2.5, "Bb3": -2.5,
        "B3": -2, "Cb4": -2,

        # Pentagrama principal (C4 a B4)
        "C4": -1, "B#3": -1,
        "C#4": 0.5, "Db4": 0.5,
        "D4": 1,
        "D#4": 1.5, "Eb4": 1.5,
        "E4": 2, "Fb4": 2,
        "E#4": 2.5, "F4": 2.5,
        "F#4": 3, "Gb4": 3,
        "G4": 4,
        "G#4": 4.5, "Ab4": 4.5,
        "A4": 5,
        "A#4": 5.5, "Bb4": 5.5,
        "B4": 6, "Cb5": 6,

        # Notas agudas (C5 a B5)
        "C5": 7, "B#4": 7,
        "C#5": 7.5, "Db5": 7.5,
        "D5": 8,
        "D#5": 8.5, "Eb5": 8.5,
        "E5": 9, "Fb5": 9,
        "E#5": 9.5, "F5": 9.5,
        "F#5": 10, "Gb5": 10,
        "G5": 11,
        "G#5": 11.5, "Ab5": 11.5,
        "A5": 12,
        "A#5": 12.5, "Bb5": 12.5,
        "B5": 13, "Cb6": 13,

        # Notas más agudas (C6 y más)
        "C6": 14, "B#5": 14,
        "C#6": 14.5, "Db6": 14.5,
        "D6": 15,
        "D#6": 15.5, "Eb6": 15.5,
        "E6": 16, "Fb6": 16,
    }

    # Crear un pentagrama dinámico basado en la cantidad de notas
    columns = len(melody) * 4  # Cada nota ocupa 4 columnas
    # 13 filas: 5 líneas + espacios
    pentagram = [[" " for _ in range(columns)] for _ in range(9)]

    # Dibujar las líneas del pentagrama
    for i in range(1, 9, 2):
        for j in range(columns):
            pentagram[i][j] = "-"

    col = 0
    for note in melody:
        # Convertir a notación anglosajona si es necesario
        if scale_type == "latina":
            note = convert_to_english(note)

        # Validar y separar partes de la nota
        alteration = ""
        if len(note) >= 3 and note[-2] in ["#", "b"]:  # Nota con alteración
            alteration = note[-2]
            octave = note[-1]
            base_note = note[:-2]
        else:  # Nota sin alteración
            octave = note[-1]
            base_note = note[:-1]

        # Construir la clave de la nota
        note_key = f"{base_note}{alteration}{octave}"
        # Posicionar en el pentagrama
        position = note_positions.get(note_key, None)
        print(note_key, position)
        if position is None:
            print(f"Nota fuera del rango definido: {note_key}")
            continue

        # Calcular la fila en el pentagrama
        row = 8 - int(position)

        # Representar la alteración antes de la nota
        if alteration:
            pentagram[row][col] = alteration
            pentagram[row][col + 1] = "O"
        else:
            pentagram[row][col + 1] = "O"

        col += 4

    # Convertir el pentagrama en una salida legible
    return "\n".join("".join(row) for row in pentagram)


# Programa principal
while True:
    melody_input = input("Ingrese la melodía: ")
    valid, scale = validate_melody(melody_input)
    if valid:
        melody = melody_input.split()
        staff_output = generate_staff(melody, scale)
        print(staff_output)
        break
    else:
        print("Error en la entrada:", scale)
