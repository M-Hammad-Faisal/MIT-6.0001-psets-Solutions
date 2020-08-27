#######################
##Problem Set 2 (Q3) ##
#######################

# Name: Muhammad Hammad Faisal
# Regd. Number: 2019-CE-13
# Collaborators: None
# Time Spent: 2 hours
def largenotpkg(pkg1 ,pkg2,pkg3):
    num = 0
    for n in range(1, 150):
        package = False
        for a in range(int(n / pkg1) + 1):
            for b in range(int(n / pkg2) + 1):
                for c in range(int(n / pkg3) + 1):
                    if pkg1 * a + pkg2 * b + pkg3 * c == n:
                        package = True
        if package == True:
            num += 1
        else:
            if num != 6:
                bestsofar = n
                num = 0
            else:
                break
    print("Largest number of McNuggets that cannot be bought"
          " in exact quantity:", bestsofar)




pkg1 = 6
pkg2 = 9
pkg3 = 20
# If Mcdonald supply in
# pkg1 = 6
# pkg2 = 10
# pkg3 = 14

largenotpkg(pkg1, pkg2 ,pkg3)
