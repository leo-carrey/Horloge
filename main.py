import time


def set_time():
    h = int(input("set hour in format 24h : "))
    m = int(input("set minute in format 24h : "))
    s = int(input("set second in format 24h : "))
    return h, m, s


def set_alarm():
    h = int(input("set alarm hour in format 24h : "))
    m = int(input("set alarm minute in format 24h : "))
    s = int(input("set alarm second in format 24h : "))
    return h, m, s


def alarm():
    userinput = input("you want set an alarm (y/n) : ")
    if userinput == "y":
        return set_alarm()
    else:
        return None, None, None


def run_time(hour, minute, second):
    second += 1
    if second >= 60:
        minute += 1
        second = 0
    if minute > 59:
        hour += 1
        minute = 0
    if hour > 23:
        hour = 0
    return hour, minute, second


def print_time(hour, minute, second,ampm):
    print('Time:{:02d}:{:02d}:{:02d}'.format(
        hour, minute, second),ampm, end='\r')


def main():
    alarm_hour, alarm_minute, alarm_second = alarm()
    hour, minute, second = set_time()
    format = input("choose your time format (24/12) :")
    while True:
        time.sleep(1)
        hour, minute, second = run_time(hour, minute, second)
        if format == "24":
            print_time(hour, minute, second,"")
        elif f'{alarm_hour}:{alarm_minute}:{alarm_second}' == f'{hour}:{minute}:{second}':
            print_time(hour, minute, second,"")
            print('Its Time !!!! :  ')
        if format == "12":
            if hour > 12:
                mini_hour = 1
                print_time(mini_hour, minute, second,"PM")
            elif f'{alarm_hour}:{alarm_minute}:{alarm_second}' == f'{hour}:{minute}:{second}':
                print_time(mini_hour, minute, second,"PM")
                print('Its Time !!!! :  ')
            else:
                print_time(hour, minute, second,"AM")
                if f'{alarm_hour}:{alarm_minute}:{alarm_second}' == f'{hour}:{minute}:{second}':
                    print_time(hour, minute, second,"AM")
                    print('Its Time !!!! :  ')


main()
