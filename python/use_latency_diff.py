import numpy as npimport latency_differencefrom scipy.io import loadmat# used loadmat of scipy.io to load my example data mat file and:data = loadmat("/Users/mahan/sciebo/Matlab_N2pcP3/example_series_N2pcP3s")query = data["N2pc_Intrusion"]reference = data["N2pc_Correct"]name_query = "Intrusion"name_reference = "Correct"units = "\u03BCV"sampling_rate = 500filepath = "/Users/mahan/sciebo/PythonCode/N2pcP3"permutations = 10000latency_difference.main(    "within", query, reference, name_query, name_reference, units, sampling_rate,    filepath, permutations    )# latency_difference.main(#     "between", query, reference, name_query, name_reference, units, sampling_rate,#     filepath, permutations#     )