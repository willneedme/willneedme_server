from datetime import datetime, timedelta


def yearMonthDay(days):
    filter_after = datetime.today() + timedelta(days=days)
    split = filter_after.isoformat().split("-")
    year = split[0]
    month = split[1]
    day = split[2][0:2]
    return year + month + day
