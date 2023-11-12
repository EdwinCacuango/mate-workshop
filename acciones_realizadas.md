# Observaciones generales
1. system("cls") = > sirve para limpiar la pantalla dentro del programa en ejecución
Esta funcion no limpia pantalla en sistemas no windows. Se refactora para que permita limpiar tambien en linux y mac
2. En cada operación se utiliza mostrar cada conjunto.

# Acciones de refactorización
1. Se separa las operaciones en archivos independientes para mayor legibilidad
2. Para no repetir las operaciones, se crea una funcion en utilidades que muestre los conjuntos
3. Se agruparon las operaciones en una subcarpeta