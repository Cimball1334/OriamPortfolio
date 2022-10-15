def find_word_values_list(words_list, letter_points_dct):
    sums = 0
    word_points_list = []
    
    #each entry word
    for word in words_list:
        #each character in word
        for c in word:
            for key in letter_points_dct.keys():
                if c == key:
                    sums += letter_points_dct[key]
        word_points_list.append(sums)
        sums = 0



    return word_points_list


print(find_word_values_list(['cucumber', 'telephone', 'potato', 'giraffe'], {'a':1, 'b':2, 'e':0, 'o':9, 'p':11}))

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_pts = {}
for i in range( len(alphabet) ):
    letter_pts[ alphabet[i] ] = i

print(find_word_values_list(['cool','colorless','cranberries','congratulate'], letter_pts))
