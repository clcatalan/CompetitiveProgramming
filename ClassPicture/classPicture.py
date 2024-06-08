def dontLikeEachOther(name1, name2, studentDict, matrix):
    if name1 == '' and name2 == '':
        return False
    i = studentDict[name1]
    j = studentDict[name2]
    if matrix[i][j] == 1 or matrix[j][i] == 1:
        return True
    return False

def permutation(matrix, studentDict, students, visited, subset, i):
    if i == len(students):
        # im thinking append all valid permutations into a list, then at main, just get the first one in that list
        print(subset)
        return
    else:
        for j in range(len(students)):
            if not visited[j]:
                name1 = ''
                name2 = ''
                if(i > 0):
                    name1 = subset[len(subset)-1]
                    name2 = students[j]
                if not dontLikeEachOther(name1, name2, studentDict, matrix):
                    subset.append(students[j])
                    visited[j] = True
                    permutation(matrix, studentDict, students, visited, subset, i+1)
                    subset.pop()
                    visited[j] = False


def main():
    n = int(input())
    students = []
    studentDict = {}
    for i in range(n):
        x = input()
        students.append(x)
    
    students.sort()

    for i in range(n):
        studentDict[students[i]] = i


    m = int(input())
    

    matrix = [[0 for j in range(n)] for i in range(n)]

    for i in range(m):
        p = input().split()
        i = studentDict[p[0]]
        j = studentDict[p[1]]
        matrix[i][j] = matrix[j][i] = 1

    # print(matrix)
    # print(studentDict)


    visited = [False]*n


    permutation(matrix, studentDict, students, visited, [], 0)

main()