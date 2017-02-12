# ComposedTransposed
# Authors: Eyosyas Dagnachew, Rozda Askari, Dima Shmagin
# 

# 1. open the file to read
# 2. Read the file one character at a time
        # if its a charater not a space or endline
                # read the next character
                    # if that charcater is not a space or endline
                        # concatenate the two character and put them in an array
                    # else put first chactaer in array based on cases
        # else save
        #suh dude

def main():

    musical_scale = {0: 'A', }



    input_file = open("input.txt", "r")
    #print(input_file.read())
    music = []
    with input_file as file:

        for line in file:
            for word in line.split():
                print(word)
        #    line = line.strip()
        #    music.append(line)
    print(music)


main()
