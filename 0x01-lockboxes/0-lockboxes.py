#!/usr/bin/python3
"""Python script for unlocking a list of locked boxes."""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Returns True if possible, else False.
    """
    # if value of key in box == num of box, key unlocks that box
    # keys with values that don't match box id(number)
    # box[0](1st index of the box list) is unlocked(key value known)
    # boxes are [[ list of lists ]]

    num_boxes = len(boxes)
    opened = [0]
    for box_id, box in enumerate(boxes):
        for k in box:
            if k < num_boxes and k not in opened and k != box_id:
                opened.append(k)
    if len(opened) == num_boxes:
        return True
    return False
