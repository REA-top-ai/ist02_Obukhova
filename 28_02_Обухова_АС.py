logs = [
    "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
    "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
    "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
    "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
    "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
]

parsed_logs = []
def parsing(line):
    parts = line.split("|")

    date = parts[0]
    level = parts[1]
    message = parts[2]

    fields = message.split(" ")
    data = {}

    for f in fields:
        kv = f.split("=")
        if kv[1].isdigit():
            data[kv[0]] = int(kv[1])
        else:
            data[kv[0]] = kv[1]

    data["date"] = date
    data["level"] = level

    return data

def list_parsed_logs(list_logs):
    spisok = []
    for line in list_logs:
        data = parsing(line)
        spisok.append(data)

    return spisok

parsed_logs = list_parsed_logs(logs)

def filter_logs(list_logs, **arguments):
    res = []
    for log in list_logs:
        flag = True
        for key, value in arguments.items():
            if log.get(key) != value:
                flag = False
                break
        if flag:
            res.append(log)
    for log in res:
        print(log)

def count_by_args(list_logs, **arguments):
    counter = 0
    for log in list_logs:
        flag = True
        for key, value in arguments.items():
            if log.get(key) != value:
                flag = False
                break
        if flag:
            counter+=1
    return counter
    
def summ_for_args(list_logs, **arg):
    summ = 0
    for log in list_logs:
        flag = True
        for key, value in arg.items():
            if log.get(key) != value:
                flag = False
                break
        if flag:
            try:
                summ+=log["amount"]
            except:
                continue
    return summ

print("---- FAIL ONLY ----")
filter_logs(parsed_logs, status="fail")

print("---- ONLY ERRORS ----")
filter_logs(parsed_logs, level="ERROR")

print("---- ONLY anna's payments ----")
filter_logs(parsed_logs, user="anna", action="payment")

print("---- COUNT BY LEVEL ----")
info = count_by_args(parsed_logs,level='INFO')
error = count_by_args(parsed_logs,level='ERROR')
warning = count_by_args(parsed_logs,level='WARNING')

print(info, error, warning)

print(summ_for_args(parsed_logs, action='payment'))
