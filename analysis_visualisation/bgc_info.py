#1 name: scaffold_n // start, end // label
#2 product_activity // product_class
#3 filtriranje (score > 0.7)
#4 zanimivi metaboliti ?
#5 cluster distribution

import os
import json
import pandas as pd


input_dir = "./json_files"
output_dir = "deepbgc_rezultati.csv"

bgc_data = []

for ime_dat in os.listdir(input_dir):
    pot_datoteke = os.path.join(input_dir, ime_dat)

    with open(pot_datoteke, 'r', encoding = "UTF-8") as datoteka: #r = read mode
        data = json.load(datoteka) #postane slovar

        seznam_records = data.get("records", [])
        for record in seznam_records:

            scaffold_ime = record.get("name")

            seznam_subregij = record.get("subregions", [])
            #print(seznam_subregij)
            for subregija in seznam_subregij:
                start = subregija.get("start")
                end = subregija.get("end")
                #label - majo vsi isti

                slovar_details = subregija.get("details", {})
               #print(seznam_podrobnosti)
                aktivnost = slovar_details.get("product_activity")
                razred = slovar_details.get("product_class")
                score = slovar_details.get("score")

                bgc_data.append({
                    "filename": ime_dat.replace(".antismash.json", ""),
                    "scaffold_name": scaffold_ime,
                    "start": start,
                    "end": end,
                    "product_activity": aktivnost,
                    "product_class": razred,
                    "score": score
                })

df = pd.DataFrame(bgc_data)
df.to_csv(output_dir, index=False)





                        
                    
                    







