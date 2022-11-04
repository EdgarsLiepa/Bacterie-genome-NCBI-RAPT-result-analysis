import csv
import sys
import os
from Bio import SeqIO
import pandas as pd

for root, dirs, files in os.walk("/home/edgars.liepa/Becteria result", topdown=False):    
    for name in dirs:
    
        # os.walk includes .git subdirectories. Only RAPT result folders needed, so rest should be ignored
        if ".git" in os.path.join(root, name):
            continue
    
        print('parse:',os.path.join(root, name))
        
        contigs = pd.DataFrame()

        for record in SeqIO.parse(os.path.join(root, name)+'/annot.gbk', "genbank"):

            print(record.id)
            products = []

            for feature in record.features:
                
                if ('product') in feature.qualifiers:
                    print(feature.type, feature.qualifiers['product'], feature.location)
                    product = feature.type + str(feature.qualifiers['product'])+ str(feature.location)
                    products.append(product)

        contigs = pd.concat([contigs, pd.DataFrame({record.id: products})], axis=1)
        contigs.to_excel(os.path.join(root, name)+"/geneProducts.xlsx")