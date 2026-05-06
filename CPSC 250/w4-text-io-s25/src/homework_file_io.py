import os


def write_file(file_path, n):
    """
    Write a pattern that looks like this into a file with n number of lines

    Below is the result of make_pattern(file_path, 5)
    *
    ##
    ***
    ####
    *****

    :param file_path:
    :param n: Number of lines to follow this pattern
    :return:
    """

    with open(file_path,'wt') as fout:
        temp = ''
        for i in range(1,n+1):
            if i % 2 != 0:
                temp += '*'*i
            else:
                temp += '#'*i
            temp += '\n'
        fout.write(temp)


def append_file(file_path, n):
    """
    Open a file and continue the pattern as seen above in the file. The pattern will be the same as in write_file().

        Note: Do not write a new file or you will not receive credit for the function.

        Note #2: You should be able to continue the pattern based on the last line only.
                 Meaning you should be able to continue the patter of a file that only has "*****\n" in it.

    :param file_path:
    :param n: Max number of lines
    :return: NLINES: number of lines written
    """
    with open(file_path,'rt') as fin:
        line = fin.readlines()
        length = len(line[-1])-1
    with open(file_path,'wt') as fout:
        temp = ''
        for i in range(length,n+1):
            if i % 2 != 0:
                temp += '*' * i
            else:
                temp += '#' * i
            temp += '\n'
        fout.write(temp)
    return n




def text_attributes(file_path):
    """
    Given a file_path of a valid text file return the number of characters and number of lines in a file.

    Note: Ignore newlines for the character count!

    :param file_path: File path with filename
    :return: tuple with number of characters and number of lines in that order
    """
    characters = 0
    with open(file_path,'rt') as fout:
        line = fout.readlines()
        line_amount = len(line)
        for i in line:
            characters += len(i)-1
    return characters,line_amount


if __name__ == '__main__':
    # Write a pattern to a file
    write_file(os.path.join("data", "cpsc250.txt"), 5)

    # Append a pattern to a file
    NLINES = append_file(os.path.join("data", "cpsc250.txt"), 4)
    print(f"Number of lines written: {NLINES}")

    # Get the number of characters and lines in a file
    file_path = os.path.join("data", "fourier_dataset.txt")
    chars, lines = text_attributes(file_path)
    print(f"Number of characters: {chars}")
    print(f"Number of lines: {lines}")
