def twoSum(numbers: list[int], target: int) -> list[int]:
    
    seen = {}
    for i, value in enumerate(numbers): 
        remaining = target - numbers[i] 
        
        if remaining in seen: 
            return [i, seen[remaining]]
        else:
            seen[value] = i


print(twoSum(numbers=[3,2,4], target=6))
print(twoSum(numbers=[2,7,11,15], target=9))
print(twoSum(numbers=[3,3], target=6))