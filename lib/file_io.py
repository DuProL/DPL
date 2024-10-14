# Handles file IO

if __name__ != "__dpl__":
    raise Exception("Must be imported by a DPL script!")

temp = {
    "version":0.1,
    "docs":"""[File IO Module]

open_file path mode
read_file file_object -> contents
write_file file_object contents
close file_object
"""
}

@add_func(temp)
def open_file(frame, file, file_path, mode):
    "Open a file."
    if file == "__main__":
        file = "."
    return open(os.path.join(os.path.basename(file), file_path), mode),

@add_func(temp)
def read_file(frame, file, file_obj):
    return file_obj.read(),

@add_func(temp)
def write_file(frame, file, file_obj, content):
    return file_obj.write(content),

@add_func(temp)
def close(frame, file, file_obj):
    file_obj.close()

frame[-1]["file_io"] = temp