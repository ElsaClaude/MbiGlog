def parser(fasta_file):
    with open(fasta_file, 'r') as fasta:
        txt = fasta.read()
        txt_tab = txt.split()
        id_gene = txt_tab[0].split(">")[1]
        header = txt.split(",")
        nom_gene = header[0]
        nom_gene = nom_gene.split()
        nom_gene = nom_gene[1:]
        nom_gene = " ".join(nom_gene)
        sequence = txt.split("\n")[1:]
        sequence = "".join(sequence)
        return {"id_gene" : id_gene, "nom_gene": nom_gene, "sequence": sequence}

if __name__ == "__main__":
    import os
    dict = parser("./fasta/arabi.fasta")
    print( "id : " , dict['id_gene'])
    print("nom : " , dict['nom_gene'])
    print("sequence : \n",dict['sequence'])


