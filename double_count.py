d = {'Straight Flush': 40, 'Four of a Kind': 624, 'Full House': 3744, 'Flush': 5108, 'Straight': 10200, 'Three of a Kind': 54912, 'Two Pair': 123552, 'One Pair': 1098240, 'High Card': 1302540}
nd = {}

nd['Straight Flush'] = d['Straight Flush']
nd['Four of a Kind'] = d['Four of a Kind']
nd['Full House'] = d['Full House']
nd['Flush'] = d['Straight Flush'] + d['Flush']
nd['Straight'] = d['Straight'] + d['Straight Flush']
nd['Three of a Kind'] = d['Four of a Kind'] + d['Full House'] + d['Three of a Kind']
nd['Two Pair'] = d['Four of a Kind'] + d['Full House'] + d['Two Pair']
nd['One Pair'] = d['One Pair'] + d['Two Pair'] + d['Three of a Kind'] + d['Four of a Kind'] + d['Full House']
nd['High Card'] = d['Straight Flush'] + d['Four of a Kind'] + d['Full House'] + d['Flush'] + d['Straight'] + d['Three of a Kind'] + d['Two Pair'] + d['One Pair'] + d['High Card']

print(nd)
