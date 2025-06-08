def order_matches_by_latest(matches:list[list]):
    for index, match in enumerate(matches):
        left_pointer = index
        right_pointer = len(matches) - (1+index)

        if right_pointer<=left_pointer:
            break

        right_match = matches[right_pointer]
        matches[right_pointer] = match
        matches[left_pointer] = right_match