filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
for files in filenames:
    if files.endswith("hpp"):
        i = filenames.index(files)
        sep_filename = files.split(".")
        main_filename = sep_filename[0]
        newExt = "h"
        new_filename = "{}.{}".format(main_filename,newExt)
        filenames[i] = new_filename
        newfilenames = filenames

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]