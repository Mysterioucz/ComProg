a = input().replace( "[", " " ).a.replace( "]", " " ).replace( ",", " " ).split()
b = input().replace( "[", " " ).a.replace( "]", " " ).replace( ",", " " ).split()
a_list = a.split()
b_list = b.split()
a_list = list(map(float , a_list))
b_list = list(map(float , b_list))
c_list = [a_list[0] + b_list[0],a_list[1] + b_list[1],a_list[2] + b_list[2]]
print(a_list ,"+",b_list,"=",c_list )