# n = int(input())
# students = list(map(int, input().split()))

# count = [0, 0, 0]
# for student in students:
#     count[student - 1] += 1

# if min(count) == 0:
#     print(0)
# else:
#     w = min(count)  
#     print(w)

# for ind, i in enumerate(students):


def form_teams(n, inclinations):
    teams = []
    programmers = []
    mathematicians = []
    athletes = []

    # Group students based on inclinations
    for i in range(n):
        if inclinations[i] == 1:
            programmers.append(i + 1)
        elif inclinations[i] == 2:
            mathematicians.append(i + 1)
        else:
            athletes.append(i + 1)

    # Calculate the maximum number of teams
    num_teams = min(len(programmers), len(mathematicians), len(athletes))

    # Form teams by selecting one student from each category
    for _ in range(num_teams):
        team = [programmers.pop(), mathematicians.pop(), athletes.pop()]
        teams.append(team)

    return num_teams, teams

# Example usage
n = int(input())
inclinations = list(map(int, input().split()))

num_teams, teams = form_teams(n, inclinations)
print(num_teams)
for team in teams:
    print(*team)