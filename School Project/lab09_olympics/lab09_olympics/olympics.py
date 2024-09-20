from race import run_the_race

competitor_count = 3


competitor_count = int(input('How many competitors are there? (3 to 8) '))
while competitor_count < 3 or competitor_count >8:
    print("Try again")
    competitor_count = int(input('How many competitors are there? (3 to 8) '))

run_the_race(competitor_count)
input('Enter to go to next event.')
go_shotput(competitor_count)
