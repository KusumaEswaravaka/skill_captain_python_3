#open file in read mode
with open('sample.txt', 'r') as file:
    file_iter = iter(file) #create iterator for file obj
     

    while True:
        try:
            line = next(file_iter) #gets next line
            print(line.strip())

        except StopIteration:
            break
