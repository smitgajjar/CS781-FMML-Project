from examples.CarNNBias1 import model as bb

import random
from random import choice
import math


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper



def uniform(num_of_samples):

    samples = {}

    # create 100 (features, Label) samples
    feature1_name = 'buying'
    feature2_name = 'maint'
    feature3_name = 'doors'
    feature4_name = 'persons'
    feature5_name = 'lug_boot'
    feature6_name = 'safety'


    print("----------------------")
    for i in range(num_of_samples):
        
        input_map = {}

        feature1_value = random.randint(0,3)
        print(feature1_name, ": ", feature1_value,end =" | ")
        input_map[feature1_name] = feature1_value

        feature2_value = random.randint(0,3)
        print(feature2_name, ": ", feature2_value,end =" | ")
        input_map[feature2_name] = feature2_value

        feature3_value = random.randint(0,3)
        print(feature3_value, ": ", feature3_value,end =" | ")
        input_map[feature3_name] = feature3_value

        feature4_value = random.randint(0,2)
        print(feature4_value, ": ", feature4_value,end =" | ")
        input_map[feature4_name] = feature4_value

        feature5_value = random.randint(0,2)
        print(feature5_value, ": ", feature5_value,end =" | ")
        input_map[feature5_name] = feature5_value

        feature6_value = random.randint(0,2)
        print(feature6_value, ": ", feature6_value,end =" | ")
        input_map[feature6_name] = feature6_value

        # feature2_value = truncate(abs(random.uniform(50000.0,95000.0)),4)
        # # print(feature2_name, ": ", feature2_value,end =" | ")
        # input_map[feature2_name] = feature2_value
        
        input_map_list = [feature1_value, feature2_value, feature3_value, feature4_value, feature5_value, feature6_value]

        print("input_map_list:",input_map_list)

        prediction_value = bb.execute(input_map_list)
        print(prediction_value)
        print("----------------------")
        
        samples[(feature1_name,feature1_value),(feature2_name,feature2_value),(feature3_name,feature3_value),
        (feature4_name,feature4_value), (feature5_name,feature5_value), (feature6_name,feature6_value)] = [("opclass",prediction_value)]


    return samples

