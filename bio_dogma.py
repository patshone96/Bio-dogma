"""
This program has different modes. You can transcribe DNA to RNA,
translate DNA or RNA to amino acids, get the CG content of a sequence
and all the bases %. Also, from an amino acd sequence, you can check
the number and % of polar, non-polar, positively charge and negatively charged
amino acids and look out for specific amino acids on the sequence.

"""

def main():

    more = True
# Little introduction of the program modes

    while more == True:

        print("There are six modes to access:")
        print("")
        print("1. DNA to RNA")
        print("2. DNA to amino acids")
        print("3. RNA to amino acids")
        print("4. % of CG")
        print("5. % of different amino acids")
        print("6. Look out for specific amino acids")

    # We prompt the user for an input in order to determine which mode them want to use
        print("")
        mode = int(input("Please, enter your choice: "))

    # Depending on mode, the program prompts for different inputs and generates specific outputs
    # We use the if statement to code the different outputs

    # The first mode turns a DNA sequence into an RNA sequence

        if mode == 1:

            print("")
            print("You selected: 1. DNA to RNA")
            print("")
            # Prompt the user to know whether they want to load a file to be read or paste the code
            print("Do you have a .txt file containing your DNA sequence? (y for yes, n for no)")
            file_or_not = input("Answer: ")

            if file_or_not.lower() == "y":
                DNA = get_file()

            else:
                print("")
                # Prompt the user for a DNA sequence
                dna = input("Enter the DNA sequence: ")
                # Make sure the DNA sequence is all in upper case
                DNA = dna.upper()

            RNA = transcribe_DNA(DNA)

            print("")
            print("The RNA sequence is:")
            print("")
            print(RNA)

    # The second mode translates DNA into amino acids
        elif mode == 2:

            print("")
            print("You selected: 2. DNA to amino acids")
            print("")
            print("Do you have a .txt file containing your DNA sequence? (y for yes, n for no)")
            file_or_not = input("Answer: ")

            if file_or_not.lower() == "y":
                DNA = get_file()

            else:
                print("")
                dna = input("Enter the DNA sequence: ")
                DNA = dna.upper()

            amino_acids = translate_DNA(DNA)


            print(amino_acids)

    # The third mode translates RNA into amino acids
        elif mode == 3:

            print("")
            print("You selected: 3. RNA to amino acids")
            print("")
            print("Do you have a .txt file containing your RNA sequence? (y for yes, n for no)")
            file_or_not = input("Answer: ")

            if file_or_not.lower() == "y":
                RNA = get_file()

            else:
                print("")
                rna = input("Enter the RNA sequence: ")
                RNA = rna.upper()

            # We will use already build functions to turn RNA to amino acids
            # 1. Turn the RNA strand into DNA

            DNA = retrot(RNA)

            # 2. Using the DNA, get the amino acids using the already build functions

            amino_acids = translate_DNA(DNA)

            print(amino_acids)

    # The forth mode gives you the CG % of a given DNA sequence
        elif mode == 4:

            print("")
            print("You selected: 4. % of CG")
            print("")
            print("Do you have a .txt file containing your DNA sequence? (y for yes, n for no)")
            file_or_not = input("Answer: ")

            if file_or_not.lower() == "y":
                DNA = get_file()

            else:
                print("")
                dna = input("Enter the DNA sequence: ")
                DNA = dna.upper()

            # We use a function to check the ATCG/ CG % of the DNA sequence we provide

            ATCG_contain(DNA)

    # This mode takes a macromolecule sequence (DNA, RNA or amino acids) and, after some modifications, calculates
    # The % of polar, non_polar, positive and negative amino acids
        elif mode == 5:


            print("")
            print("You selected: 5. % of different amino acids")
            print("")
            # We prompt the user to know with what type of macromolecule they are working with
            print("Do you have a 1. DNA, 2. RNA or 3. amino acid sequence?")
            # Depending on the answer, the program has to do some transformations in order to get the amino-acids
            macro = input("Answer: ")


            # If the user is working with a DNA sequence, this has to be translated into amino acids
            if macro == "1":
                print("Do you have a .txt file containing a DNA sequence? (y for yes, n for no)")
                file_or_not = input("Answer: ")

                if file_or_not.lower() == "y":
                    DNA = get_file()

                else:
                    print("")
                    dna = input("Enter the DNA sequence: ")
                    DNA = dna.upper()

                amino_acids = translate_DNA(DNA)

            # If the user is working with an RNA sequence, this has to be translated into amino acids
            if macro == "2":
                print("Do you have a .txt file containing a RNA sequence? (y for yes, n for no)")
                file_or_not = input("Answer: ")

                if file_or_not.lower() == "y":
                    RNA = get_file()

                else:
                    print("")
                    rna = input("Enter the RNA sequence: ")
                    RNA = rna.upper()

                DNA = retrot(RNA)

                amino_acids = translate_DNA(DNA)

            # If the user is working with amino acids, no transformation is required

            if macro == "3":
                print("Do you have a .txt file containing a amino acid sequence? (y for yes, n for no)")
                file_or_not = input("Answer: ")

                if file_or_not.lower() == "y":
                    amino_acids = get_file()

                else:
                    print("")
                    amino_acids = input("Enter the amino acid sequence (3 letter format separated by hyphens): ")


                # Separate the aminoacids, removing the hyphens and storing them on a list

            amino_list = amino_acids.split('-')

            for ch in amino_list:
                ch.lower()
                ch.capitalize()

            # Function to count the number of amino acids with given properties (returns a list)
            propert_list = amino_counter(amino_list)

            # Function to count the number of amino acids with a given property (prints the list)
            number_of(propert_list)

        elif mode == 6:
            print("")
            print("You selected: 6. Look out for specific amino acids")
            print("")
            # We prompt the user to know with what type of macromolecule they are working with
            print("Do you have a 1. DNA, 2. RNA or 3. amino acid sequence?")
            # Depending on the answer, the program has to do some transformations in order to get the amino-acids
            macro = input("Answer: ")

            # If the user is working with a DNA sequence, this has to be translated into amino acids
            if macro == "1":
                print("Do you have a .txt file containing a DNA sequence? (y for yes, n for no)")
                file_or_not = input("Answer: ")

                if file_or_not.lower() == "y":
                    DNA = get_file()

                else:
                    print("")
                    dna = input("Enter the DNA sequence: ")
                    DNA = dna.upper()

                amino_acids = translate_DNA(DNA)

            # If the user is working with an RNA sequence, this has to be translated into amino acids
            if macro == "2":
                print("Do you have a .txt file containing a RNA sequence? (y for yes, n for no)")
                file_or_not = input("Answer: ")

                if file_or_not.lower() == "y":
                    RNA = get_file()

                else:
                    print("")
                    rna = input("Enter the RNA sequence: ")
                    RNA = rna.upper()

                DNA = retrot(RNA)

                amino_acids = translate_DNA(DNA)

            # If the user is working with amino acids, no transformation is required

            if macro == "3":
                print("Do you have a .txt file containing a amino acid sequence? (y for yes, n for no)")
                file_or_not = input("Answer: ")

                if file_or_not.lower() == "y":
                    amino_acids = get_file()

                else:
                    print("")
                    amino_acids = input("Enter the amino acid sequence (3 letter format separated by hyphens): ")


                # Separate the amino acids, removing the hyphens and storing them on a list

            amino_list = amino_acids.split('-')

            for ch in amino_list:
                ch.lower()
                ch.capitalize()

            # Function to count the number of amino acids with given properties (returns a list)
            propert_list = amino_counter(amino_list)

            total_amino = sum(propert_list[0 : len(propert_list)])


            # Count how many given aminoacids there are

            given_amino(amino_list, total_amino)

        else:
            print("Select a valid choice")
            
                
                
        print("")
        cont = input("Would you like to continue using this program? (Type y to continue, anything else to leave) ")
        print("")

        if cont.lower() != "y":
            more = False

    # To finish the program, the user has to enter something
    print("")
    input("Press any key to end the program")

