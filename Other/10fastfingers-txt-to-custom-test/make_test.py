import os
from datetime import datetime


def main(filepath, output_filename=None):
    """Replaces "newlines" and "spaces" with "|" as well as substitute uncommon characters with their equivalents:
        “”  ""
        ’   '
        —   -

    Parameters
    ----------
        filepath : string
            Relative or absolute path to the text you would like to convert.
        output_filename  : (optional) string
            Relative or absolute path to the output file. Default is "test-Text-TIMESTAMP".
    """
    with open(filepath, "r") as f:
        data = f.read()

    txtdict = data.maketrans("“”’— \n", "\"\"'-||")
    data.translate(txtdict).replace("||", "|").replace("_","")

    if output_filename is None:
        output_filename = f"test-Text-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}.txt"

    with open(output_filename, "w") as f:
        f.write(data.translate(txtdict).replace("||", "|").replace("_", ""))


if __name__ == '__main__':
    main("example.txt")
