T = input("Digite o seu texto:")

Caracteres_Digitados = T[0:501]

numero_texto = int(len(Caracteres_Digitados))

if(numero_texto<=140):
  print('TWEET')
  
elif(numero_texto>140):
  print('MUTE')

  