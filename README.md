# fast_dump.py
The script downloads SRA files and generates fastq files for specified SRA numbers corresponding to different species.
The sra_species dictionary maps SRA numbers to their respective species names.
The script iterates through the dictionary and performs the following actions for each species:
Downloads the .sra files using prefetch.
Generates fastq files using fastq-dump with the --split-files option to separate paired-end reads.
Information about the commands being executed is printed for each step.
How to Use for GitHub:

Save the script in a Python file, e.g., download_fastq.py.
Make the script executable by running chmod +x download_fastq.py.
Commit the script to your GitHub repository.
Provide usage instructions in your repository's README, specifying that users need to have prefetch and fastq-dump installed.
Users can then clone the repository, execute the script, and download the necessary data.
