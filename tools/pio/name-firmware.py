# Inspired by: https://github.com/arendst/Tasmota/blob/development/pio/name-firmware.py
# Thanks Theo & Jason2866 :)

Import('env')
import os
import shutil

OUTPUT_DIR = "build_output{}".format(os.path.sep)

def copy_to_build_output(sourcedir, variant, file_suffix):
    in_file = "{}{}".format(variant, file_suffix)
    if ".elf" in file_suffix:
        out_file = "{}elf{}{}".format(OUTPUT_DIR, os.path.sep, in_file)
    else:
        out_file = "{}bin{}{}".format(OUTPUT_DIR, os.path.sep, in_file)

    if os.path.isfile(out_file):
        os.remove(out_file)

    full_in_file = os.path.join(sourcedir, in_file)
    #print("\u001b[33m in file : \u001b[0m  {}".format(full_in_file))
    
    if os.path.isfile(full_in_file):
        print("\u001b[33m copy to: \u001b[0m  {}".format(out_file))
        shutil.copy(full_in_file, out_file)



def bin_elf_copy(source, target, env):
    variant = env['PROGNAME']
    
    # check if output directories exist and create if necessary
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    for d in ['bin', 'elf']:
        if not os.path.isdir("{}{}".format(OUTPUT_DIR, d)):
            os.mkdir("{}{}".format(OUTPUT_DIR, d))

    split_path = str(source[0]).rsplit(os.path.sep, 1)

    for suff in [".elf", ".bin", ".bin.gz", "-factory.bin"]:
        copy_to_build_output(split_path[0], variant, suff)


env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", [bin_elf_copy])
