length_input = input("Enter the length of the filament in meters: ")
weight_input = input("Enter the weight of the filament in grams: ")

length = 0.0 if not length_input else float(length_input)
weight = 0.0 if not weight_input else float(weight_input)

lengthDefault = 0.01
weightDefault = 0.01

weightTotal = 0
LengthTotal = 0

PLA = 2.98
ABS = 2.50
PETG = 3.05
ASA = 2.57
Nylon = 2.59
TPU = 2.88
PC = 2.88
TPE = 2.88

material = input("Enter the material of the filament: ").upper()

if length >= lengthDefault:
    if material == "PLA":
        weightTotal = length * PLA
    elif material == "ABS":
        weightTotal = length * ABS
    elif material == "PETG":
        weightTotal = length * PETG
    elif material == "ASA":
        weightTotal = length * ASA
    elif material == "Nylon":
        weightTotal = length * Nylon
    elif material == "TPU":
        weightTotal = length * TPU
    elif material == "PC":
        weightTotal = length * PC
    elif material == "TPE":
        weightTotal = length * TPE
    else:
        material_input = input("Enter the weight  of the filament per meter: ")
        material_weight = 0.0 if not material_input else float(material_input)
        weightTotal = length * material_weight
weightOutput = "The weight of the filament is: %.2f" % weightTotal
print(weightOutput)

if weight >= weightDefault:
    if material == "PLA":
        LengthTotal = weight / PLA
    elif material == "ABS":
        LengthTotal = weight / ABS
    elif material == "PETG":
        LengthTotal = weight / PETG
    elif material == "ASA":
        LengthTotal = weight / ASA
    elif material == "Nylon":
        LengthTotal = weight / Nylon
    elif material == "TPU":
        LengthTotal = weight / TPU
    elif material == "PC":
        LengthTotal = weight / PC
    elif material == "TPE":
        LengthTotal = weight / TPE
    else:
        material_input = input("Enter the Length of the filament per meter: ")
        material_weight = 0.0 if not material_input else float(material_input)
        LengthTotal = weight / material_weight
lengthOutput = "The length of the filament is: %.2f" % LengthTotal
print(lengthOutput)