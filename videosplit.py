import sys
import os

# Check to see if the input filename is passed
if (len(sys.argv) !=  2):
    print ("ERROR: No input filename specified")
    exit(-1)

# Open up the input filename
try:
    file_object = open(sys.argv[1],"r")
except IOError as e:
    print("Error: "+str(e))
    exit(-1)




# Read the first line.   This line should contain the input video filename
fn=file_object.readline().replace("\n","")
# Split up the input filename into both an extension and filename prefix.
filename = fn.rsplit('.', 1)[0]
extension = fn.rsplit('.', 1)[1]

# Counter is used for the new file name
counter = 1

# Process each line in the file
for line in file_object:

    # Remove the newline character, and split the file into both fields (Start Time and End Time)
    words = line.replace("\n","").split(" ")
    print ("----------------------------------")
    print ("Splitting "+fn+" between: "+words[0]+" and "+words[1]+" using the following command:")

    command="ffmpeg -i "+ fn+" -vcodec copy -acodec copy -ss "+words[0]+" -to "+words[1]+" "+filename+"-part\ "+str(counter)+"."+extension
    print("'"+command+"'")

    # Execute the command

    os.system(command)
    counter+=1

# Close the file
file_object.close()


