"""
Assignments 2
I hope that you enjoyed the first exercise and discussion. This next one is one of my favorites, in that it uses the "/etc/passwd" file on Unix systems, which I find convenient for a large number of demonstrations.

 /etc/passwd to dict

 This exercise assumes that you have access to a copy of /etc/passwd, the file in which basic user information is stored on Unix computers. If you don't, then you can likely find such a file by searching for "/etc/passwd example" on the Web. The format is:

     nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
     root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
     daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
      
      In other words, each line is a set of fields, separated by colon (:) characters. The first field is the username, and the third field is the ID of the user. Thus, on my system, the nobody user has ID -2, the root user has ID 0, and the daemon user has ID 1.  You can ignore all but the first and third fields in the file.
       
       There is one exception to this format: A line that begins with a # character is a comment, and should be ignored by the parser.
        
        For this exercise, you must create a dictionary based on /etc/passwd, in which the dict's keys are usernames and the values are the numeric IDs of those users. You should then iterate through this dict, displaying one username and user ID on each line in alphabetical order.

"""

f = open("/etc/passwd")
lines = f.readlines()
passwd_dict = {}
for line in lines:
    if line.startswith("#"):
        continue
    else:
        fields = line.split(":")
        passwd_dict[fields[0]] = fields[2]

for key in sorted(passwd_dict):
    print "%s: %s" %(key, passwd_dict[key])
