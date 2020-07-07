from src.helpers.palindrome import isPalindrome

def problem348():
    pals = {}
    print(isPalindrome(5229225))
    smolPals = []
    square = 2
    while True:
        cube = 2
        while cube <= square:
            pal = pow(square, 2) + pow(cube, 3)
            if isPalindrome(pal):
                val = (square, cube)
                if pal not in pals:
                    pals[pal] = [val]
                else:
                    pals[pal].append(val)
                if len(pals[pal]) == 4:
                    if pal not in smolPals:
                        print("found", pal, pals[pal])
                        smolPals.append(pal)
                        if len(smolPals) == 5:
                            print(smolPals)
                            print(sum(smolPals))
                            exit(69)
                #print(pal, square, cube)
            #print(str(square) + "^2 +", str(cube) + "^3")
            cube += 1
        square += 1
        #if square > 3000:
        #    break

# 5229225 [(1197, 156), (1810, 125), (2223, 66), (2285, 20)]
# 37088073 [(3300, 297), (3417, 294), (4323, 264), (6083, 44)]
# 56200265 [(5832, 281), (7069, 184), (7249, 154), (7491, 44)]
# 108909801 [(3583, 458), (5901, 420), (6202, 413), (10401, 90)]
# 796767697 [(21705, 688), (24904, 561), (27827, 282), (28215, 88)]