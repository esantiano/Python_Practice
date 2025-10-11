#region my solution
def add_time(start, duration, day = ''):
    start_colon_index = start.find(':')
    duration_colon_index = duration.find(':')
    am_pm_index = start.find(' ')
    am_pm_indicator = start[am_pm_index+1:]
    total_days = 0
    days_passed = '(next day)'
    new_day = ''
    total_hours = 0
    total_mins = 0

    if am_pm_indicator == 'PM':
        total_hours = 12

    total_mins = (int(start[start_colon_index+1:start_colon_index+3]) + int(duration[duration_colon_index+1:duration_colon_index+3]))
    total_hours = total_hours + int(start[:start_colon_index]) + int(duration[:duration_colon_index]) + total_mins//60

    if total_hours/24 >1:
        total_days = total_hours//24
        if total_hours/24 > total_hours//24 + 0.5:
            total_days = total_hours//24 + 1

    if total_days > 1:
        days_passed = f'({total_days} days later)'

    if day:
        new_day_index = 0
        normalized_day = day.lower()
        days = {
            'sunday':1,
            'monday':2,
            'tuesday':3,
            'wednesday':4,
            'thursday':5,
            'friday':6,
            'saturday':7
        }
        if total_days>0:
            new_day_index = (total_days + days[normalized_day])%7
            new_day = list(days.keys())[list(days.values()).index(new_day_index)]
            new_day = new_day[0].upper() + new_day[1:]
    
    normalized_hour = total_hours%24
    if 0 <= normalized_hour < 12:
        am_pm_indicator = 'AM'
    elif 12 <= normalized_hour < 24:
        am_pm_indicator = 'PM'
    
    if normalized_hour == 0:
        normalized_hour = 12
    elif normalized_hour > 12:
        normalized_hour = normalized_hour - 12
    normalized_hour = str(normalized_hour)
    
    total_mins = total_mins%60
    normalized_min = str(total_mins)
    if total_mins < 10:
        normalized_min = '0' + normalized_min
    
    new_time = f'{normalized_hour}:{normalized_min} {am_pm_indicator}'
    if not new_day and total_days:
        new_time = new_time + f' {days_passed}'
    elif new_day and total_days:
        new_time = new_time + f', {new_day} {days_passed}'
    if day and total_days == 0:
        new_time = new_time + f', {day}'
    return new_time
# endregion 
#region chatGPT refactor
def add_time(start, duration, day=''):
    # --- Helpers ---
    def parse_time(time_str):
        """Parse a time like '3:30 PM' into hours, minutes, and AM/PM."""
        time, period = time_str.split()
        hours, minutes = map(int, time.split(':'))
        return hours, minutes, period

    def to_24_hour(hours, period):
        """Convert to 24-hour format."""
        if period == 'PM' and hours != 12:
            return hours + 12
        if period == 'AM' and hours == 12:
            return 0
        return hours

    def format_time(hours_24, minutes):
        """Format back into 12-hour clock with AM/PM."""
        period = 'AM' if hours_24 < 12 else 'PM'
        hours_12 = hours_24 % 12 or 12
        return f"{hours_12}:{minutes:02d} {period}"

    days = ["sunday", "monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday"]

    # --- Parse start and duration ---
    start_hours, start_minutes, period = parse_time(start)
    start_hours_24 = to_24_hour(start_hours, period)
    dur_hours, dur_minutes = map(int, duration.split(':'))

    # --- Total minutes calculation ---
    total_minutes = start_hours_24 * 60 + start_minutes
    total_minutes += dur_hours * 60 + dur_minutes

    # --- Normalize ---
    total_days = total_minutes // (24 * 60)
    new_minutes = total_minutes % (24 * 60)
    new_hours_24, new_minutes = divmod(new_minutes, 60)

    # --- Format result time ---
    new_time = format_time(new_hours_24, new_minutes)

    # --- Handle day of week ---
    new_day = ''
    if day:
        start_day_idx = days.index(day.lower())
        new_day_idx = (start_day_idx + total_days) % 7
        new_day = days[new_day_idx].capitalize()
        new_time += f", {new_day}"

    # --- Handle days later suffix ---
    if total_days == 1:
        new_time += " (next day)"
    elif total_days > 1:
        new_time += f" ({total_days} days later)"

    return new_time
#endregion

#region test cases
print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00'))
print(add_time('11:59 PM', '24:05'))
print(add_time('8:16 PM', '466:02'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))
#endregion

