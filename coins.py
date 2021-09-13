# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #van euro's naar centen
paid = int(float(input('Payed amount: ')) * 100) #van euro's naar centen
change = paid - toPay #Bereken wat het verschil is tussen betaald en hoeveel er betaald moet worden.
vijf_euro = 0 
drie_euro = 0
twee_euro = 0
vijftig_cent = 0
twintig_cent = 0
tien_cent = 0
vijf_cent = 0
twee_cent = 0
een_cent = 0

if change > 0: #kijken of er wisselgeld gegeven moet worden
  coinValue = 500 #de waarde vanaf er wordt vegeleken
  
  while change > 0 and coinValue > 0: #wordt alleen uitgevoerd als het wisselgeld en waarde van de munten hoger is dan 0
    nrCoins = change // coinValue #bereken hoeveel munten er maximaal terug geven kunnen worden

    if nrCoins > 0: #wanneer coins boven 0 is wordt het uitgevoerd anders niet
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #kijken hoeveel munten per munt eenheid kan terug geven worden
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #vraag hoeveel munten er terug geven zijn
      if coinValue == 500:
        vijf_euro += nrCoinsReturned
      elif coinValue == 300:
        drie_euro += nrCoinsReturned
      elif coinValue == 200:
        twee_euro += nrCoinsReturned
      elif coinValue == 50:
        vijftig_cent += nrCoinsReturned
      elif coinValue == 20:
        twintig_cent += nrCoinsReturned
      elif coinValue == 10:
        tien_cent += nrCoinsReturned
      elif coinValue == 5:
        vijf_cent += nrCoinsReturned
      elif coinValue == 2:
        twee_cent += nrCoinsReturned
      else:
        een_cent += nrCoinsReturned
      
      change -= nrCoinsReturned * coinValue #de hoeveelheid van de opgegeven munten wordt van toaal afgehaald
    
# comment on code below: 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0
if change > 0: #als er nog extra geld gegeven moet worden dan wordt dit uitgevoerd
  print('Change not returned: ', str(change) + ' cents')
else:
  print('5 euro = ' + str(vijf_euro))
  print('3 euro = ' + str(drie_euro))
  print('2 euro = ' + str(twee_euro))
  print('50 cent = ' + str(vijftig_cent))
  print('20 cent = ' + str(twintig_cent))
  print('10 cent = ' + str(tien_cent))
  print('5 cent = ' + str(vijf_cent))
  print('2 cent = ' + str(twee_cent))
  print('1 cent = ' + str(een_cent))