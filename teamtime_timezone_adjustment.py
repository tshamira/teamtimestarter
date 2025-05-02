def timezone_adjustment(timezone):
    # timezone is a string of three or four character denoting the timezone that the user is using the app in.
    # something tricky about timezones is that they can change depending on the time of year (due to daylight savings time).. will try to account for this
    format = '%H:%M:%S'
    game_start_time_ET = datetime.strptime(game['etm'][-8:], '%H:%M:%S')

    # USA
    if timezone == "EST":
        # UTC -05
        game_start_times.append(game_start_time)
    elif timezone == "CST":
        game_start_time = (game_start_time_ET - datetime.strptime("01:00:00", format))
        game_start_times.append(game_start_time)
    elif timezone == "MST":
        game_start_time = (game_start_time_ET - datetime.strptime("02:00:00", format))
        game_start_times.append(game_start_time)
    elif timezone == "PST":
        game_start_time = (game_start_time_ET - datetime.strptime("03:00:00", format))
        game_start_times.append(game_start_time)
    elif timezone == "AKST":
        game_start_time = (game_start_time_ET - datetime.strptime("04:00:00", format))
        game_start_times.append(game_start_time)
    elif timezone == "HST":
        game_start_time = (game_start_time_ET - datetime.strptime("05:00:00", format))
        game_start_times.append(game_start_time)
    else:
        print("Incorrect/missing timezone.")
        break
