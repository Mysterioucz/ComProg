n = int(input().strip())
file_data = {}
for _ in range(n):
    f_name = input().strip()
    data = input().split()
    file_data[f_name] = data
search = input().strip()
def search_file(w):
    similiar = {}
    for file in file_data:
        f_freq = file_data[file].count(w)/len(file_data[file])
        unique = len(set(file_data[file]))
        similiar[f_freq*(1/unique)] = file
    if max(similiar) == 0:
        return "NOT FOUND"
    return similiar[max(similiar)]
while search != "-1":
    print(search_file(search))
    search = input().strip()