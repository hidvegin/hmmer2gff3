# hmmer2gff3

**hmmer2gff3** is a Python script that converts HMMER `hmmscan --tblout` output to protein-level GFF3 format.  
It supports exporting all detected domains or only the best-scoring domain per protein.

---

## 🚀 Usage

```bash
python hmmer2gff3.py -f <protein_fasta> -t <hmmscan_tblout> -o <output_gff3> [-b]
```

### **Required arguments**

- `-f`, `--fasta`  
  Protein FASTA file containing transcript and gene information in the header.

- `-t`, `--tblout`  
  Output file from `hmmscan` generated with the `--tblout` option.

- `-o`, `--output`  
  Output GFF3 file name.

### **Optional arguments**

- `-b`, `--best-only`  
  Only keep the best scoring domain per protein.

---

## 📄 Example

Export **all domains**:
```bash
python hmmer2gff3.py -f Abo_protein_1B_fasta.fasta -t Abo_1B_protein.out -o all_domains.gff3
```

Export **only the best-scoring domain** per protein:
```bash
python hmmer2gff3.py -f Abo_protein_1B_fasta.fasta -t Abo_1B_protein.out -o best_domains.gff3 -b
```

---

## 📝 Output

The script generates a GFF3 file with protein domain annotations.  
Each feature includes the domain name, ID, and parent transcript.

---

## 📦 Requirements

- Python 3
- pandas

Install dependencies:
```bash
pip install pandas
```

---

## ⚡ Notes

- The script expects the FASTA headers to contain `OriTrascriptID` and `OriGeneID` fields.
- The GFF3 output includes domain coordinates, scores, and parent transcript information.

---

## 👤 Author

Norbert Hidvégi

---

If you have questions or encounter issues, please open an issue on the repository.

---