# Gives how much of a given aminoacid there are on a provided sequence
def given_amino(list, total):

    again = True

    while again:
        print("")
        amin = input(("Type the name of the amino acid you'd like to check (3 letter format): "))
        amin = amin.lower()
        amin = amin.capitalize()

        if amin == "Total":
            print("")
            print("There are a total of " + str(len(list)) + " amino acids on the sequence provided")
            print("")
            one_more = input("Would you like to check a given amino acid? (type Y to continue, anything else to skip) ")

        else:
            percent = (list.count(amin) / total) * 100
            print("")
            print("There are " + str(list.count(amin)) + " " + str(amin) + " on the sequence provided")
            print("")
            print("This represents a " + str(percent) + "% of the total amino acids")
            print("")
            one_more = input("Would you like to check another amino acid? (type Y to continue, anything else to skip) ")

        if one_more.upper() != "Y":
            again = False

# Function to print the number of amino acids with a given property
def number_of(list):
    non_polar = list[0]
    polar = list[1]
    positive = list[2]
    negative = list[3]

    total = list[0] + list[1] + list[2] + list[3]

    print("")
    print("There are " + str(non_polar) + " non-polar aminoacids. This represents the "  + str(non_polar / total * 100) + "% of the sequence")
    print("")
    print("There are " + str(polar) + " polar aminoacids. This represents the "  + str(polar / total * 100) + "% of the sequence")
    print("")
    print("There are " + str(positive) + " aminoacids with positive charge. This represents the "  + str(positive / total * 100) + "% of the sequence")
    print("")
    print("There are " + str(negative) + " aminoacids with negative charge. This represents the "  + str(negative / total * 100) + "% of the sequence")
    print("")



