#!/usr/bin/python3
"unlocking boxes"


def canUnlockAll(boxes):
    "unlocking boxes"
    push = []
    for index in range(1, len(boxes) - 1):
        display = boxes[0]
        display.extend(boxes[index])
        for number in display:
            push.extend(boxes[number])
        unique_list = list(set(push))
        if index + 1 not in unique_list:
            return False

    return True
