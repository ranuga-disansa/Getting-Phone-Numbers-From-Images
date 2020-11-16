import re
import pytesseract
from PIL import Image
import csv
import os
import random

gibiris = "fewgyugrdauhiretui8resdhsdujfhyreuirrduhgfdkhjfghtyriurirghrdsfjghbfdjhjfghdjfghbjrkdhgtjksdfasfkjeswhgjshjlghfjgthsdklfhsdjuthewitr3oi47545475yt6rytr6fewgyugrdauhiretui8resdhsdujfhyreuirrduhgfdkhjfghtyriurirghrdsfjghbfdjhjfghdjfghbjrkdhgtjksdfasfkjeswhgjshjlghfjgthsdklfhsdjuthewitr3oi47545475yt6rytr6fewgyugrdauhiretui8resdhsdujfhyreuirrduhgfdkhjfghtyriurirghrdsfjghbfdjhjfghdjfghbjrkdhgtjksdfasfkjeswhgjshjlghfjgthsdklfhsdjuthewitr3oi47545475yt6rytr6fewgyugrdauhiretui8resdhsdujfhyreuirrduhgfdkhjfghtyriurirghrdsfjghbfdjhjfghdjfghbjrkdhgtjksdfasfkjeswhgjshjlghfjgthsdklfhsdjuthewitr3oi47545475yt6rytr6fewgyugrdauhiretui8resdhsdujfhyreuirrduhgfdkhjfghtyriurirghrdsfjghbfdjhjfghdjfghbjrkdhgtjksdfasfkjeswhgjshjlghfjgthsdklfhsdjuthewitr3oi47545475yt6rytr6fewgyugrdauhiretui8resdhsdujfhyreuirrduhgfdkhjfghtyriurirghrdsfjghbfdjhjfghdjfghbjrkdhgtjksdfasfkjeswhgjshjlghfjgthsdklfhsdjuthewitr3oi47545475yt6rytr6+td6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56rtd6td56rtre46t5e424w3etrwetretwqewretg43euyteughuwetyuiehguserytuer3tiryiuyrey8re96gh5er6y5er9y8er65hr6ey8459y5her6yher879r6yh5er9y68549td56r"
gibiries = []
totla = []
not_add_numbers = []


def check_if_a_number_doesnt_already_exists(number):
    number = {number}
    for x in totla:
        if x == number:
            return False
    return True


def detect_numbers(text):
    phone_regex = re.compile(r"(\+94)?\s*?(\d{2})\s*?(\d{3})\s*?(\d{4})")
    return phone_regex.findall(text)


def get_info(images_names: list):
    for image in images_names:
        value = Image.open(image)
        text = pytesseract.image_to_string(value, config="")
        text_filtered = text.upper()
        result = detect_numbers(text_filtered)
        print(result)
        for x in result:
            final_string = ""
            for m in x:
                final_string = final_string + str(m)
            conditions = [
                final_string in not_add_numbers,
                check_if_a_number_doesnt_already_exists(final_string) is False,
            ]
            if any(conditions):
                pass
            else:
                random_thing = "ABCD"
                for x in range(
                    random.randint(112, random.randint(250, random.randint(289, 598)))
                ):
                    random_thing = random_thing + gibiris[x]
                if random_thing in gibiries:
                    for x in range(
                        random.randint(
                            112, random.randint(250, random.randint(289, 598))
                        )
                    ):
                        random_thing = random_thing + gibiris[x]
                        random_thing = random_thing + gibiris[x]
                    if random_thing in gibiries:
                        random_thing = (
                            str(gibiries[random.randint(0, len(gibiries))])
                            + str(gibiries[random.randint(0, len(gibiries))])
                            + str(gibiries[random.randint(0, len(gibiries))])
                            + str(gibiries[random.randint(0, len(gibiries))])
                        )
                    gibiries.append(random_thing)
                else:
                    gibiries.append(random_thing)
                print(final_string[1:])
                totla.append({"Number": final_string[1:], "Random Thing": random_thing})


def change_the_extention_to_png(file_names):
    for x in file_names:
        a = "directory of this file" + x
        os.rename(a, os.path.splitext(x)[0] + ".png")


file_names = os.listdir()
file_names.remove("test.py")
file_names.remove("info.csv")
get_info(file_names)

print("adding to file")
fields = ["Number", "Random Thing"]
with open("info.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(totla)
