# Write a program to format a string by inserting a '/' every three characters, ensuring the total length is 9 by prepending zeros if necessary? For example, if the input is '123456', it should be converted to '000123456' and then formatted as '000/123/456'.

# hard way
# def format_string(original_string):
#     l = len(original_string)
#     if l > 9:
#         original_string = original_string[-9:]

#     multiplier = 9 - l
#     prefix = "0" * multiplier
#     original_string = prefix + original_string

#     count = 0
#     format_string = ""
#     for c in original_string:
#         if count != 0 and count % 3 == 0:
#             format_string = format_string + "/" + c
#         else:
#             format_string += c
#         count += 1
    
#     return format_string

# python way
def format_string(original_string):
    if len(original_string) > 9:
        original_string = original_string[-9:]

    padded_string = original_string.zfill(9)

    formatted_string = '/'.join(padded_string[i:i+3] for i in range(0, 9, 3))
    return formatted_string

print(format_string("123456789"))
print(format_string("123456"))
print(format_string("12345678912345"))