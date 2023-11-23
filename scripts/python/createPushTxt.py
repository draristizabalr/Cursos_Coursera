import datetime

# Ruta del archivo de texto
archivo = "scripts/git_bash/gitPush"

# Obtener la fecha y hora actual
fecha_actual = datetime.datetime.now()

# Abrir el archivo en modo escritura
with open(archivo, "w") as f:
    # Escribir la fecha y hora actual en el archivo
    f.write(f'''git add .
git commit -m "Update: {fecha_actual.strftime("%d/%m/%Y %H:%M:%S")}"
git push''')
