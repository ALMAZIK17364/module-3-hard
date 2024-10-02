def sum_extractor(material):
    final_cnt = 0
    for cur_element in material:
        if isinstance(cur_element, int):
            final_cnt += cur_element

        elif isinstance(cur_element, str):
            final_cnt += len(cur_element)

        elif isinstance(cur_element, (list, tuple, set)):
            final_cnt += sum_extractor(cur_element)

        elif isinstance(cur_element, dict):
            final_cnt += sum_extractor(cur_element)
            final_cnt += sum_extractor(cur_element.keys())

    return final_cnt


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

print(sum_extractor(data_structure))