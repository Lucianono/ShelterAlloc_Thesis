


import pandas as pd

# Your big dictionary here
data = { 
     'initial': {'Balite': 'San Marcos National H.S.', 'Balungao': 'F. Mendoza Memorial Elem Sch.', 'Buguion': 'San Marcos National H.S.', 'Bulusan': 'San Marcos National H.S.', 'Calizon': 'San Marcos National H.S.', 'Calumpang': 'San Marcos National H.S.', 'Caniogan': 'Doña Damiana Elem School', 'Corazon': 'Doña Damiana Elem School', 'Frances': 'Doña Damiana Elem School', 'Gatbuca': 'San Marcos National H.S.', 'Gugo': 'San Marcos National H.S.', 'Iba Este': 'F. Mendoza Memorial Elem Sch.', "Iba O'Este": 'San Marcos National H.S.', 'Longos': 'San Marcos National H.S.', 'Meysulao': 'Doña Damiana Elem School', 'Meyto': 'Mun. Covered Court', 'Palimbang': 'San Marcos National H.S.', 'Panducot': 'Mun. Covered Court', 'Pio Cruzcosa': 'San Marcos National H.S.', 'Poblacion': 'Doña Damiana Elem School', 'Pungo': 'San Marcos Elem. Sch.', 'San Jose': 'Barangay Hall Bulusan', 'San Marcos': 'Gugo E.C.', 'San Miguel': 'Doña Damiana Elem School', 'Santa Lucia': 'Gatbuca Basketball Court', 'Santo Niño': 'San Marcos National H.S.', 'Sapang Bayan': 'F. Mendoza Memorial Elem Sch.', 'Sergio Bayan': 'Balungao E.C.', 'Sucol': 'Mun. Covered Court'}
}

df = pd.DataFrame([
    {
        "Community": community,
        "Shelter Initial": initial_shelter
    }
    for community, initial_shelter in data['initial'].items()
])

# Save to Excel
df.to_excel("WORK_alloc.xlsx", index=False)
print("Excel file created: WORK_alloc.xlsx")
