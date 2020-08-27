#######################
##Problem Set 2 (Q4) ##
#######################

# Name: Muhammad Hammad Faisal
# Regd. Number: 2019-CE-13
# Collaborators: None
# Time Spent: 2 hours
def largenotpkg(pkgs):
    num = 0
    pkg1 = pkgs[0]
    pkg2 = pkgs[1]
    pkg3 = pkgs[2]
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
    print("Given package sizes", pkg1, ",", pkg2, "and", pkg3,
          "the largest number of McNuggets that cannot be bought"
          " in exact quantity is: ", bestsofar)


package = (3,19,30)
# package can be changed to any tuple of three elements like below:
# package = (4,14,24)
# package = (10,11,12)
largenotpkg(package)


