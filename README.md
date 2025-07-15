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

Install `pandas` using pip if it's not already installed:

```bash
pip install pandas```

## 🚀 Usage

```bash
python hmmer2gff3.py -f <protein_fasta.fasta> -t <hmmscan.tblout> -o <output.gff3> [-b]```

---

## 📦 Example

Generate a GFF3 with **all domain hits**:

```bash
python hmmer2gff3.py -f Abo_protein_1B_fasta.fasta -t Abo_1B_protein.out -o all_domains.gff3```
