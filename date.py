import dateparser
import moment


# returns ranges for days, weeks, months
def getDate(inputString):
    return moment.date(inputString).timezone("UTC").zero.date


def getOffset(inputTimeUnit):
    if "day" in inputTimeUnit:
        return 86400
    elif "week" in inputTimeUnit:
        return 604800
    elif "month" in inputTimeUnit:
        return 2592000


def getDateUnix(inputString):
    # stringParts = inputString.split()
    start = int(getDate(inputString).timestamp())

    if "day" in inputString:
        return (start, start + getOffset("day") - 1)
    elif "week" in inputString:
        return (start, start + getOffset("week") - 1)
    elif "month" in inputString:
        return (start, start + getOffset("month") - 1)

    return None


def test():
    # assumes dates is feb 10, 2018
    testcases = ["yesterday", "last week", "last month"]
    yest_start = int(dateparser.parse('feb 9, 2018 UTC').timestamp())
    yest_end = int(dateparser.parse('feb 10, 2018 UTC').timestamp()) - 1

    today_start = int(dateparser.parse('feb 10, 2018 UTC').timestamp())
    today_end = int(dateparser.parse('feb 11, 2018 UTC').timestamp()) - 1

    lastweek_start = int(dateparser.parse('feb 3, 2018 UTC').timestamp())
    lastweek_end = int(dateparser.parse('feb 10, 2018 UTC').timestamp()) - 1

    lastmonth_start = int(dateparser.parse('jan 10, 2018 UTC').timestamp())
    lastmonth_end = int(dateparser.parse('feb 10, 2018 UTC').timestamp()) - 1

    expected = [(yest_start, yest_end), (lastweek_start, lastweek_end), (lastmonth_start, lastmonth_end)]

    for i in range(len(testcases)):
        print(testcases[i], getDateUnix(testcases[i]), expected[i])
        assert (getDateUnix(testcases[i]) == expected[i])


if __name__ == "__main__":
    test()
