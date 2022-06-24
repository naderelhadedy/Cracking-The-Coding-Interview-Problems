def groupAnagrams(strs):
    if len(strs) == 1:
        return [strs]
    vals = []
    final_arr = []
    for i in strs:
        vals.append(get_val(i))
        
    visited = dict()
    for i in range(len(vals)):
        if vals[i] not in visited:
            visited.setdefault(vals[i], [strs[i]])
        else:
            visited[vals[i]].append(strs[i])
            
    
    for val in visited.values():
        final_arr.append(val)
    
    return final_arr

def get_val(word):
    return ''.join(sorted(word))

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)