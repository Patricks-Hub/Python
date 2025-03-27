from django.shortcuts import render

def filament_calculator(request):
    # 1. Initialize variables
    length_input = ""
    weight_input = ""
    length = 0.0
    weight = 0.0
    weightTotal = 0
    LengthTotal = 0
    material = ""
    weightOutput = ""
    lengthOutput = ""

    # 2. Define Material Constants
    PLA = 2.98
    ABS = 2.50
    PETG = 3.05
    ASA = 2.57
    Nylon = 2.59
    TPU = 2.88
    PC = 2.88
    TPE = 2.88

    # 3. Handle POST Request (Form Submission)
    if request.method == 'POST':
        length_input = request.POST.get('length', '')
        weight_input = request.POST.get('weight', '')
        material = request.POST.get('material', '').upper()

        length = 0.0 if not length_input else float(length_input)
        weight = 0.0 if not weight_input else float(weight_input)

        lengthDefault = 0.01
        weightDefault = 0.01

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
                material_input = request.POST.get('material_weight', '')
                material_weight = 0.0 if not material_input else float(material_input)
                weightTotal = length * material_weight
            weightOutput = "The weight of the filament is: %.2f" % weightTotal

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
                material_input = request.POST.get('material_weight', '')
                material_weight = 0.0 if not material_input else float(material_input)
                LengthTotal = weight / material_weight
            lengthOutput = "The length of the filament is: %.2f" % LengthTotal

    # 4. Render the Template with Data
    return render(request, 'filament_calc/calculator.html', {
        'weightOutput': weightOutput,
        'lengthOutput': lengthOutput,
        'length_input': length_input,
        'weight_input': weight_input,
        'material': material,
    })