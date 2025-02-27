for x in reversed(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']):
    result = int('a23' + x + 'ac0', 22) + int('gb' + x + '21670', 22)
    if result % 21 == 0:
        print(result // 22)
        break 