items = []
while True:
    item = str(input("Add a number to the list or type STOP to finish: "))
    if item.lower() == "stop":
        break
    items.append(int(item))



def insertion_sort(items):
    indexing_length = range(1, len(items))
    for i in indexing_length:
        value_to_sort = items[i]

        while items[i-1] > value_to_sort and i > 0:
            items[i], items[i-1] = items[i-1], items[i]
            i = i -1

sorted_items = insertion_sort(items)
print("The sorted list is: ", items)

