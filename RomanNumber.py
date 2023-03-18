def RomanToDigit(InputString):
    """Convert a string roman number to integer"""
    # dictionnaire de conversion des chiffres romains
    digits = {'M': 1000,
              'D': 500,
              'C': 100,
              'L': 50,
              'X': 10,
              'V': 5,
              'I': 1}
    # initialize la valeur convetie à 0
    Value = 0
    # Memorise le dernier digit lu
    LastDigit = 0
    # Comte le nombre de igits identiques successifs
    DigitCount = 0
    # Memorise si on en déjà dans une phase de décrément
    # evite les sequence du type 'IIX'
    DecrementPhase = False

    # On s'assure que la chaine est bien est majuscules
    InputString = InputString.upper()

    # Renverse la chaine a convertir
    InputString = InputString[::-1]

    # si la chaine n'est pas vide
    if len(InputString) > 0 :
        # Traitement spécifique du premier caractère
        # Converti le premier digit
        digit = InputString[0]
        digitValue = digits[digit]
        Value = digitValue
        DigitCount = 1
        # Memorise le dernier digit lu
        LastDigit = digitValue
        # parcours le reste de la chaine d'input
        for digit in InputString[1:]:
            # Convertir le digit lu
            digitValue = digits[digit]
            # Compte le nombre de digits identiques consécutifs
            if digitValue < LastDigit :
                if DecrementPhase :
                    # Leve une exception car plus d'un digit en decrement
                    print("ERROR 2 consecutive digit lesser")
                    DigitCount += 1
                else :
                    DigitCount = 0
                    Value -= digitValue
                    DecrementPhase = True
            elif digitValue != 1000 and digitValue == LastDigit:
                # Si identique au dernier digit lu on incrémente
                DigitCount+=1
                Value += digitValue
                DecrementPhase = False
                LastDigit = digitValue
            else:
                # Sinon on reprend le compte à 1
                DigitCount = 1
                Value += digitValue
                DecrementPhase = False
                LastDigit = digitValue
        # Si le nombre de digits identiques consécutifs est égal à 4
            # On leve une exception
            if DigitCount >= 4:
                print("ERROR 4 consecutive digits identical")
                print(DigitCount)
            # mémorise le dernier chiffre
    return Value

def DigitToRoman(DigitalValue) :
    """Convert an integer to a string roman number"""
    # Tableau de conversion groupe de décimales vers chiffres romains
    Int2Roman = {1000: 'M',
                 900: 'CM',
                 500: 'D',
                 400: 'CD',
                 100: 'C',
                 90: 'XC',
                 50: 'L',
                 40: 'XL',
                 10: 'X',
                 9: 'IX',
                 5: 'V',
                 4: 'IV',
                 1: 'I'}

    # GFonction generique pour calculer le nombre de digit
    def GroupeToRoman(Valeur, Groupe, Chaine):
        # Modulo Groupe et Calcul du reste
        Quotient = Valeur // Groupe
        Reste = Valeur % Groupe
        RomanValue = Quotient * Chaine
        return Reste, RomanValue

    # Initialize le résultat avec une chaine vide.
    RomanValue = ''

    for i in Int2Roman :
        DigitalValue, Chaine = GroupeToRoman(DigitalValue, i, Int2Roman[i])
        RomanValue += Chaine

    return RomanValue

#######################################################
#                                                     #
#  Debut du corps principal du programme              #
#                                                     #
#######################################################
while True:
    # Saisie du nombre decimal à convertir
    InputString = input("Entrez un nombre decimal : ")
    Value = DigitToRoman(int(InputString))
    print(f"---> {Value}")

    # Saisie du nombre romain à convertir
    InputString = input("Entrez un nombre en chiffres romains : ")
    Value = RomanToDigit(InputString)
    print(f"---> {Value}")

#######################################################
#                                                     #
#  Boucle d'auto-test des deux fonctions              #
#  Verifie que chacune est bien re-entrante           #
#                                                     #
#######################################################
# for loop_int in range(1, 5000):
    # Roman = DigitToRoman(loop_int)
    # Digit = RomanToDigit(Roman)
    # if Digit != loop_int :
        # print("##### ERROR #####")
        # break;
# print("LOOP ENDED")
