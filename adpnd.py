#Automata de pila no determinista
#L1={ a^nb^n }

Q = ['q0','q1','q2','q3']
sigma = ['a','b']
Apila = ['A','B']
z = 'A'
F = ['q3']
s = 'q0'
stack=[]
delta = {
         ('q0','a','A'): ['q1','BA'],
         ('q0',' ','A'): ['q3',''],
         ('q1','a','B'): ['q1','BB'],
         ('q1','b','B'): ['q2',''],
         ('q2',' ','A'): ['q3','A'],
         ('q2','b','B'): ['q2',''],
         }

Ejemplos_L=[' ','aabb ','aaabbb ', 'aaaabbbb ']
Ejemplos_Lc=['aba','ba','aaabb','baab']

def transicion(estado, sigma, stack):
    #print("estado=",estado,"sigma=",sigma,"estadopila=",stack[0])
    try:
        estado_siguiente = delta[(estado,sigma,stack[0])]
    except:
        return 0;
    #print("estado_siguiente=",estado_siguiente)
    stack.pop(0)
    for x in estado_siguiente[1][::-1]:
        stack.insert(0,x)
    #print("stack", stack)
    estado_siguiente = estado_siguiente[0]
    #print("estado_siguiente=",estado_siguiente)
    #print(len(stack))
    if len(stack) != 0:
        estadopila = stack[0]
        #print(estadopila)
    return estado_siguiente

for w in Ejemplos_L:
    estado = s
    estadopila = z
    stack.append(estadopila)
    for sigma in w: #para cada simblo de la cadena
        estado = transicion(estado,sigma,stack)
        #print("estado= ", estado)

    if estado in F:
        print(w,"es aceptada")
    else:
        print(w, "no es aceptada")

for w in Ejemplos_Lc:
    estado = s
    estadopila = z
    stack.append(estadopila)
    for sigma in w: #para cada simblo de la cadena
        estado = transicion(estado,sigma,stack)
    if estado in F:
        print(w,"es aceptada")
    else:
        print(w, "no es aceptada")
        


        
