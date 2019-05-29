# #linear search 
# #WAP search on selement in list

# import pdb
# def linear_search(List,key):
# 	#loop init
# 	for i in range (len(List)):
# 		# pdb.set_trace()
# 		if (List[i] == key):
# 			return i;
# 			break;
# 	return -1

# #given list

# List=[2,3,4,6,9,10,11,14,18,19,22,24,50,56,60,70,80,85,90,100]

# r = linear_search(List,23)

# key =input("Enter the search key:  ")


# if (r!=-1):
# 	print(key,'Search key findout',r)
# else:
# 	print(key,'key is not found')


def search(arr,x):
	for i in range (len(arr)):
		if (arr[i] == x):
			return i;
	return -1;

arr =[2,5,7,9,15]
x = int(input("enter search key: "))
result = search(arr,x)

if(result == -1):
	print("element is not in arry")
else:
	print("element is present at index",result)
