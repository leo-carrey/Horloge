import time

temps = True

def clock(hour, minute, seconde):

    temps = True
    hour = int(input("Enter hour :")) # valeur entrée par Utilisateur
    minute = int(input("Enter minute :"))
    seconde = int(input("Enter seconde :"))
    alarm_seconde = ""
    alarm_hour = ""
    alarm_minute = ""
    h_empty=""
    m_empty=""
    s_empty=""

    print("Voulez-vous programmez un reveil ? (y/n)" )
    alarme = input()

    if alarme == "y":
        print("Enter hour :")
        alarm_hour = int(input())
        print("Enter minute :")
        alarm_minute = int(input())
        print("Enter seconde :")
        alarm_seconde = int(input())

    while temps:
        time.sleep(1)
        seconde += 1
        if seconde > 59:
            minute += 1
            seconde = 0
        if minute > 59:
            hour += 1 # valeur entrée par utilisateur + 1
            minute = 0
        if hour > 23:
            hour = 0
        if hour <= 9:
            h_empty = '0'
        else:
            h_empty = ''
        if minute <= 9:
            m_empty = '0'
        else:
            m_empty = ''
        if seconde <= 9:
            s_empty = '0'
        else:
            s_empty = ''

        if alarm_hour == hour and alarm_minute == minute and alarm_seconde == seconde:
            print("time: " + h_empty + str(hour) + ":" + m_empty + str(minute) + ":" + s_empty + str(seconde), "it's time !!!", end='\r')    
        else:
            print("time: " + h_empty + str(hour) + ":" + m_empty + str(minute) + ":" + s_empty + str(seconde), "              ",end="\r")

clock(00,00,00)