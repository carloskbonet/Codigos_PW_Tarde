from datetime import datetime


def conversaoIdade(day:int , month:int , year:int):
    resDay = int(0);
    resMonth = int(0);
    resYear = int(0);

    varr = datetime.now();

    resDay = varr.day - day;
    resMonth = varr.month - month;
    resYear = varr.year - year;

    if (resDay < 0):
        resDay = 30 - (resDay * -1);
        resMonth = resMonth - 1;

    if (resMonth < 0):
        resMonth = 12 - (resMonth * -1);
        resYear = resYear - 1;

    return [resDay , resMonth , resYear];