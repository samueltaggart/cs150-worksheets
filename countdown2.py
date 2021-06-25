N = int(input("What should our countdown start at: "))

j = 0
i = N
for j in range(0,N+1):
	print(i, "minutes are left!")
	print(j, "minutes have passed!")
	i = N-j
	print()
