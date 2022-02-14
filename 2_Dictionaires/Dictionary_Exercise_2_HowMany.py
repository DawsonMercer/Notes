
def how_many(animals):
    total_len = 0
    for item in animals.values():
        total_len += len(item)
    print(total_len)

    #return(len(animals.values()))




def main():
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    #print(animals)
    how_many(animals)






if __name__ == "__main__":
    main()