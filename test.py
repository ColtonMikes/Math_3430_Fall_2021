def add_vectors(vector_a,vector_b):
    """
    """
    result = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result


test_vector_01 = [1,2,3]
test_vector_02 = [4,3,2]


print(add_vectors(test_vector_01,test_vector_02))


