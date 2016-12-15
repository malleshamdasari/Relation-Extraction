import pickle
import numpy as np

Person_tag = "_TYPE_PERSON"
Time_tag = "_TYPE_TIME"
# Number_tag = "_TYPE_NUMBER"
Oragnization_tag ="_TYPE_ORGANIZATION"
word_dict = pickle.load( open( "word.pkl", "rb" ) )
rel_dict = pickle.load( open( "rel.pkl", "rb" ) )
# print(word_dict)
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


# print((word_dict))
# A1_hot = np.zeros((len(word_dict.keys()),1))
# A2_hot = np.zeros((len(word_dict.keys()),1))
# rel_hot = np.zeros((len(rel_dict.keys()),1))


def hotvec(A1,rel, A2 ):
    A1_hot = np.zeros((len(word_dict.keys()),1))
    A2_hot = np.zeros((len(word_dict.keys()),1))
    rel_hot = np.zeros((len(rel_dict.keys()),1))
    pos_A1 = int((word_dict[A1]))
    A1_hot[pos_A1] = 1
    pos_rel = int((rel_dict[rel]))
    rel_hot[pos_rel] = 1
    pos_A2 = int((word_dict[A2]))
    A2_hot[pos_A2] = 1
    return np.concatenate([A1_hot,rel_hot,A2_hot],axis=0)
    # return A1_hot, rel_hot, A2_hot


with open("1987_01_tuples.txt") as f:
    lines = f.readlines()

for line in lines:
    split_line = line.split("|")
    A1 = split_line[1]
    A1Types = split_line[2]
    rel = split_line[4]
    A2 = split_line[6]
    A2Types = split_line[7]
    A1 = cleaning(A1Types,A1)
    A2 = cleaning(A2Types,A2)

    threehotvector = hotvec(A1,rel,A2)

    # print(A1+ " "+rel + " "+A2)
    # print(a)
    # print('--')
    # print(b)
    # print('-----')
    # print(c)
    # print("+++++")
    # print(np.concatenate([a,b,c],axis=0))
    # threehotvector = np.concatenate([a,b,c],axis=0)
    # print threehotvector
    # print("=========")
    # threehotvector = np.concatinate([temp,c],axis=0)
    # print(threehotvector)

# print(word_dict)
# print(rel_dict)
print("done")

# for item in word_dict:
#     print item
#     print word_dict[item]
