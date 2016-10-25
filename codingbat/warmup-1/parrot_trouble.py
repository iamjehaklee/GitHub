def parrot_trouble(talking, hour):
  if (hour > 20 or hour < 7) and talking == True:
    return True
  return False