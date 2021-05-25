

from typing import List

def find_missing(input_list:List, range_max=20):
    """This function will return a string 
    format of missing numbers from a range 
  """
    missing = sorted([x for x in range(range_max+1) if x not in input_list])

    subtract = [missing[i]-missing[i-1] for i in range(1,len(missing))]
    # get the indices where the difference between adjacent numbers is great than 1
    indices = [i + 1 for i, x in enumerate(subtract) if x !=1]

    # split the list, each sublist has numbers increasing by 1

    result_str=[]
    for i, j in zip([0] + indices, indices + [None]):
         if len(missing[i:j])>1:
            result_str.append( str(min(missing[i:j]))+"-"+str(max(missing[i:j])))
         else:
            result_str.append( str(min(missing[i:j])))

    result_str = (','.join(result_str))
    
    # split_missing = [missing[i:j] for i, j in zip([0] + indices, indices + [None])]
    # result_str=""
    # for split in split_missing:
    #     if len(split)>1:
    #         result_str += ","+str(min(split))+"-"+str(max(split))
    #     else:
    #         result_str+=str(min(split))+","

    return result_str

input_list= [1,10,20,80,-100]
example = find_missing(input_list )
print(example)
