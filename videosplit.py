import sys
import os


print ("Video Split")
print ("===========")
# Check to see if the input filename is passed
if (len(sys.argv) !=  2):
    print ("ERROR: No input filename specified")
    filename = input("Enter the name of the input filename --> ")
else:
    filename=sys.argv[1]

# Open up the input filename
try:
    file_object = open(filename,"r")
except IOError as e:
    print("Error: "+str(e))
    exit(-1)




# Read the first line.   This line should contain the input video filename
fn=file_object.readline().replace("\n","")

# Split up the input filename into both an extension and filename prefix.
filename = fn.rsplit('.', 1)[0]
extension = fn.rsplit('.', 1)[1]

if not os.path.exists(fn):
    print(f"Error: Can't open {fn}")
    exit(-1)

# Counter is used for the new file name
counter = 1

# Process each line in the file
for line in file_object:

    cleaned = line.replace("\n","")
    # Remove the newline character, and split the file into both fields (Start Time and End Time)
    words = cleaned.split()

    if len(words)<2:
        print(f"WARNING: Ignoring Line '{cleaned}', Doesn't contain time stamps.")

    else:
        if len(words) >=3:
            output_filename=words[2]+"."+extension
        else:
            output_filename=filename+"-part-"+str(counter)+"."+extension
            counter += 1
        print ("----------------------------------")
        print ("Splitting "+fn+" between: "+words[0]+" and "+words[1]+" into "+output_filename)


        command="ffmpeg -loglevel warning -i "+ fn+" -vcodec copy -acodec copy -ss "+words[0]+" -to "+words[1]+" "+output_filename
        print("'"+command+"'")

        # Execute the command

        os.system(command)


# Close the file
file_object.close()


