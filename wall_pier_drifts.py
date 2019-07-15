"""
Title: LS-DYNA wall drift FAST-TCF script generator
Input: csv with wall pier info: top node ID, bottom node ID, vertical dist btwn top and bottom nodes
Process: Create a FAST-TCF script using input data
Output: FAST-TCF script: walldrifts.inp
Python Version: 3.6
Script Version: 0.0.1
"""


wallinputs = r'J:\S-F\230000\238558-00\4 Internal Project Data\4-04 Calculations\Struct\97 - LsDyna\scripts\piers.csv'
outfile = r'J:\S-F\230000\238558-00\4 Internal Project Data\4-04 Calculations\Struct\97 - LsDyna\scripts\walldrifts.inp'

import numpy as np

inputs = np.genfromtxt(wallinputs, dtype=str, skip_header=1, delimiter=',')

nwalls = np.shape(inputs)[0]

colors = ['white','red','green','blue','cyan','magenta','yellow','orange','purple']

script_walls = []

for i in range(nwalls):
  wallID = inputs[i,0]
  topnode = inputs[i,1]
  botnode = inputs[i,2]
  height = inputs[i,3]
  direction = inputs[i,5]

  scriptadd = ['node '+topnode+' displacement '+direction+' tag curve_'+str(i*4+1),
               'node '+botnode+' displacement '+direction+' tag curve_'+str(i*4+2),
               'operation sub curve_'+str(i*4+2)+' curve_'+str(i*4+1)+' tag curve_'+str(i*4+3),
               'operation div curve_'+str(i*4+3)+' '+height+' tag curve_'+str(i*4+4),
               'delete curve_'+str(i*4+1)+' curve_'+str(i*4+2)+' curve_'+str(i*4+3),
               'label curve_'+str(i*4+4)+'  '+wallID+' drift ratio',
               'stylec curve_'+str(i*4+4)+' '+colors[i%len(colors)]+',default,solid,circle,1',
               '#']

  script_walls.extend(scriptadd)


script_start = ['# Program:  FASTTCF',
                '# Filetype:  Postscript',
                '# Filename:  script_output.png',
                '#',
                '# Built in variables:',
                '# ==================',
                '# $ftcf_script: Name of the FAST-TCF that is being run.',
                '# $ftcf_script_dir: Name of the FAST-TCF directory.',
                '# $ftcf_dir: Name of the current working directory.',
                '# $ftcf_path: Full pathname of the current working directory.',
                '# $ftcf_startin_dir: Directory T/HIS was started from.',
                '#',
                '# $run_name: Basename of the key file for the first model.',
                '# $run_dir: Full pathname of output file directory.',
                '# $run_title: Title of the analysis found in the output files.',
                '#',
                '# If a script refers to multiple models then, $run_nameN,',
                '# $run_dirN, $run_titleN (where N is the model number) can',
                '# be used for each model.',
                '#',
                'version 16.0',
                '#',
                '# Create additional graphs',
                '#',
                'layout graph total  1',
                '#',
                '# Setup page layouts',
                '#',
                'layout page wide',
                '#',
                '# Setup toolbar visibility',
                '#',
                'layout graphs toolbar show',
                '#',
                '# Remove graphs from all pages',
                '#',
                'layout page all none',
                'layout page 1 add graph  1',
                'layout page 1 graph  1 position 0.00,-.08 1.00,0.45',
                '#',
                '# Setup axis positions and properties',
                '#',
                'layout graph 1 axis position auto auto auto auto',
                'layout graph 1 x-axis format automatic',
                'layout graph 1 x-axis precision 1',
                'layout graph 1 y-axis format automatic',
                'layout graph 1 y-axis precision 1',
                '#',
                '# Setup legend format and position',
                '#',
                'layout graph 1 legend format column',
                'layout graph 1 legend columns 2',
                '#',
                '#',
                '# Read data from models and files',
                '#',
                'model none',
                'model 1']

script_end = ['#',
              'condense',
              '#',
              '# Curve and Legend Properties',
              '#',
              'properties format font Default 14 foreground',
              'properties format background background',
              'properties format border foreground off',
              'properties format border fine',
              'properties format arrow off',
              'properties format transparency 0',
              'properties format number y_only',
              'properties format value scientific',
              'properties format precision 3',
              '#',
              'properties legend format append',
              'properties legend * ## maximum off',
              'properties legend * ## minimum off',
              'properties legend * ## average off',
              'properties legend * ## hic off',
              'properties legend * ## clip off',
              'properties legend * ## thiv off',
              'properties legend * ## phd off',
              '#',
              'properties curves format off',
              'properties curves summary smaximum off',
              'properties curves summary sminimum off',
              'properties curves summary lmaximum off',
              'properties curves summary lminimum off',
              'properties curves * ## smaximum off',
              'properties curves * ## lmaximum off',
              'properties curves * ## sminimum off',
              'properties curves * ## lminimum off',
              '#',
              '# Select graph  1',
              '#',
              'layout graph select none',
              'layout graph select  1',
              '#',
              '# Plot setup',
              '#',
              'setup \\',
              '        Title "Wall pier rotation (ratio)" \\',
              '        title_on \\',
              '        x_label "Time" \\',
              '        x_label manual \\',
              '        x_label on \\',
              '        x_unit auto \\',
              '        x_unit on \\',
              '        y_label "Drift ratio" \\',
              '        y_label manual \\',
              '        y_label on \\',
              '        y_unit auto \\',
              '        y_unit on \\',
              '        y2_label auto \\',
              '        y2_label on \\',
              '        y2_unit auto \\',
              '        y2_unit on \\',
              '        x_min auto\\',
              '        x_max auto\\',
              '        y_min auto\\',
              '        y_max auto\\',
              '        y2_min auto\\',
              '        y2_max auto\\',
              '        y2_align off \\',
              '        axis normal \\',
              '        axis foreground\\',
              '        double off \\',
              '        border on \\',
              '        border normal \\',
              '        border foreground\\',
              '        axis top on \\',
              '        axis right on \\',
              '        background black\\',
              '        foreground white\\',
              '        grid on \\',
              '        grid fine \\',
              '        grid foreground\\',
              '        symbols off \\',
              '        solid off \\',
              '        line normal \\',
              '        line on \\',
              '        fix off \\',
              '        xlin \\',
              '        ylin \\',
              '        y2lin \\',
              '        mp auto \\',
              '        prefix id \\',
              '        Xauto \\',
              '        Yauto \\',
              '        font title Default 14 foreground \\',
              '        font xlabel Default 14 foreground \\',
              '        font ylabel Default 14 foreground \\',
              '        font y2label Default 14 foreground \\',
              '        font legend Default 14 foreground \\',
              '        font xunit Default 14 foreground \\',
              '        font yunit Default 14 foreground \\',
              '        font y2unit Default 14 foreground',
              '#',
              'display curve_*',
              '#',
              'prefix model  1 M1',
              '#',
              '# Set all graphs active',
              '#',
              'layout graph select all'
              '#'
              'csv2 wallPierDrifts.csv curve_* auto']

# Set up output file name and write file

with open(outfile, 'w') as writeout:
  for line in script_start:
    writeout.write(line+'\n')
  for line in script_walls:
    writeout.write(line+'\n')
  for line in script_end:
    writeout.write(line+'\n')
