# Imaging_data_registration

The notebook make_average_stacks_py3 allows averaging of several brain stacks to produce a reference brain for the given expression pattern.
Can be used for registration of individual brain scans to this reference brain with either Computational Morphometry Toolkit (CMTK) or Advanced Normalization Tools (ANTs)

See links:

https://www.nitrc.org/projects/cmtk/

http://stnava.github.io/ANTs/


ANTspy_run.py allows running  ANTsPy. Depending on your data you may need a lot of RAM to run the registration. Tested on Linux server with 64GB RAM and supercomputer with many nodes (3424 compute nodes, 529 TB RAM). See for more details and requirements: https://github.com/ANTsX/ANTsPy
