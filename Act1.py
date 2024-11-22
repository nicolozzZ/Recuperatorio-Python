listNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

def listAndSlices(list):
  firstTen = []
  lastTen = []
  positionPair = []
  positionImpair = []
  for i in range(len(list)):
    ind = i + 1
    if ind<=10:
      firstTen.append(list[i])
    if i >= len(list)-10:
      lastTen.append(list[i])
    if i%2 == 0:
      positionPair.append(list[i])
    if i%2 == 1:
      positionImpair.append(list[i])
  return (firstTen, lastTen, positionPair, positionImpair)

print(listAndSlices(listNum))
