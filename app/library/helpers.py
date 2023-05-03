"""helper library"""

import os
import markdown


def openfile(filename):
    """
    Open file
    """
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)

    data = {
        "text": html
    }

    return data
