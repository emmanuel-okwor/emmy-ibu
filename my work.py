#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      okwor
#
# Created:     03/07/2024
# Copyright:   (c) okwor 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    jamb_result=[70,95, 80, 90,100,110,120, 130, 140, 150,]
    high_score=[]
    low_score=[]
    for list in jamb_result:
        if list>70 and list<100:
            low_score.append(list)
        elif list >100:
            high_score.append(list)

    print(low_score)
    print(high_score)

if __name__ == '__main__':
    main()
