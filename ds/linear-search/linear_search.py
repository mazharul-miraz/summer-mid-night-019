

def search(arr,x):
	for i in range (len(arr)):
		if (arr[i] == x):
			return i;
	return -1;

arr =[2,5,7,9,15]
x = int(input("enter search key: "))
result = search(arr,x)

if(result != -1):
	print("element is present at index",result)
	
else:
	print("element is not in arry")
