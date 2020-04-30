'''write out a for loop that takes in from and to
and from there confirm if the index is less than zero
then append each word to a from to category and if
we find the last index in the list then we stop'''

def get_order(tickets):
    order = []
    from_to_dictionary = {}

    #build dictionary from and to
    for ticket in tickets:
        from_island = ticket[0]
        to_island = ticket[1]
        from_to_dictionary[from_island] = to_island
    print(from_to_dictionary)

    #find the first island
    for from_island in from_to_dictionary.keys():
        if from_island not in from_to_dictionary.values():
            start = from_island
            break
    print(start)
    #loop and reconstruct the order

    current= start

    for i in range(len(tickets)):
        order.append(current)
        current = from_to_dictionary[current]
    order.append(current)
    return order


tickets = [("Noodle", "Jungalow"), ("Korok", "Bunpun"), ("Bunpun", "Noodle"), ("Jungalow", "Astra Nova")]
print(get_order(tickets))