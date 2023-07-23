def create_input_files(input_string):
    # Split the input string into lines
    lines = input_string.split('\n')

    # Initialize an empty list to hold the current subcategories
    subcategories = []

    # Iterate over the lines in the input string
    for line in lines:
        # If the line is not blank, it's either a category or a subcategory
        if line.strip():
            # If the line is not indented, it's a category
            if not line.startswith('    '):
                category = line.strip()
                # If there are current subcategories, it's the end of the previous category
                if subcategories:
                    # Create the input file for the previous category
                    with open(f'{category}_{subcategories[0]}.txt', 'w') as f:
                        for subcategory in subcategories:
                            f.write(f'{subcategory}\n{subcategory}\n5 g\n')
                    # Reset the current subcategories
                    subcategories = []
            # If the line is indented, it's a subcategory
            else:
                subcategories.append(line.strip())
    # If there are remaining subcategories after the last line, it's the end of the last category
    if subcategories:
        # Create the input file for the last category
        with open(f'{category}_{subcategories[0]}.txt', 'w') as f:
            for subcategory in subcategories:
                f.write(f'{subcategory}\n{subcategory}\n5 g\n')

                
# Call the function with the input string
create_input_files("""Hedelmä- ja marjaruoat

    Tuoreet hedelmät
    Hedelmä- ja marjasalaatit
    Marjat
    Marjakiisselit, -keitot
    Hedelmä- ja marjaruoka
    Täysmehut

Palkokasviruoat

    Palkokasvit
    Palkokasvivalmiste
    Palkokasviruoat
    Palkokasvikeitot
    Palkokasvikastikkeet

Kasvisruoat

    Tuoreet kasvikset
    Kypsennetyt kasvikset
    Kasvispääruoat
    Kasviskeitot
    Kasviskastikkeet
    Sieniruoat
    Kasvissäilykkeet
    Kasvismehut

Salaatit

    Kasvissalaatit
    Yhdistelmäsalaatit
    Majoneesisalaatti

Perunat

    Keitetyt perunat
    Perunaruoat
    Perunat, paistetut

Vilja ja leivontatuotteet

    Sekaleipä, jyväleipä
    Vehnäleipä
    Ruisleipä
    Kahvileipä
    Leivonnainen makea
    Leivonnainen suolainen
    Pannukakut
    Voileivät, hampurilaiset
    Makeat keksit
    Voileipäkeksit
    Riisilisäke
    Pasta
    Puuro
    Aamiaisviljavalmisteet
    Viljapatukat
    Pizza
    Jauhot

Maidot ja maitoruoat

    Maitojuoma rasvaton
    Maitojuomat <2%
    Maitojuomat >2%
    Piimä
    Kerma
    Jogurtit
    Viili
    Rahka
    Muut hapanmaitotuotteet
    Juusto, kypsytetty
    Tuorejuustot
    Sulatejuustot
    Jäätelö
    Maitojälkiruoat
    Maitokastikkeet

Rasva ja rasvavalmisteet

    Voi
    Eläinrasva
    Rasvaseokset >= 55 %
    Rasvaseokset < 55 %
    Margariini <55%
    Margariini >= 55%
    Ruoanvalmistusrasva
    Salaatinkastikkeet
    Öljy

Kananmunat

    Kananmuna
    Kananmunaruoat

Kalaruoat

    Kalat
    Kalavalmiste
    Kalakeitot
    Kalaruoat
    Kalakastike
    Äyriäiset
    Äyriäisruoat
    Äyriäiskeitto
    Äyriäiskastike

Liharuoat

    Pihvit, kyljykset
    Lihakeitot
    Liharuoat
    Linnut
    Linturuoat
    Lintukeitot
    Lintukastikkeet
    Lihavalmisteet
    Makkaraleikkeleet
    Lihaleikkeleet
    Makkarat
    Sisäelinruoat
    Lihakastike

Juomat

    Kahvi
    Tee
    Vedet
    Mehujuomat
    Virvoitusjuomat, sokeroidut
    Keinotekoisesti makeutetut juo
    Urheilujuomat
    Muu juoma

Alkoholijuomat

    Oluet
    Siiderit
    Viinit
    Väkevät viinat
    Muut alkoholijuomat

Sokeri, makeiset

    Sokerit, siirapit
    Makeiset
    Suklaa
    Hillot, marmeladit

Sekalaiset

    Mausteet
    Maustekastikkeet
    Kastikkeet
    Jälkiruokakastike
    Sekalaiset ruoka-aineet

Naposteltavat

    Suolaiset naposteltavat
    Pähkinät

Lastenruoat

    Baby liharuoka
    Baby kalaruoka
    Baby hedelmävalmiste
    Baby lasten kasvisvalmiste

Äidinmaito ja äidinmaitokorvik

    Äidinmaito, tav.korvikkeet

Ravintovalmisteet

    Ravintoainevalmisteet
    Ateriankorvikkeet
    Urheiluvalmisteet""")
