#All domains from hmmscan tblout to protein-level GFF3:
#python hmmscan2gff3.py -f reference.fasta -t hmmscan_result.out -o all_domains.gff3
#Only keep the best scoring domain:
#python hmmscan2gff3.py -f reference.fasta -t hmmscan_result.out -o best_domains.gff3 -b

import re
import argparse
import pandas as pd

def parse_fasta_headers(fasta_file):
    mapping = {}
    with open(fasta_file) as f:
        for line in f:
            if line.startswith(">"):
                parts = line[1:].split()
                query_id = parts[0]
                transcript_match = re.search(r"OriTrascriptID=([^\t]+)", line)
                gene_match = re.search(r"OriGeneID=([^\t]+)", line)
                transcript_id = transcript_match.group(1) if transcript_match else query_id
                gene_id = gene_match.group(1) if gene_match else transcript_id
                mapping[query_id] = {
                    "transcript_id": transcript_id,
                    "gene_id": gene_id
                }
    return mapping

def parse_hmmscan_tblout(tblout_file):
    with open(tblout_file) as f:
        lines = [line for line in f if not line.startswith("#") and line.strip()]
    
    records = [line.strip().split(None, 22)[:22] for line in lines]
    columns = [
        "target_name", "target_accession", "tlen",
        "query_name", "query_accession", "qlen",
        "E_value_full", "score_full", "bias_full",
        "domain_num", "domain_total", "c_Evalue",
        "i_Evalue", "score", "bias",
        "hmm_from", "hmm_to", "ali_from", "ali_to",
        "env_from", "env_to", "acc"
    ]
    df = pd.DataFrame(records, columns=columns)
    df["ali_from"] = df["ali_from"].astype(int)
    df["ali_to"] = df["ali_to"].astype(int)
    df["score"] = df["score"].astype(float)
    return df

def filter_best_hits(df):
    """Keep only the best scoring domain per query_name."""
    return df.sort_values("score", ascending=False).groupby("query_name", as_index=False).first()

def create_gff3(df, mapping, output_file):
    gff_lines = ["##gff-version 3"]
    for _, row in df.iterrows():
        query = row["query_name"]
        domain = row["target_name"]
        start = row["ali_from"]
        end = row["ali_to"]
        score = row["score"]
        domain_num = row["domain_num"]

        transcript_id = mapping.get(query, {}).get("transcript_id", query)
        domain_id = f"{domain}_{domain_num}"
        attributes = f"ID={domain_id};Name={domain};Parent={transcript_id}"
        gff_line = f"{query}\tHMMER\tprotein_domain\t{start}\t{end}\t{score}\t.\t.\t{attributes}"
        gff_lines.append(gff_line)

    with open(output_file, "w") as f:
        f.write("\n".join(gff_lines))
    print(f"GFF3 file written to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert hmmscan tblout to protein-level GFF3.")
    parser.add_argument("-f", "--fasta", required=True, help="Protein FASTA file with transcript info.")
    parser.add_argument("-t", "--tblout", required=True, help="hmmscan --tblout output file.")
    parser.add_argument("-o", "--output", required=True, help="Output GFF3 file.")
    parser.add_argument("-b", "--best-only", action="store_true", help="Only keep the best scoring domain per protein.")

    args = parser.parse_args()

    mapping = parse_fasta_headers(args.fasta)
    df = parse_hmmscan_tblout(args.tblout)
    
    if args.best_only:
        df = filter_best_hits(df)

    create_gff3(df, mapping, args.output)

if __name__ == "__main__":
    main()
