from StdSuites.Text_Suite import word
import pickle

lines = []
Person_tag = "_TYPE_PERSON"
Time_tag = "_TYPE_TIME"
# Number_tag = "_TYPE_NUMBER"
Oragnization_tag ="_TYPE_ORGANIZATION"
vocab_size = 0
relvocab_size = 0
word_dict = {}
rel_dict = {}

def cleaning(ATypes, A):
    if "," in ATypes:
        A1_Types_comma = ATypes.split(",")
        for type in A1_Types_comma:
            A1_Types_colon = type.split(":")
            for colon in A1_Types_colon:
                if "person" in colon:
                    A = Person_tag
                if "time_unit" in colon:
                    A = Time_tag
                # if "number" in colon:
                #     A = Number_tag
                if "organization" in colon:
                    A = Oragnization_tag
    else:
            A1_Types_colon = ATypes.split(":")
            for colon in A1_Types_colon:
                if "person" in colon:
                    A = Person_tag
                if "time_unit" in colon:
                    A = Time_tag
                # if "number" in colon:
                #     A = Number_tag
                if "organization" in colon:
                    A = Oragnization_tag
    return A



with open("1987_01_tuples.txt") as f:
    lines = f.readlines()

for line in lines:
    split_line = line.split("|")
    A1 = split_line[1]
    A1Types = split_line[2]
    rel = split_line[4]
    A2 = split_line[6]
    A2Types = split_line[7]
    print(A2)
    A1 = cleaning(A1Types,A1)
    A2 = cleaning(A2Types,A2)


    print(A2)
    # print(A1)
    if(not word_dict.has_key(A1)):
        word_dict[A1] = vocab_size
        vocab_size += 1
    if(not word_dict.has_key(A2)):
        word_dict[A2] = vocab_size
        vocab_size += 1
    if(not rel_dict.has_key(rel)):
        rel_dict[rel] = relvocab_size
        relvocab_size += 1

print(word_dict)
print("---------")
print(rel_dict)
pickle.dump( word_dict, open( "word.pkl", "wb" ) )
pickle.dump( rel_dict, open( "rel.pkl", "wb" ) )
