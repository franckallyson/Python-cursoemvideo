def notes(*notes, sit=False):
    '''
    -> Function of analyze notes and situation of various students.
    :param notes: One or more student grades (accept multiple)
    :param sit: (Optional) Indicates whether or not to add the situation
    :return: Dictionary with various information.
    '''
    reportCard = dict()
    reportCard['total'] = len(notes)
    reportCard['highest'] = max(notes)
    reportCard['smaller'] = min(notes)
    reportCard['average'] = sum(notes) / len(notes)
    if sit:
        if reportCard['average'] < 6:
            reportCard['situation'] = 'Bad'
        elif reportCard['average'] < 7:
            reportCard['situation'] = 'Moderate'
        else:
            reportCard['situtation'] = 'Good'
    return reportCard


# Main Program
ans = notes(3.5, 7, 8, 5, 3.5, sit=True)
print(ans)
help(notes)
