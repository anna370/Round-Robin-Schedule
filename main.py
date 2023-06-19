def generate_round_robin_schedule(name_list):
  """
  Generates a round robin schedule for a list of names.
  
  Parameters:
    name_list: a list of strings, each of which is a name
  Return value:
    A list of tuples, where each tuple is a pair of names
  """
  list_copy = list(name_list)

  if len(list_copy) % 2 == 1:
    list_copy.append("bye")

  schedule = []

  for r in range(len(list_copy) - 1):
    pairs = []
    for i in range(len(list_copy) // 2):
      pairs.append((list_copy[i], list_copy[-i - 1]))
    schedule += pairs
    list_copy = [list_copy[0]] + list_copy[-1:] + list_copy[1:-1]

  return schedule

print(generate_round_robin_schedule(['A', 'B', 'C'])) # [('A', 'bye'), ('B', 'C'), ('A', 'C'), ('bye', 'B'), ('A', 'B'), ('C', 'bye')]
