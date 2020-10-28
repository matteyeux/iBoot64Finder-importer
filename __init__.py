from binaryninja import *

def import_iboot(binaryView):
    # This is the string that's displayed in the pop-up dialogue by binja itself
    iboot64 = OpenFileNameField("Import iBoot64Finder symbols")

    # Sets the title of the dialogue and gets the input field value
    get_form_input([iboot64], "Import symbols")

    if iboot64.result != '':
        real_file = iboot64.result

    if real_file is None:
        return -1

    iboot_functions = {}
    with open(real_file) as iboot:
        for line in iboot.readlines():
            if "=" in line:
                print(line.split())
                iboot_function = line.split()[1]
                str_addr = line.split()[3]
                iboot_addr = int(str_addr, 0)
                iboot_functions[iboot_function] = iboot_addr

    for function in binaryView.functions:
        for iboot_function in iboot_functions:
            if function.start == iboot_functions[iboot_function]:
                function.name = iboot_function
                print(iboot_function)


# Registers the plugin with binja and allows us to specify the function that the binaryview is passed to.
PluginCommand.register("Import iBoot64Finder", "Import iBoot64Finder symbols", import_iboot)
