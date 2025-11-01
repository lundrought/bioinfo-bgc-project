#!/bin/bash

input_directory="../genomes"

for fasta_file in "$input_directory"/Aspergillus*.fasta; do
  if [[ -e "$fasta_file" ]]; then
    echo "Processing $fasta_file..."
    deepbgc pipeline "$fasta_file" --output "${fasta_file}_output"
    echo "Completed $fasta_file"
  else
    echo "No matching files."
    break
  fi
done
