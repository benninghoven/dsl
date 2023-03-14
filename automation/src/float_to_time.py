def FloatToTime(float_hours):
    hours = int(float_hours)
    minutes = int((float_hours - hours) * 60)
    return f"{hours}:{minutes:02d}"
