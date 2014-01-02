import sys
from subprocess import Popen, PIPE


def changegitConfigfile():
    line = ""
    file_reads = open("hellodjango/settings.py","r")
    #previousline = ""
    line = file_reads.read()
    file_reads.close()
    if line.find("''' RunLocaly Comment and Uncomment Run Heroku(Do not change this comment line)") != -1:
        line2 = line.replace("''' RunLocaly Comment and ", "#''' RunLocaly Comment and ")
    if line2.find("''' RunLocaly Comment and Uncomment Run Heroku(Do not change this comment line)") != -1:
        line2 = line2.replace("#''' Setting RunLocaly unComment and comment Run Heroku","''' Setting RunLocaly unComment and comment Run Heroku")    
    file_write = open("hellodjango/settings.py","w")
    file_write.write(line2)
    file_write.close()
    line = ""
    line2 = ""
    file_readw = open("hellodjango/wsgi.py","r")
    line = file_readw.read()
    file_readw.close()
    if line.find("'''RunLocaly Comment and  Uncomment Run Heroku(Do not change this comment line)") != -1:
        line2 = line.replace("'''RunLocaly Comment and  ", "#'''RunLocaly Comment and  ")
    file_write = open("hellodjango/settings.py","w")
    file_write.write(line2)
    file_write.close()    


       
if __name__ == "__main__":
    changegitConfigfile()
    if len(sys.argv) == 3:
        changegitConfigfile() 
        #proc = Popen(['bash',sys.argv[1]], stdin=PIPE)
        #proc.communicate('Y')
        #revertChnagetoconfigfile()
        #proc = Popen(['bash',sys.argv[2]], stdin=PIPE)
        #proc.communicate('Y')
    else:
        print "This need to be in Clone dir and Bash scripts are not provided"
        print "python Changedotgitconfig.py \"gitpull script\" \"run foreman script\" "     

