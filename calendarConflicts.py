def hasConflicting(events):
    for i in range(len(events)):
        if i == len(events) - 1:            return False
        if events[i][1] > events[i + 1][0]: return True

conflictingEvents = [[1, 2, 'a'], # Start, End, ID
                     [3, 5, 'b'],
                     [4, 6, 'c'],
                     [7, 10, 'd'],
                     [8, 11, 'e'],
                     [10, 12, 'f'],
                     [13, 14, 'g'],
                     [13, 14, 'h']]

# nonConflictingEvents = [[1, 2, 'a'], # Start, End, ID
#                         [3, 5, 'b']]

print('Conflicting events!' if hasConflicting(conflictingEvents) else 'No conflicting events!')