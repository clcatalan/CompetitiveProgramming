from sys import stdin
matrix = []
studentDict = {}
foundSolution = False

def dontLikeEachOther(name1, name2):
    global matrix
    global studentDict
    if name1 == '' and name2 == '':
        return False
    i = studentDict[name1]
    j = studentDict[name2]
    if matrix[i][j] == 1 or matrix[j][i] == 1:
        return True
    return False

def permutation(students, visited, subset, i):
    global matrix
    global studentDict
    global foundSolution

    if not foundSolution:
        if i == len(students):
            foundSolution = True
            print(" ".join(subset))
            return
        else:
            for j in range(len(students)):
                if not visited[j]:
                    name1 = ''
                    name2 = ''
                    if(i > 0):
                        name1 = subset[len(subset)-1]
                        name2 = students[j]
                    if not dontLikeEachOther(name1, name2):
                        subset.append(students[j])
                        visited[j] = True
                        permutation(students, visited, subset, i+1)
                        subset.pop()
                        visited[j] = False


def main():
    global matrix
    global studentDict
    global foundSolution

    while True:
        try:
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

            visited = [False]*n


            permutation(students, visited, [], 0)

            if not foundSolution:
                print("You all need therapy.")
        except EOFError:
            break

    

main()