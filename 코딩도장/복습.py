sumsec = 0
for hour in range(24):
    for minute in range(60):
        if "3" in str(hour) or "3" in str(minute):
            sumsec += 60
print("하루에",sumsec,"초 3이 보입니다.")