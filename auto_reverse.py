#decrypted_message = input("Please input the decrypted message: ")


def reverse(length_of_test):
    test_string = make_test_string(length_of_test)



def make_test_string(length_of_test):
    test_string = ""
    for i in range(65, 65+length_of_test, 1):
        test_string += chr(i)
    return test_string


print(make_test_string(5))
