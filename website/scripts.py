import random

def shuffler(entrada):

    vetor_dados = entrada.split()
    result = ''

    for item in vetor_dados:
        charlst = list(item)
        random.shuffle(charlst)
        new_item = ''.join(charlst)

        result =result + new_item + "\n"

    return result

def enthalpy(entrada):

    vetor_dados = entrada.split()
    result = ''

    lista_entalpia = []

    for item in vetor_dados:
        size = len(item)
        entalpia = 0

        for pos in range(size - 1):
            if item.upper()[pos:pos + 2] == 'AA':
                entalpia = -7.6
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'AT':
                entalpia = -7.2
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'TA':
                entalpia = -7.2
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'AG':
                entalpia = -8.2
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'GA':
                entalpia = -8.2
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'TT':
                entalpia = -7.6
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'AC':
                entalpia = -8.5
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'CA':
                entalpia = -8.5
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'TG':
                entalpia = -8.4
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'GT':
                entalpia = -8.4
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'TC':
                entalpia = -7.8
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'CT':
                entalpia = -7.8
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'CC':
                entalpia = -8
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'CG':
                entalpia = -10.6
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'GC':
                entalpia = -10.6
                lista_entalpia.append(entalpia)

            if item.upper()[pos:pos + 2] == 'GG':
                entalpia = -8
                lista_entalpia.append(entalpia)

    for item in lista_entalpia:
        result = result + str(item) + "\n"

    return result

def entropy(entrada):
    vetor_dados = entrada.split()
    result = ''

    lista_entropia = []

    for item in vetor_dados:
        size = len(item)
        entropia = 0

        for pos in range(size - 1):
            if item.upper()[pos:pos + 2] == 'AA':
                entropia = -21.3
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'AT':
                entropia = -20.4
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'TA':
                entropia = -21.3
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'AG':
                entropia = -21
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'GA':
                entropia = -21
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'TT':
                entropia = -21.3
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'AC':
                entropia = -22.7
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'CA':
                entropia = -22.7
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'TG':
                entropia = -22.4
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'GT':
                entropia = -22.4
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'TC':
                entropia = -22.4
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'CT':
                entropia = -22.2
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'CC':
                entropia = -19.9
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'CG':
                entropia = -27.2
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'GC':
                entropia = -24.4
                lista_entropia.append(entropia)

            if item.upper()[pos:pos + 2] == 'GG':
                entropia = -19.9
                lista_entropia.append(entropia)

    for item in lista_entropia:
        result = result + str(item) + "\n"

    return result

def stability(entrada):

    vetor_dados = entrada.split()
    result = ''

    lista_stability = []

    for item in vetor_dados:
        size = len(item)
        stability = 0

        for pos in range(size - 1):
            if item.upper()[pos:pos + 2] == 'AA':
                stability = -1
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'AT':
                stability = -0.88
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'TA':
                stability = -0.58
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'AG':
                stability = -1.3
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'GA':
                stability = -1.3
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'TT':
                stability = -1
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'AC':
                stability = -1.45
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'CA':
                stability = -1.45
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'TG':
                stability = -1.44
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'GT':
                stability = -1.44
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'TC':
                stability = -1.28
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'CT':
                stability = -1.28
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'CC':
                stability = -1.84
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'CG':
                stability = -2.24
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'GC':
                stability = -2.27
                lista_stability.append(stability)

            if item.upper()[pos:pos + 2] == 'GG':
                stability = -1.84
                lista_stability.append(stability)

    for item in lista_stability:
        result = result + str(item) + "\n"

    return result

def stacking(entrada):
    vetor_dados = entrada.split()
    result = ''

    lista_stacking = []

    for item in vetor_dados:
        size = len(item)
        stacking = 0

        for pos in range(size - 1):
            if item.upper()[pos:pos + 2] == 'AA':
                stacking = -5.37
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'AT':
                stacking = -6.57
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'TA':
                stacking = -3.82
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'AG':
                stacking = -6.78
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'GA':
                stacking = -9.81
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'TT':
                stacking = -5.37
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'AC':
                stacking = -10.51
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'CA':
                stacking = -6.57
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'TG':
                stacking = -6.57
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'GT':
                stacking = -10.51
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'TC':
                stacking = -9.81
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'CT':
                stacking = -6.78
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'CC':
                stacking = -8.26
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'CG':
                stacking = -9.69
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'GC':
                stacking = -14.59
                lista_stacking.append(stacking)

            if item.upper()[pos:pos + 2] == 'GG':
                stacking = -8.26
                lista_stacking.append(stacking)

    for item in lista_stacking:
        result = result + str(item) + "\n"

    return result
