import subprocess

# SRA numbers and corresponding species names
sra_species = {
    "SRR1024068": "Unknown_species",
    "SRR26190532": "Aptostichus hedinorum",
    "SRR26190608": "Aptostichus stanfordianus",
    "SRR1514884": "Cyclocosmia truncata",
    "SRR26190583": "Promyrmekiaphila clathrata",
    "SRR26190502": "Promyrmekiaphila winneme"
}

# Iterate over SRA numbers and species
for sra_id, species in sra_species.items():
    # Print information about the current download
    print(f"Currently downloading: {species} - {sra_id}")

    # Use prefetch to download the .sra files
    prefetch_command = f"prefetch {sra_id}"
    print(f"The command used was: {prefetch_command}")
    subprocess.call(prefetch_command, shell=True)

    # Print information about the current fastq dump
    print(f"Generating fastq for: {species} - {sra_id}")

    # Use fastq-dump to extract .sra files into a folder named 'fastq' with split-files option
    fastq_dump_command = (
        f"fastq-dump --outdir fastq --gzip --skip-technical "
        f"--readids --read-filter pass --dumpbase --split-3 --clip "
        f"--split-files ~/ncbi/public/sra/{sra_id}.sra"
    )
    print(f"The command used was: {fastq_dump_command}")
    subprocess.call(fastq_dump_command, shell=True)
