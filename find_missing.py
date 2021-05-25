

from typing import List

def find_missing(input_list:List, range_max=20):
    """This function will return the missing numbers(in string format) 
    by comparing the input_list with the range list 
  """
    missing = sorted([x for x in range(range_max+1) if x not in input_list])

    subtract = [missing[i]-missing[i-1] for i in range(1,len(missing))]
    # get the indices where the difference between adjacent numbers is great than 1
    indices = [i + 1 for i, x in enumerate(subtract) if x !=1]

    # split the list, each sublist missing[i:j]  has numbers increasing by 1

    result_str=[]
    for i, j in zip([0] + indices, indices + [None]):
         if len(missing[i:j])>1:
            result_str.append( str(min(missing[i:j]))+"-"+str(max(missing[i:j])))
         else:
            result_str.append( str(min(missing[i:j])))

    result_str = (','.join(result_str))

    return result_str

input_list= [1,10,20,80,-100]
example = find_missing(input_list )
print(example)
