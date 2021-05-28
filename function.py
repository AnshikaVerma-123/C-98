def countWordfromfile () :
    fileName =  input ("Enter your file name: ")
    noofwords = 0
    file = open (fileName , "r") 
    for Line in file : 
      word = Line.split ()
      noofwords = noofwords+ len(word)
    print ("Number Of Words")
    print (noofwords)




countWordfromfile () 