#include "lexico.h"

  Lexico::Lexico(string fuente){
    ind= 0;                  
    this->fuente= fuente;
  }      

  Lexico::Lexico(){
    ind= 0;                  
  }      
  
  string Lexico::tipoAcad(int tipo){
         string cad= "";
         
         switch (tipo){
           case TipoSimbolo::IDENTIFICADOR:
                cad= "Identificador";
                break;
                
           case TipoSimbolo::OPADIC:
                cad= "Op. Adicion";
                break;

           case TipoSimbolo::OPMULT:
                cad= "Op. Multiplicacion";
                break;            
           case TipoSimbolo::IGUAL:
                cad= "Igual";
                break;
           case TipoSimbolo::OPNOT:
                cad= "Operador Not";
                break; 
           case TipoSimbolo::PESOS:
                cad= "Fin de la Entrada";
                break;            
           case TipoSimbolo::RELACIONAL:
                cad= "Relacional";
                break;
           case TipoSimbolo::PTCOMA:
                cad= "Punto y coma";
                break;
           case TipoSimbolo::COMA:
                cad= "Coma";
                break;
           case TipoSimbolo::PAREABI:
                cad= "Parentesis abierto";
                break;
           case TipoSimbolo::PARECER:
                cad= "Parentesis cerrado";
                break;
           case TipoSimbolo::CORCABI:
                cad= "Corchete abierto";
                break;
           case TipoSimbolo::CORCCER:
                cad= "Corchete cerrado";
                break;     
           case TipoSimbolo::ENTERO:
                cad= "Entero";
                break;
           case TipoSimbolo::LETRA:
                cad= "Letra";
                break;
                
         }
         
         return cad;
  }
  
  void Lexico::entrada(string fuente){
       ind= 0;                  
      this->fuente= fuente;
  }

int Lexico::sigSimbolo(){
    
    estado=0;
    continua= true;
    simbolo= "";
    while (continua){
      c= sigCaracter();
      switch (estado){
        case 0:
             while (esEspacio(c)){
                  c=sigCaracter();
             }
             /* if((esLetra(c)||esDigito(c))&&(esEspacio(sigCaracter())==false)){
                  aceptacion(0);
             }  */
             if ( c == '+' || c=='-') aceptacion(5);
             else if ( c == '*' || c=='/') aceptacion(6);
             else if ( c == '<' || c=='>') aceptacion(7);
             else if ( c == '!') aceptacion(10);
             else if ( c == ';') aceptacion(12);
             else if ( c == ',') aceptacion(13);
             else if ( c == '(') aceptacion(14);
             else if ( c == ')') aceptacion(15);
             else if ( c == '{') aceptacion(16);
             else if ( c == '}') aceptacion(17);
             else if ( c == '=') aceptacion(18);
             else if ( c == '$' ) aceptacion(23);
             else if (esDigito(c)) aceptacion(1);
             else if (esLetra(c)) aceptacion(3);
             else 
              aceptacion(-1);
             break;                            
      }      
   }        
      switch (estado){
         case 0:
              tipo= TipoSimbolo::IDENTIFICADOR;
              break;
         case 1:
              tipo= TipoSimbolo::ENTERO;
              break;
         case 2:
              break;
         case 3:
              tipo= TipoSimbolo::LETRA;
              break;  
         case 4:
              break; 
         case 5:
              tipo= TipoSimbolo::OPADIC;
              break;
         case 6:
              tipo= TipoSimbolo::OPMULT;
              break;
         case 7:
              tipo= TipoSimbolo::RELACIONAL;
              break;
         case 10:
              tipo= TipoSimbolo::OPNOT;
              break;
         case 12:
              tipo= TipoSimbolo::PTCOMA;
              break;
         case 13:
              tipo= TipoSimbolo::COMA;
              break;
         case 14:
              tipo= TipoSimbolo::PAREABI;
              break;
         case 15:
              tipo= TipoSimbolo::PARECER;
              break;
         case 16:
              tipo= TipoSimbolo::CORCABI;
              break;
         case 17:
              tipo= TipoSimbolo::CORCCER;
              break;
         case 18:
              tipo= TipoSimbolo::IGUAL;
              break;         
         case 23:
              tipo= TipoSimbolo::PESOS;
              break;    
         default:                 
              tipo= TipoSimbolo::ERROR;
      }
    		
	return tipo;
}

 char Lexico::sigCaracter(){
      if (terminado()) return '$';
      
      return fuente[ind++];
 }

  void Lexico::sigEstado(int estado){
       this->estado= estado;
       simbolo+= c;
  }
  
  void Lexico::aceptacion(int estado){
       sigEstado(estado);
       continua= false;
  }

  bool Lexico::terminado(){//fin de cadena
         return ind >= fuente.length();
  }

   bool Lexico::esLetra(char c){
        return isalpha(c) || c=='_';
   }
   
   
   bool Lexico::esDigito(char c){
        return isdigit(c);
   }
   
   bool Lexico::esEspacio(char c){
        return c== ' ' || c== '\t';        
   }

            
   void Lexico::retroceso(){
      if ( c != '$') ind--;
        continua= false;
    }