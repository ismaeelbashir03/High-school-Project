#ismaeel bashir

#insertion sort

#defines a function for insertion sort
def insertion_sort(scorelist):

    #loops starting at second element in list and ends at the legnth of the list -1
    for index in range(0, len(scorelist)):

        #sets current value as current value in list
        currentVal = scorelist[index]

        #sets position as index
        pos = index

        #loops while pos doesnt reach the start of list and element before current value is bigger
        while pos > 0 and scorelist[pos-1] > currentVal:

            #sets the current value in list to previous element
            scorelist[pos] = scorelist[pos-1]

            #increments the position by -1
            pos -= 1

        #sets the current value as element in pos index
        scorelist[pos] = currentVal

    #returns values
    return scorelist



