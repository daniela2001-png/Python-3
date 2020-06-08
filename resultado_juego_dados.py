'''

Antes, ya había escrito código Python que determina el siguiente paso en función del paso anterior.
Ahora es el momento de poner este código dentro de un forbucle para que podamos simular una caminata aleatoria.

Haga una lista random_walkque contenga el primer paso, que es el entero 0.
Termina el forciclo:
El ciclo debe correr 100tiempos.
En cada iteración, establezca stepigual al último elemento de la random_walklista. Puedes usar el índice -1para esto.
A continuación, deje que if- elif- elseconstruya la actualización steppor usted.
El código que se añade stepa la random_walkque ya está codificado.
Imprimir random_walk.

'''

# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = max(0, step - 1) # Aqui actualizo para que no me den valores negativos en los steps
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

'''
salida aleatoria de (steps):

[0, 4, 3, 2, 4, 3, 4, 6, 7, 8, 13, 12, 13, 14, 15, 16, 17, 16, 21, 22, 23, 24, 23, 22, 21, 20, 19, 20, 21, 22, 28, 27, 26, 25, 26, 27, 28, 27, 28, 29, 28, 33, 34, 33, 32, 31, 30, 31, 30, 29, 31, 32, 35, 36, 38, 39, 40, 41, 40, 39, 40, 41, 42, 43, 42, 43, 44, 45, 48, 49, 50, 49, 50, 49, 50, 51, 52, 56, 55, 54, 55, 56, 57, 56, 57, 56, 57, 59, 64, 63, 64, 65, 66, 67, 68, 69, 68, 69, 70, 71, 73]

'''
