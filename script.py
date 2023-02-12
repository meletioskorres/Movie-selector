from data import *
from linked_list import*


#Initializes a LinkedList with name movie_type_list that holds all the genres from data.py
def insert_movie_types():
    movie_type_list = LinkedList()
    for movie_type in types:
        movie_type_list.insert_beginning(movie_type)
    return movie_type_list


def insert_movie_data():
    movie_data_list = LinkedList()
    for movie_type in types:
        movie_sublist = LinkedList()
        for movie in top_50_movies:
            if movie[2] == movie_type:
                movie_sublist.insert_beginning(movie)
        movie_data_list.insert_beginning(movie_sublist)
    return movie_data_list

my_type_list = insert_movie_types()
my_movie_list = insert_movie_data()


selected_movie_type = ""

while len(selected_movie_type) == 0:

    user_input = str(input("What movie genre would you like to watch today? Type the begginning of the genre to see if its here\n")).lower()


    matching_types = []
    type_list_head = my_type_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).lower().startswith(user_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()


    for movie in matching_types:
        print(movie)


    if len(matching_types) == 1:
        select_type = str(input("""The only matching type is {}. Do you want to look at {} movies?
        Enter y for yes and n for no\n""".format(matching_types[0], matching_types[0]))).lower()

        if select_type == "y":
            selected_movie_type = matching_types[0]
            print("Selected Movie Genre: " + selected_movie_type)
            movie_list_head = my_movie_list.get_head_node()
            while movie_list_head.get_next_node() is not None:
                sublist_head = movie_list_head.get_value().get_head_node()
                if sublist_head.get_value()[2] == selected_movie_type:
                    while sublist_head.get_next_node() is not None:
                        print("--------------------------")
                        print("Name: " + sublist_head.get_value()[0])
                        print("Director: " + sublist_head.get_value()[1])
                        print("Rating: {}".format(sublist_head.get_value()[3]))
                        print("Length: " + str(sublist_head.get_value()[4]))
                        print("--------------------------")
                        sublist_head = sublist_head.get_next_node()
                movie_list_head = movie_list_head.get_next_node()