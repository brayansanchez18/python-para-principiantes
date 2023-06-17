miDiccionario = {
  "marca":"volkswagen",
  "modelo":"jetta",
  "year":2023,
  "color":"gris"
}

print(miDiccionario)

# actualizar elemento del array
miDiccionario.update({"color":"negro"})
print(miDiccionario)

# actualizar sin el update
miDiccionario['color'] = 'Azul'
print(miDiccionario)

# agregar elemento al array
miDiccionario['serie'] = 'SE'
print(miDiccionario)