# This function counts the number of a type of aminoacids and returns a list with the result
def amino_counter(amino_list):

    # We create variables to track the types of aas we encounter on a sequence


    non_polar = 0
    polar = 0
    positive = 0
    negative = 0

    for amin in amino_list:

        # We make sure the format of the aminoacids is correct so thr program can interpret them
        amin = amin.lower()
        amin = amin.capitalize()

        if amin == 'Gly' or amin == 'Ala' or amin == 'Val' or amin == 'Cys' or amin == 'Pro' or amin == 'Leu' or amin == 'Ile' or amin == 'Met' or amin == 'Trp' or amin == 'Phe':
            non_polar += 1

        if amin == 'Ser' or amin == 'Thr' or amin == 'Tyr' or amin == 'Asn' or amin == 'Gln':
            polar += 1

        if amin == 'Lys' or amin == 'Arg' or amin == 'His':
            positive += 1

        if amin == 'Asp' or amin == 'Glu':
            negative += 1

    #print(non_polar, polar, positive, negative)

    # Return the values of the variables in this order - non-polar, polar, posit and negat - as a list

    value_list = [non_polar, polar, positive, negative]

    return value_list

# This function calculates the bases % and the CG %
def ATCG_contain(sequence):


    Total = len(sequence)
    A = sequence.count("A")
    T = sequence.count("T")
    C = sequence.count("C")
    G = sequence.count("G")

    A_percent = (A / Total) * 100
    T_percent = (T / Total) * 100
    C_percent = (C / Total) * 100
    G_percent = (G / Total) * 100

    print("")
    print("There is a " + str(A_percent) + "% of A on the sequence")
    print("")
    print("There is a " + str(T_percent) + "% of T on the sequence")
    print("")
    print("There is a " + str(C_percent) + "% of C on the sequence")
    print("")
    print("There is a " + str(G_percent) + "% of G on the sequence")
    print("")
    print("The GC content of the sequence is " + str(C_percent + G_percent) + "%")
    print("")


# This function produces a complementary mRNA string from a provided DNA string
# A --> T
# U --> A
# C --> G
# G --> C

def retrot(RNA):
    RNA = RNA.replace("A", "T")
    RNA = RNA.replace("U", "A")

    # Now we have to do an intermediate step to transform Cs into Gs and vice-versa
    # Because if we turn one into the other, we would lose one of them
    # We use an intermediate step

    RNA = RNA.replace("C", "X")
    RNA = RNA.replace("G", "C")
    DNA = RNA.replace("X", "G")

    return DNA


