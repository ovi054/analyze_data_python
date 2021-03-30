import temperature, report

def main():
    # gather data
    filename = input('file?\n')
    print('file:',filename)
    temperature.readData(filename)
    # process requests
    prompt = 'report?\n'
    command = input(prompt)
    while command != "" and command[0:4].lower() != 'stop':
        print('report:',command)
        processRequest(command)
        command = input(prompt)


def processRequest(command):
    if command[0:7].lower() == 'average':
        report.average(command)
    elif command[0:5].lower() == 'table':
        report.table(command)
    else:
        print('Unknown report:', command)


if __name__ == "__main__":
    main()