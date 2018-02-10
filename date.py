import datetime, dateparser
from recurrent import RecurringEvent
from freezegun import freeze_time

r = RecurringEvent()


# returns ranges for days, weeks, months
def getDate(inputString):
    return r.parse(inputString)


def getOffset(inputTimeUnit):
    if "day" in inputTimeUnit:
        return 86400
    elif "week" in inputTimeUnit:
        return 604800
    elif "month" in inputTimeUnit:
        return 2592000


def getDateUni(inputString):
    # stringParts = inputString.split()
    start = int(getDate(inputString).timestamp())

    if "day" in inputString:
        return (start, start + getOffset("day"))
    elif "week" in inputString:
        return (start, start + getOffset("week"))
    elif "month" in inputString:
        return (start, start + getOffset("month"))

    return None


def test():
    # assumes dates is feb 10, 2018
    testcases = ["yesterday", "last week", "last month"]
    yest_start = int(dateparser.parse('feb 9, 2018 UTC').timestamp())
    yest_end = int(dateparser.parse('feb 10, 2018 UTC').timestamp()) - 1
    today_start = int(dateparser.parse('feb 10, 2018 UTC').timestamp())
    today_end = int(dateparser.parse('feb 11, 2018 UTC').timestamp()) - 1
    lastweek_start = int(dateparser.parse('feb 2, 2018 UTC').timestamp())
    lastweek_end = int(dateparser.parse('feb 10, 2018 UTC').timestamp()) - 1
    expected = [(yest_start, yest_end), (lastweek_start, lastweek_start), ]

    for i in range(len(testcases)):
        print(testcases[i])
        assert (getDateUni(testcases[i]) == expected[i])


if __name__ == "__main__":
    test()
