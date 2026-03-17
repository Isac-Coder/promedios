# def busqueda_binaria(lista, target):
    
#     inicio = 0
#     final = len(lista) - 1

#     while inicio <= final:
#         medio = (inicio + final) // 2
#         valor_medio = lista[medio]

#         if valor_medio == target:
#             return medio  # target encontrado
#         elif valor_medio > target:
#             final = medio - 1  # Buscar en la mitad inicio
#         else:
#             inicio = medio + 1  # Buscar en la mitad final
            
#     return -1 # No encontrado

# # Ejemplo de uso
# lista = [1, 3, 5, 7, 9, 11, 13, 15]
# print(busqueda_binaria(lista, 0))  # Salida: 3



nums = [1,2,3,4,5,6,7,8,9,10]
target = 9

def busqueda_binaria(nums, target):
    
    inicio = 0
    final = len(nums) - 1
    
    while inicio <= final:
        
        mitad = (inicio + final) // 2
        valor_mitad = nums[mitad]
        
        if target == valor_mitad:
            return mitad
        elif target > valor_mitad:
            inicio = mitad + 1
        else:
            final = mitad - 1
            
    return -1

print(busqueda_binaria(nums, target))
            
    