import csv
import datetime
import subprocess


def speed_test():
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sped_test_cmd = "speedtest-cli --simple"
    proscess = subprocess.run(sped_test_cmd.split(), stdout=subprocess.PIPE, encoding="utf-8")

    process_output = proscess.stdout
    process_output = process_output.split()
    process_output.append(date_time)
    return process_output


def save_to_csv(data, filename):
    try:
        with open(filename + ".csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except FileNotFoundError:
        with open(filename + ".csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except Exception as e:
        print("Unhandled exception:", e)


def print_from_csv(filename):
    with open(filename + ".csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" ".join(row))


def main():
    for i in range(5):
        speedtest_output = speed_test()
        print("Test number: {}".format(i))
        print(speedtest_output)
        save_to_csv(speedtest_output, 'test')

    print_from_csv("test")


if __name__ == '__main__':
    main()