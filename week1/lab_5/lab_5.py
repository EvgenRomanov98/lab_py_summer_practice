import re  # подключение регулярных выражений


def findNmuOne(f):
    regex = re.compile(r"(\w+\.\w+){2}@nmu\.one$")
    return [regex.search(l).group() for l in f if regex.search(l)]


def findDotOrZero(file):
    regex = re.compile(r"^\w*[0|\\.]{1}\w*@.+$")
    return [regex.search(i).group() for i in file if regex.search(i)]


def main():
    with open("emails_lab5.txt", 'r') as file:
        nmuOne = findNmuOne(file)
        file.seek(0)
        dotOrZero = findDotOrZero(file)
    print("Почты, имеют три слова разделенные точкой в левой части и в правая домен nmu.one:\n", nmuOne)
    print("В левой части имеют одну точку или ноль:\n", dotOrZero)


main()
