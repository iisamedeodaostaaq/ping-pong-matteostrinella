# dichiaro le variabili inziali 
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
    
    
    
    rect(x_racchetta,375,100,25) #disegno un rettangolo (prima racchetta)
    rect(x_racchetta1,0,100,25) #disegno un rettangolo (seconda racchetta)
    
   

    
    if (ypos+25>height-25) and (xpos+25)>x_racchetta and (xpos-25)<(x_racchetta+100) : #se la pallina rimbalza sulla prima racchetta
        y_dir = -1 #respingo la pallina facendogli cambiare direzione
        punt+=1 #aumento il punteggio
        
    
    if (ypos-25<25) and (xpos+25)>x_racchetta1 and (xpos-25)<(x_racchetta1+100) : #se la pallina rimbalza sulla seconda racchetta
        y_dir = +1 #respingo la pallina facendogli cambiare direzione
        punt1+=1 #aumento il punteggio
        
        
        
    if (xpos+25 > width or xpos-25 < 0): #se la pallina tocca su o giù
        x_dir = x_dir * (-1) #reapingo la pallina facendogli cambiare direzione
        fill(random (0, 255),random (0, 255),random (0, 255)) #cambio il colore della pallina in maniera casulale
        if punt >= 10: #se il punteggio è superiore o uguale a 10
            punt-=1 #diminuisco il punteggio
        
        
    if (ypos+25 > height or ypos-25 < 0): #se la pallina tocca destra o sinistra
        y_dir = y_dir * (-1) #reapingo la pallina facendogli cambiare direzione
        fill(random (0, 255),random (0, 255),random (0, 255)) #cambio il colore della pallina in maniera casulale
        if punt1 >= 10: #se il punteggio è superiore o uguale a 10
            punt1-=1 #diminuisco il punteggio
        
    #cambio le coordinate della pallina per fare in modo che essa si muova
    xpos = xpos+5*x_dir 
    ypos = ypos+5*y_dir
    

    textSize(20) #stabilisco la grandezza del punteggio della prima racchetta
    text(punt,0,400) #assegno valore e posizione al punteggio
    
    textSize(20) #stabilisco la grandezza del punteggio della seconda racchetta
    text(punt1, 0,20) #assegno valore e posizione al punteggio
    

    
def keyPressed():
    global x_racchetta,x_racchetta1 #definisco le variabili globali
    if  keyCode == LEFT: #se premo la freccia sinistra 
        if x_racchetta <= 0: #se la racchetta ha toccato il bordo sinistro
            x_racchetta+=10 #la spost di 10 verso destra
        else: #altrimenti
            x_racchetta -= 10 #la sposto di 10 verso sinistra 
            
    if  keyCode == RIGHT: #se premo la freccia destra 
        if x_racchetta >= (width - 100): #se la racchetta ha toccato il bordo destro
            x_racchetta-=10 #la sposto di 10 verso sinistra
        else: #altrimenti
            x_racchetta += 10 #la spost di 10 verso destra
            
        
    if key== "z": #se premo il tasto z
        if x_racchetta1 <= 0: #se la racchetta ha toccato il bordo sinistro
            x_racchetta1+=10 #la spost di 10 verso destra
        else: #altrimenti
            x_racchetta1 -= 10 #la sposto di 10 verso sinistra
            
    if key== "x": #se premo il tasto x
        if x_racchetta1 >= (width - 100): #se la racchetta ha toccato il bordo destro
            x_racchetta1-=10 #la sposto di 10 verso sinistra
        else: #altrimenti
            x_racchetta1 += 10 #la spost di 10 verso destra
            
