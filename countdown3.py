N = int(input("What should our countdown start at: "))

for j in range(N,-1,-1):
	i = N-j
	print(i, "minutes are left!")
	print(j, "minutes have passed!")
	print()
