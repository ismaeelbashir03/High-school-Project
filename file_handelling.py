#ismaeel bashir

#file handelling

#reading list from file

def readfilelist(score_list, filename):

    file = open(filename, "r")

    for line in file:

        line = line[0:5]
        
        score_list.append(float(line))

    file.close()

    return score_list

#write to file

def rewritefile(filename, scorelist):

    file = open(filename, "w")

    for score in scorelist:

        file.write('%s\n' % score)