def translate_DNA(DNA):

    # Splitting the string 'DNA' in chunks of 3 letters (AKA codons or, in this case, anti-codons)
    DNA_list = [DNA[i:i + 3] for i in range(0, len(DNA), 3)]


    amino_list = decod_loop(DNA_list)

    # We need to turn the amino_list into a string of amino acids
    amino_str = ""

    # This for-each loop runs through the amino_list, copying each amino acid into the amino_str variable
    # while adding a hyphen at the end, to separate the amino acids
    for amin in amino_list:
        amino_str += (amin + "-")


    # returns amino_str but trims the last hyphen
    return amino_str[:-1]



# This function reads a list of DNA chunks (3 letters per chunk) and returns a list
# with the amino acids matching each of those chunks

def decod_loop(DNA):

    amino_acid = []
    for i in DNA:
        if i == "AAA" or i == "AAG":
            amino_acid.append("Phe")

        if i == "AAT" or i == "AAC":
            amino_acid.append("Leu")

        if i == "AGA" or i == "AGG" or i == "AGT" or i == "AGC":
            amino_acid.append("Ser")

        if i == "ATA" or i == "ATG":
            amino_acid.append("Tyr")

        if i == "ACA" or i == "ACG":
            amino_acid.append("Cys")

        if i == "ACC":
            amino_acid.append("Trp")

        if i == "GAA" or i == "GAG" or i == "GAT" or i == "GAC":
            amino_acid.append("Leu")

        if i == "GGA" or i == "GGG" or i == "GGT" or i == "GGC":
            amino_acid.append("Pro")

        if i == "GTA" or i == "GTG":
            amino_acid.append("His")

        if i == "GTT" or i == "GTC":
            amino_acid.append("Gln")

        if i == "GCA" or i == "GCG" or i == "GCT" or i == "GCC":
            amino_acid.append("Arg")

        if i == "TAA" or i == "TAG" or i == "TAT":
            amino_acid.append("Ile")

        if i == "TAC":
            amino_acid.append("Met")

        if i == "TGA" or i == "TGG" or i == "TGT" or i == "TGC":
            amino_acid.append("Thr")

        if i == "TTA" or i == "TTG":
            amino_acid.append("Asn")

        if i == "TTT" or i == "TTC":
            amino_acid.append("Lys")

        if i == "TCA" or i == "TCG":
            amino_acid.append("Ser")

        if i == "TCT" or i == "TCC":
            amino_acid.append("Arg")

        if i == "CAA" or i == "CAG" or i == "CAT" or i == "CAC":
            amino_acid.append("Val")

        if i == "CGA" or i == "CGG" or i == "CGT" or i == "CGC":
            amino_acid.append("Ala")

        if i == "CTA" or i == "CTG":
            amino_acid.append("Asp")

        if i == "CTT" or i == "CTC":
            amino_acid.append("Glu")

        if i == "CCA" or i == "CCG" or i == "CCT" or i == "CCC":
            amino_acid.append("Gly")

        if i == "ATT" or i == "ATC" or i == "ACT":
            amino_acid.append("STOP")

    return amino_acid



# This function produces a complementary mRNA string from a provided DNA string
# A --> U
# T --> A
# C --> G
# G --> C
def transcribe_DNA(DNA):

    DNA = DNA.replace("A", "U")
    DNA = DNA.replace("T", "A")

    # Now we have to do an intermediate step to transform Cs into Gs and vice-versa
    # Because if we turn one into the other, we would lose one of them
    # We use an intermediate step

    DNA = DNA.replace("C", "X")
    DNA = DNA.replace("G", "C")
    DNA = DNA.replace("X", "G")

    return DNA


# This function imports a .txt document and turns it into a string of information
def get_file():
    print("")
    name = input("Enter the name of your document (if it is not on the same folder, please, indicate its location): ")
    file = open(name)
    output = ""
    for line in file: # for-each loop gives lines one at a time
        return (line.strip())



if __name__ == '__main__':
    main()