class Classifier:
    def __init__(self, input_str: str):
        self.input_str = input_str

    def numbers_method(self):
        return ''.join([x for x in self.input_str if x.isdigit()])

    def letters_method(self):
        return ''.join([x for x in self.input_str if x.isalpha()])

    def symbols_method(self):
        return ''.join([x for x in self.input_str if not x.isalnum()])

    def __repr__(self):
        res = self.numbers_method()
        res += f'\n{self.letters_method()}'
        res += f'\n{self.symbols_method()}'
        return res

# WITHOUT OPP
# def get_matching_chars(s: str, condition_fn):
#     result = ''
#     for char in s:
#         if condition_fn(char):
#             result += char
#     return result
#
#
# def all_digits(s: str):
#     return get_matching_chars(
#         s,
#         lambda c: c.isdigit()
#     )
#
#
# def all_letters(s: str):
#     return get_matching_chars(
#         s,
#         lambda c: c.isalpha()
#     )
#
#
# def all_others(s: str):
#     return get_matching_chars(
#         s,
#         lambda c: not c.isalnum()
#     )
#
#
# s = input()
#
# print(all_digits(s))
# print(all_letters(s))
# print(all_others(s))