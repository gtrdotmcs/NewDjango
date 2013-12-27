import sys
from subprocess import Popen, PIPE

global line

def changegitConfigfile():
    global line
    file_read = open("setting.py","r")
    #previousline = ""
    line = file_read.read()
    file_read.close()
    line2 = line.replace("TalentBeat@bitbucket", "TalentBeat:Talent_123!@bitbucket")
    #file_write = open(".git/config","w")
    #file_write.write(line2)
    #file_write.close()

def revertChnagetoconfigfile():    
    global line
    print line
    #file_write = open(".git/config","w")
    #file_write.write(line)
    #file_write.close()
    
       
if __name__ == "__main__":
    
    if len(sys.argv) == 3:
        changegitConfigfile() 
        proc = Popen(['bash',sys.argv[1]], stdin=PIPE)
        proc.communicate('Y')
        revertChnagetoconfigfile()
        proc = Popen(['bash',sys.argv[2]], stdin=PIPE)
        proc.communicate('Y')
    else:
        print "This need to be in Clone dir and Bash scripts are not provided"
        print "python Changedotgitconfig.py \"gitpull script\" \"run foreman script\" "     

