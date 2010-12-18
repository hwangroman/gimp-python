#! /usr/bin/env python
from gimpfu import *
import os

def run(*args):
    """Generated icons with different numbers using template"""
    template_name, num, prefix, output_dir = args

    output_dir = os.path.expanduser('~/' + output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    for i in xrange(1, num+1):
        im = pdb.gimp_file_load(template_name, template_name)


        # Suppose the name of layer in 'Text'
        text_layer = filter(lambda x: x.name == 'Text', im.layers)[0]
        pdb.gimp_text_layer_set_text(text_layer, str(i))


        # We can save only one layer at time
        # Merger visible layers in one
        merged = pdb.gimp_image_merge_visible_layers(im, 0)

        output_filename = "%s%d.png" % (prefix, i)
        full_output_filename = os.path.join(output_dir, output_filename)

        pdb.file_png_save_defaults(im, merged, full_output_filename, full_output_filename) 

    print "Finished"


register(
    "chobo_icon_gen", "", "", "", "", "",
    "<Toolbox>/Xtns/Languages/Python-Fu/_Chobo Scripts/_Icon Generator", "",
    [
    (PF_FILE, "arg0", "Template file", ""),
    (PF_INT,    "arg1", "Maximum number of icons to create", 29),
    (PF_STRING, "arg3", "Output file prefix", ""),
    (PF_STRING, "arg4", "Output directory (relative to user's home)", ""),
    ],
    [],
    run 
    )

main()
