# map(function(element,index,array)){}, this)

sample_list = [1,2,3,4,5,6,7]

print(f"Sample list : {sample_list}")

result = map(lambda x : x * 3 , sample_list)

print(f'Triple of list numbers : {list(result)}')
