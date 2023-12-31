#xác định các bữa ăn liên tiếp có nhàm chán hay là không 
meals_1 = ['Redneck Ribs','Prawn Star','San Quentin Squid','First Full of Pizza','Honky Tonk Chicken']
meals_2 = ['Redneck Ribs','Prawn Star','Running Bear Salmon','Running Bear Salmon','Honky Tonk Chicken']
def menu_is_boring(menu):
    menu12 = tuple(menu) 
    for i in range(len(menu12)-1):
        if menu12[i] == menu12[i+1]:
            return True
    return False
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))