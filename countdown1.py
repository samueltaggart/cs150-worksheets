N = int(input("What should our countdown start at: "))

j = 0
i = N
for N in range(0,N+1):
	print(i, "minutes are left!")
	print(j, "minutes have passed!")
	j = j+1
	i = N-j
	print()
