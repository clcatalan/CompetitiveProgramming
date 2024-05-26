def compareRoutines(r1, r2):

    r1Chars = [c for c in r1]
    r2Chars = [c for c in r2]
    quickChanges =  len([i for i in r1 if i in r2 ])

    return quickChanges


def getQuickChanges(routines):
    quickChangesTotal = 0
    for i in range(len(routines)-1):
        r1 = routines[i]
        r2 = routines[i+1]
        quickChangesTotal += compareRoutines(r1, r2)
    return quickChangesTotal


def permutation(changes, routines, i = 0):
    if i == len(routines):
        # print(routines)
        changes.append(getQuickChanges(routines))
    else:
        for j in range(i, len(routines)):
            routines[i], routines[j] = routines[j], routines[i]
            permutation(changes, routines, i+1)
            routines[j], routines[i] = routines[i], routines[j]

def main():
    r = int(input())
    routines = []
    for i in range(r):
        routines.append(input())

    changes = []
    permutation(changes, routines)

    print(min(changes))   
main()