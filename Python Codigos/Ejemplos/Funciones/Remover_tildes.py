# Remover tildes

"""
Programa para quitar tildes de un texto
"""

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

print(normalize("¿Cómo compaginar la aniquiladora idea de la muerte\
con ese incontenible afán de vida ¿cómo acoplar el horror\
ante la nada que vendrá con la invasora alegría del amor\
provisional y verdadero? ¿cómo desactivar la lápida con el\
sembradío? ¿la guadaña con el clavel? ¿será que el hombre es eso?\
¿esa batalla?"))