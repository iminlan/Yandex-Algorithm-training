def main():
    t_now, t_wish = input().split()
    mode = input()
    t_now = int(t_now)                  
    t_wish = int(t_wish)

    if mode == "auto":
        print(t_wish)                   # при авторежиме температура станет желаемой через час при любой исходной (условие)
    if mode == "fan":
        print(t_now)                    # при вентиляции температура воздух не поменяется
        
    if mode == "heat":
        if t_now >= t_wish:
            print(t_now)                # температура уже выше ожидаемой или такая же - кондиционер выключается
        else:
            print(t_wish)               # нагреваем воздух до необходимого значения за час
            
    if mode == "freeze":
        if t_now <= t_wish:
            print(t_now)
        else:
            print(t_wish)


if __name__ == "__main__":
    main()
