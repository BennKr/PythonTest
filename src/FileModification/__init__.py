import os

s= os.getenv("JAVA_HOME")
print(s)
servers = ["", ""]

def printStuff():
    print("doIT")
    
def calc2Values(a, b):
    return a+b;

def connectRemoteShare(server, username,password):
    import win32api
    import win32net
    import win32netcon,win32wnet

    try:
        win32wnet.WNetAddConnection2(win32netcon.RESOURCETYPE_DISK, 'Z:','\\\\' + server + '\D$', None, username,password, 0)
        print ("connection established successfully")
    except:
        print("connection not established")
        

java_home = "for %i in (java.exe) do @echo.   %~$PATH:i"
def getJavaHome(server, user, password):
    import winrm
    # Create winrm connection.
    sess = winrm.Session(server, auth=(user, password), transport='kerberos')
    result = sess.run_cmd(java_home, [])
    return result

def replaceInFile(file, reqExp, replaceString):
    import re
    with open (file, 'r' ) as f:
        content = f.read()
    quotedString = replaceString.replace("\\b", "\\\\b")
    content_new = re.sub(reqExp, quotedString, content)

    with open(file, 'w') as f:
        f.write(content_new)

print(os.popen(java_home).read())

def fixJAvaUpgradeProblem(servers, user, password):
    for server in servers:
        connectRemoteShare(server,user, password)
        java_home = getJavaHome(server, user, password)
        replaceInFile("C:\\temp\jenkins.xml", "<executable>(.*)</executable>", "<executable>" + java_home + "</executable>")
