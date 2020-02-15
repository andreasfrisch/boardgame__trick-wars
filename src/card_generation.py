
START_DOCUMENT="""
\\documentclass[a4paper]{article}
\\input{include/libs.tex}
\\input{include/colors.tex}
\\input{include/sizes.tex}
\\input{include/card_definitions.tex}

\\begin{document}
\\begin{center}
\\pagestyle{empty}
\\hyphenpenalty=10000

"""

END_DOCUMENT="""

\\end{center}
\\end{document}
"""

def suitIcon(suit):
    if suit == "teal":
        return "\\suitSquare{teal}"
    elif suit == "hotpink":
        return "\\suitCircle{hotpink}"
    elif suit == "orange":
        return "\\suitTriangle{orange}"
    else:
        return ""

def card(value, suit, effect):
    return """
        \\begin{tikzpicture}
            \\cardborder
            \\cardMiddle
            %s
            \\cardvalue{%d}{%s}
            \\effect{%s}
        \\end{tikzpicture}""" % (suitIcon(suit), value, suit, effect)

SUITS=["teal", "orange", "hotpink"]
VALUE_EFFECTS={
    1: "The losing player becomes the leading player",
    2: "When played, player may swap any card in hand with the trump indicator",
    3: "",
    4: "When played, player may swap this card with the trump indicator",
    5: "When placed, player may activate any coloumn",
    6: "",
    7: "When placed, player may reorganize the acticated coloumn",
    8: "",
    9: "",
    10: "",
    11: "",
    12: "Must be chosen when winning the trick"
}

output_file = open("cards.tex", "w")

output_file.write(START_DOCUMENT)

for suit in SUITS:
    for value, effect in VALUE_EFFECTS.items():
        output_file.write(card(value, suit, effect))
        if value % 3 == 0:
            output_file.write("""
                             \\newline
                             \\noindent
                             """)

output_file.write(END_DOCUMENT)

output_file.close()
