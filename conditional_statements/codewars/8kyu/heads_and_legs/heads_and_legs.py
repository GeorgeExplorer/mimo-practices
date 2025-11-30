def animals(heads: int, legs: int) -> tuple[int, int]:
  if legs % 2 or not 2*heads <= legs <= 4*heads:
    print("No solutions")
    return ("No solutions")
  else:
    chicken = (legs - (4 * heads)) // -2
    cows = heads - chicken
    result = (chicken, cows)
    print(chicken, cows)
    return (chicken, cows)
