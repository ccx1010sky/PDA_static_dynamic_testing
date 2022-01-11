### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # change = to == to check if card.value equal 1, rather using = to assign the value to card.value.
      return True
    else  # missing a colon at the end of else keyword
      return False
   

  dif highest_card(self, card1 card2): # wrong spelling,change dif to def and also add a comma at the end of card1
  if card1.value > card2.value:  # the whole if...else statement need to be indented 
    return card # change card to card1 
  else:
    return card2
  


def cards_total(self, cards): #The whole def function need to be indented 
  total  # variable total is undefined,need to assign an integer to it .
  for card in cards:
    total += card.value
    return "You have a total of" + total   # 1,return clause indention incorrect,need to align with for keyword instead of put it inside the for loop,2 as total is integer,should convert it into string by replacing total with str(total).
  
```
