# dichiaro le variabili inziali 
## Prof. più che dire che dichiari le variabili (il che è evidente) specifica cosa sono e fanno tali variabili
xpos = 60 
ypos = 60
b_height = 400;
b_width= 500;
x_dir = 1
y_dir = 1
x_racchetta= 200
x_racchetta1= 200
punt=0;
punt1=0;

def setup():
    global xpos,ypos,b_width,b_height # dichiaro le variabili globali
    background(18,3,255) #coloro lo sfondo
    size (b_width, b_height) # stabilisco le dimenzioni della finestra
    

def draw():
    global xpos,ypos,b_width,b_height,x_dir,y_dir, x_racchetta, x_racchetta1,punt,punt1 # dichiaro le variabili globali
    background(18,3,255) #coloro lo sfondo
    ellipse(xpos,ypos,50,50) #disegno un cerchio
    
    
## Prof. Le ordinate sarebbe meglio esprimerle in funzone delel dimensioni della finestra    
    rect(x_racchetta,375,100,25) #disegno un rettangolo (prima racchetta)
    rect(x_racchetta1,0,100,25) #disegno un rettangolo (seconda racchetta)
    
   

## Prof. Fai il calcolo utilizzando il raggio del cerchio come variabile in maniera da poterlo cambiare e gestire facilmente    
    if (ypos+25>height-25) and (xpos+25)>x_racchetta and (xpos-25)<(x_racchetta+100) : #se la pallina rimbalza sulla prima racchetta
        y_dir = -1 #respingo la pallina facendogli cambiare direzione
    
        
    
    if (ypos-25<25) and (xpos+25)>x_racchetta1 and (xpos-25)<(x_racchetta1+100) : #se la pallina rimbalza sulla seconda racchetta
        y_dir = +1 #respingo la pallina facendogli cambiare direzione
    
        
        
        
    if (xpos+25 > width or xpos-25 < 0): #se la pallina tocca destra o sinistra
        x_dir = x_dir * (-1) #reapingo la pallina facendogli cambiare direzione
        fill(random (0, 255),random (0, 255),random (0, 255)) #cambio il colore della pallina in maniera casulale
        
    if (ypos-25 < 0): #se la pallina tocca sopra
        y_dir = y_dir * (-1) #reapingo la pallina facendogli cambiare direzione
        fill(random (0, 255),random (0, 255),random (0, 255)) #cambio il colore della pallina in maniera casulale
        punt+=1 #aumento il punteggio
        
    if (ypos+25 > height): #se la pallina tocca giù
        y_dir = y_dir * (-1) #reapingo la pallina facendogli cambiare direzione
        fill(random (0, 255),random (0, 255),random (0, 255)) #cambio il colore della pallina in maniera casulale
        punt1+=1 #aumento il punteggio
    
## Prof. Anche la velocità redenrei un parametro. Fra le altre cose con 5 non si riesce a giocare: troppo veloce in relazione alla grandezza del campo        
    #cambio le coordinate della pallina per fare in modo che essa si muova
    xpos = xpos+5*x_dir 
    ypos = ypos+5*y_dir
    

    textSize(20) #stabilisco la grandezza del punteggio della prima racchetta
    text(punt,0,400) #assegno valore e posizione al punteggio
    
    textSize(20) #stabilisco la grandezza del punteggio della seconda racchetta
    text(punt1, 0,20) #assegno valore e posizione al punteggio
    
## Prof. Cosa accade al game over? come ne esco?
    if punt>= 10: #se il punteggio del primo giocatore è maggiore o uguale a 10
        textSize(30)
## Prof. Attenzione a scrivere bene le scritte!!!!
        text("Gocatore 1 ha vinto",100,250) #giocatore 1 ha vinto
        #riporto la pallina al centro
        xpos=width/2
        ypos=height/2
        
    if punt1>= 10: #se il punteggio del secondo giocatore è maggiore o uguale a 10
        textSize(30)
        text("Gocatore 2 ha vinto",100,250) #giocatore 2 ha vinto
        #riporto la pallina al centro
        xpos=width/2 
        ypos=height/2
        
        
def keyPressed():
    global x_racchetta,x_racchetta1 #definisco le variabili globali
## Prof. Perché fai rimbalzare la racchetta: conviene no muoverla quanto tocca i bordi
    if  keyCode == LEFT: #se premo la freccia sinistra 
        if x_racchetta <= 0: #se la racchetta ha toccato il bordo sinistro
            x_racchetta+=10 #la spost di 10 verso destra
        else: #altrimenti
            x_racchetta -= 10 #la sposto di 10 verso sinistra 
            
    if  keyCode == RIGHT: #se premo la freccia destra 
        if x_racchetta >= (width - 100): #se la racchetta ha toccato il bordo destro
            x_racchetta-=10 #la sposto di 10 verso sinistra
        else: #altrimenti
            x_racchetta += 10 #la sposto di 10 verso destra
            
        
    if key== "z": #se premo il tasto z
        if x_racchetta1 <= 0: #se la racchetta ha toccato il bordo sinistro
            x_racchetta1+=10 #la spost di 10 verso destra
        else: #altrimenti
            x_racchetta1 -= 10 #la sposto di 10 verso sinistra
            
    if key== "x": #se premo il tasto x
        if x_racchetta1 >= (width - 100): #se la racchetta ha toccato il bordo destro
            x_racchetta1-=10 #la sposto di 10 verso sinistra
        else: #altrimenti
            x_racchetta1 += 10 #la sposto di 10 verso destra
            
