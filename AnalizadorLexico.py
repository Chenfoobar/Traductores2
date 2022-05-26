elementos=[]
entrada="cadena a analizar"
def analizadorLexico(cadena):
    decim=False
    if cadena[-1]!='$':cadena=cadena+'$'
    indice=0
    estado=0
    while(indice<=(len(cadena)-1)  and estado==0):  
            lexema=''
            token='error'
            num=0
            while(indice<=(len(cadena)-1) and estado!=18):
                if estado==0:
                    if(cadena[indice].isspace()):
                        estado=0
                    elif cadena[indice].isalpha() or cadena[indice]=='_':
                        estado=1
                        lexema+=cadena[indice]
                        token='id'
                        num=1
                    elif cadena[indice]=='$':
                        estado=18
                        lexema+=cadena[indice]
                        token='pesos'
                        num=18
                    elif cadena[indice]=='=':
                        lexema+=cadena[indice]
                        token='asignación'
                        estado=8
                        num=8
                    elif cadena[indice]==';':
                        lexema+=cadena[indice]
                        token='punto y coma'
                        estado=18 
                        num=2
                    elif cadena[indice]==',':
                        lexema+=cadena[indice]
                        token='coma'
                        estado=18
                        num=3
                    elif cadena[indice]=='(':
                        lexema+=cadena[indice]
                        token='parentesis abierto'
                        estado=18
                        num=4
                    elif cadena[indice]==')':
                        lexema+=cadena[indice]
                        token='parentesis cerrado'
                        estado=18
                        num=5
                    elif cadena[indice]=='{':
                        lexema+=cadena[indice]
                        token='corchete abierto'
                        estado=18
                        num=6
                    elif cadena[indice]=='}':
                        lexema+=cadena[indice]
                        token='corchete cerrado'
                        estado=18  
                        num=7
                    elif cadena[indice].isdigit():
                        estado=13
                        lexema+=cadena[indice]
                        token='constante'
                        num=13
                    elif cadena[indice]=='+' or cadena[indice]=='-':
                        lexema+=cadena[indice]
                        token='opSuma'
                        estado=18 
                        num=14
                    elif cadena[indice]=='|' or cadena[indice]=='&':
                        lexema+=cadena[indice]
                        estado=15
                    elif cadena[indice]=='*' or cadena[indice]=='/':
                        lexema+=cadena[indice]
                        token='opMultiplicacion'
                        estado=18   
                        num=16
                    elif cadena[indice]=='<' or cadena[indice]=='>':
                        lexema+=cadena[indice]
                        token='opRelacional'
                        estado=17   
                        num=17
                    elif cadena[indice]=='!':
                        lexema+=cadena[indice]
                        estado=17   
                    else:
                        estado=18
                        token='error'
                        lexema=cadena[indice]
                        num='x'
                    indice+=1
                elif estado==1:
                    if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice]=='_':
                        estado=1
                        lexema+=cadena[indice]
                        token='id'
                        indice+=1
                        num=1
                    else:
                        estado=18 
                elif estado==8:
                    if cadena[indice]=='=':
                        lexema+=cadena[indice]
                        token='opRelacional'
                        estado=18
                        indice+=1
                        num=17
                        estado=18
                    if cadena[indice]=='>':
                        lexema+=cadena[indice]
                        token='opRelacional'
                        estado=18
                        indice+=1
                        num=17
                        estado=18
                    else:
                        estado=18
                elif estado==13:
                    if cadena[indice].isdigit() and decim==False:
                        estado=13
                        lexema+=cadena[indice]
                        token='constante'
                        indice+=1
                        num=13
                    elif cadena[indice].isdigit() and decim==True:
                        estado=13
                        lexema+=cadena[indice]
                        token='constante decimal'
                        indice+=1
                        num=13
                        decim=True
                    elif cadena[indice]=='.':
                        estado=13
                        lexema+=cadena[indice]
                        token='constante decimal'
                        indice+=1
                        num=13
                        decim=True
                    else:
                        estado=18
                        decim=False
                elif estado==15:
                    if cadena[indice-1]=='|'and cadena[indice]=='|':
                        lexema+=cadena[indice]
                        token='opLogico'
                        estado=18
                        indice+=1   
                        num=15
                    elif cadena[indice-1]=='&'and cadena[indice]=='&':
                        lexema+=cadena[indice]
                        token='opLogico'
                        estado=18
                        indice+=1     
                        num=15
                    else:
                        estado=18
                elif estado==17:
                    if(cadena[indice-1]=='<' or cadena[indice-1]=='>') and cadena[indice]=='=':
                        lexema+=cadena[indice]
                        token='opRelacional'
                        estado=17   
                        num=17
                        indice+=1
                    elif cadena[indice-1]=='!' and cadena[indice]=='=':
                        lexema+=cadena[indice]
                        token='opRelacional'
                        estado=17   
                        num=17
                        indice+=1
                    else:
                        estado=18
            estado=0
            elementos.append({'token':token,'lexema':lexema, 'num':num})
    for elemento in elementos:
        if elemento['lexema']=="if":
            elemento['token']="condicional SI"
            elemento['num']=9
        if elemento['lexema']=="while":
            elemento['token']="bucle while"
            elemento['num']=10
        if elemento['lexema']=="return":
            elemento['token']="valor retornado"
            elemento['num']=11
        if elemento['lexema']=="else":
            elemento['token']="else"
            elemento['num']=12
        if elemento['lexema']=="int":
            elemento['token']="Tipo int"
            elemento['num']=0
        if elemento['lexema']=="float":
            elemento['token']="Tipo float"
            elemento['num']=0
        if elemento['lexema']=="char":
            elemento['token']="Tipo char"
            elemento['num']=0
        if elemento['lexema']=="void":
            elemento['token']="Tipo void"
            elemento['num']=0
    return elementos
elem=analizadorLexico(entrada)
for elemento in elem:
    print(elemento)