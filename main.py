"""
Maria plays college basketball and wants to go pro.
Each season she maintains a record of her play.
She tabulates the number of times she breaks her season record for most points and least points in a game.
Points scored in the first game establish her record for the season, and she begins counting from there.
"""
examples = [[10, 5, 20, 20, 4, 5, 2, 25, 1], [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]]

def breakingRecords(scores):
    min, max = scores[0], scores[0]
    recordsBroken = [0, 0]
    for x in scores[1:]:
        if x < min:
            min = x
            recordsBroken[1] += 1
        if x > max:
            max = x
            recordsBroken[0] += 1
    return recordsBroken
            
print(breakingRecords(examples[0]))
print(breakingRecords(examples[1]))