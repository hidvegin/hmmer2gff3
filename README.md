# HMMER2GFF3

A Python script to convert [HMMER](http://hmmer.org/) `--tblout` output from `hmmscan` into a protein-level GFF3 file using information from a protein FASTA file.

This tool is particularly useful for annotating protein domains on predicted protein-coding genes, based on domain hits identified by `hmmscan`.

---

## 🔧 Features

- Parses `hmmscan` `--tblout` output file
- Extracts transcript and gene information from protein FASTA headers
- Outputs GFF3 file with domain coordinates at the protein level
- Optional filtering to include **only the best-scoring domain** per protein

---

## 🐍 Requirements

- Python 3.x
- [`pandas`](https://pandas.pydata.org/) library

Install `pandas` using pip if it's not already installed.

