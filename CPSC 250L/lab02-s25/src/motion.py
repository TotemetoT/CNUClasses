"""
Practice with lists and tuples


@author <Your Name Here>
@version <Date Here>

"""
def motion(start, motions):
    x=start[0]
    y=start[1]

    for i in range(len(motions)):
        x = x + motions[i][0]
        y = y + motions[i][1]
    return x,y

"""
    Calculate the final position given a starting point (x,y), and a list
    of incremental motions as a list of tuples (dx, dy)

    Calculate the final position by adding the incremental motions to the
    appropriate term.
    For example, starting at (1,2), with
    motions=[(2,0), (0, 2), (1, 3)]
    The intermediate positions would be
    (1+2, 2),  (3, 2+2), (3+1, 4+3) with final position (4, 7)

    Hint: You may need to convert from tuple-to-list and list-to-tuple


    :param start:  tuple of starting position (x,y)
    :param motions:  list of tuples of [(dx1, dy1), ...(dxn, dyn)]
                       that define incremental "motions" on a grid
    :return: tuple with final (x,y) position
"""


if __name__ == '__main__':
    # Here is simple test - no need to modify below
    starting_position = (1, 2)
    motion_list = [(2, 0), (0, 2), (1, 3)]
    print("Final position", motion(starting_position, motion_list))
