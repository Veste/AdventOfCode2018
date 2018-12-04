data = []

with open('input') as input_file:
    for input_line in input_file:
        line_data = {}

        line_split = input_line.split()

        date_section = line_split[0].split('-')
        line_data['month'] = date_section[1]
        line_data['day'] = date_section[2]

        time_section = line_split[1].split(':')
        line_data['hour'] = time_section[0]
        line_data['minute'] = time_section[1][:-1]

        text_section = line_split[2:]
        if text_section[0] == "Guard":
            line_data['action'] = int(text_section[1][1:])
        elif text_section[0] == 'falls':
            line_data['action'] = "sleep"
        else:
            line_data['action'] = "wakeup"
        # end if

        data.append(line_data)
    # end for
# end with

data.sort(key=lambda x: x['month'] + x['day'] + x['hour'] + x['minute'])

per_guard_data = {}

# Assume the first entry is a guard shift

current_guard = data[0]['action']
print("{}: {}".format(current_guard, data[0]))

for i in range(1, len(data)):
    data_entry = data[i]
    print("{}: {}".format(current_guard, data_entry), end='')
    if isinstance(data_entry['action'], int):
        current_guard = data_entry['action']
        print()
    elif data_entry['action'] == "sleep":
        sleep_end_minute = int(data[i+1]['minute'])
        sleep_start_minute = int(data_entry['minute'])
        sleep_time = sleep_end_minute - sleep_start_minute
        print("; Sleep time for {} is increasing by {}".format(current_guard, sleep_time))

        if current_guard not in per_guard_data:
            per_guard_data[current_guard] = [0 for _ in range(60)]
        # end if

        for minute in range(sleep_start_minute, sleep_end_minute):
            per_guard_data[current_guard][minute] += 1
        # end for

        i += 1
    else:
        print()
    # end if
# end for

largest_sleep_minute_count = -1
largest_minute = -1
largest_minute_guard = -1
print()
for guard_num, guard_info in per_guard_data.items():
    print("{:0>4d}: {}".format(guard_num, guard_info))
    max_minute_amount = max(guard_info)
    if max_minute_amount > largest_sleep_minute_count:
        largest_sleep_minute_count = max_minute_amount
        largest_minute = [j for j, k in enumerate(guard_info) if k == max_minute_amount][0]
        largest_minute_guard = guard_num

print("\n{} x {} = {}".format(largest_minute_guard, largest_minute, largest_minute_guard * largest_minute))


