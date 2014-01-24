'''
Created on 19-Jan-2014

@author: ghanshyam
'''
import sys
from subprocess import Popen, PIPE


def changegitConfigfile_setting():
    line = ""
    line2 = "" 
    file_reads = open("hellodjango/settings.py","r")
    #previousline = ""
    line = file_reads.read()
    file_reads.close()
    if line.find("#''' RunLocaly Comment and Uncomment Run Heroku(Do not change this comment line)") != -1:
        line2 = line.replace("#''' RunLocaly Comment and", "''' RunLocaly Comment and")
    if line2.find("''' Run setting for heroku comment it and localy uncomment it") != -1:
        line2 = line2.replace("''' Run setting for heroku comment","#''' Run setting for heroku comment")    
    file_write = open("hellodjango/settings.py","w")
    file_write.write(line2)
    file_write.close()

def changegitConfigfile_wsgi():
    line = ""
    line2 = ""
    file_readw = open("hellodjango/wsgi.py","r")
    line = file_readw.read()
    file_readw.close()
    if line.find("#''' RunLocaly Comment and  Uncomment Run Heroku(Do not change this comment line)") != -1:
        line2 = line.replace("#''' RunLocaly Comment and", "''' RunLocaly Comment and")
    file_write = open("hellodjango/wsgi.py","w")
    file_write.write(line2)
    file_write.close()    


       
if __name__ == "__main__":
    changegitConfigfile_setting()
    changegitConfigfile_wsgi()
    #if len(sys.argv) == 3:
    #    changegitConfigfile() 
        #proc = Popen(['bash',sys.argv[1]], stdin=PIPE)
        #proc.communicate('Y')
        #revertChnagetoconfigfile()
        #proc = Popen(['bash',sys.argv[2]], stdin=PIPE)
        #proc.communicate('Y')
    #else:
    #    print "This need to be in Clone dir and Bash scripts are not provided"
    #    print "python Changedotgitconfig.py \"gitpull script\" \"run foreman script\" "     

