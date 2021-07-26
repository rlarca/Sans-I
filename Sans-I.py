#Sans-I
#this will be useful for a future algorithm to automatically analyise the outputs of each sans i file against the source file
#written entirely by Robert Larca


print('Please enter the name of the file you would like to segment (remember to include the extension of the file (".txt") and to have the desired file in the same folder as this python file)')
filename = input()
f = open(filename, "r")
fLines = f.readlines()
fLength = len(fLines)
filename = str(filename[:filename.index(".")])
filename = filename +'@SansI@'

i = 0
while i < fLength:
    #TODO implement the algorithm, creating flength files and not printing when i = j
    sansfilename = filename + str(i) + ".txt"
    j = 0
    with open(sansfilename, 'w') as fp:
        while j < fLength:
            if i == j:
                print(str (i) + str(j) )
            else:
                fp.write(fLines[j])

            j+=1
    i+=1