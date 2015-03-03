"""
Convertion d'un fichier rmd vers dokuwiki
Amelioration:
    * Supprimer le header
    * Formater les menus niveaux 2, attention ne doit pas les supprimer dans les portions <code>
    * Liste a puce ("- " -> " *  ")
"""

afinnfile = open("in.rmd", "r")
outfile = open("out.txt", "w")

for line in afinnfile:
    line = line.replace("`", "``")
    if(line[0:5] == "```{r"):
        newline = "<code rsplus>"
    
    elif(line[0:3] == "```"):
        newline = "</code>"
    elif(line[0:2] == "# "):
        newline = "==== " + line[2:-1] + " ===="
    elif(line[0:8] == "<center>"):
        newline = ""
    elif(line[0:9] == "</center>"):
        newline = ""
    elif(line[0:5] == "<img "):
        splitter = line.split("\"")
        newline = "{{" + splitter[1] + "?}}" 
    else:
        newline = line
    outfile.write(newline)

afinnfile.close()
outfile.close()

