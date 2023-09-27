first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    

result=""

for i in range(m):
    alphanumeric=False
    for j in range(n):
        temp = matrix[j][i]
        print(temp)
        if temp.isalnum():
            result += temp
            alphanumeric=True
        elif alphanumeric and (temp ==" " or not temp.isalnum()):
            result += " "
print(result)