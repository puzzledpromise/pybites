from heapq import heappush

hub = { 
          'a': {'b': 2, 'c': 4, 'e': 1},
          'b': {'a': 2, 'd': 3},
          'c': {'a': 4, 'd': 6},
          'd': {'c': 6, 'b': 3, 'e': 2},
          'e': {'a': 1, 'd': 2},
        }
        
def shortest_path(graph, start, end):
    """
       Input: graph: a dictionary of dictionary
              start: starting city   Ex. a
              end:   target city     Ex. b

       Output: tuple of (distance, [path of cites])
       Ex.   (distance, ['a', 'c', 'd', 'b])
    """
    h = []
    left = list(hub.keys())
    left.remove(start)
    left.remove(end)

    pick = start
    distance = 0
    steps = []
    print(f"I will start at {pick}.")

    while(True):
        next_steps = graph[pick]
        steps.append(pick)
        print(f"My next possible steps are {next_steps}.")
        if end in next_steps.keys():
            print(f"My final destination is in there! I am going to pick {end}.")
            pick = end
            steps.append(pick)
            distance += next_steps[pick]
            print(steps, distance)
            break
        else:
            if len(left) > 0:
                pick = list(set(left) & set(next_steps)).pop()
                steps.append(pick)
                print(f"I am going to pick {pick}.")
                left.remove(pick)
            else:
                break
        distance += next_steps[pick]



        
    print("I finished without reaching my target.")
    print(steps, distance)

if __name__ == "__main__":
    shortest_path(hub, "a","d")


    
