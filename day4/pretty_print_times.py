
def print_formatted_data(print_data):

    print_data.sort(key=lambda x: x['month'] + x['day'] + x['hour'] + x['minute'])

    per_date_data = []

    longest_id_length = 0

    for i in range(0, len(print_data)):
        data_entry = print_data[i]

        if isinstance(data_entry['action'], int):
            current_guard = data_entry['action']

            current_guard_id_length = len(str(current_guard))
            if current_guard_id_length > longest_id_length:
                longest_id_length = current_guard_id_length

            per_date_data.append({
                'date': "{}-{}".format(data_entry['month'], data_entry['day']),
                'id': "#{}".format(current_guard),
                'minute_data': ['.' for _ in range(60)]
            })
        elif data_entry['action'] == "sleep":
            sleep_end_minute = int(print_data[i+1]['minute'])
            sleep_start_minute = int(data_entry['minute'])

            for minute in range(sleep_start_minute, sleep_end_minute):
                per_date_data[-1]['minute_data'][minute] = '#'
            # end for

            i += 1
        # end if
    # end for

    spaces_for_id = ' ' * longest_id_length

    print("Date\tID{}\tMinute".format(spaces_for_id))

    first_minute_row = ('0'*10)+('1'*10)+('2'*10)+('3'*10)+('4'*10)+('5'*10)
    print("    \t  {}\t{}".format(spaces_for_id, first_minute_row))

    second_minute_row = '0123456789' * 6
    print("    \t  {}\t{}".format(spaces_for_id, second_minute_row))

    for per_date_datum in per_date_data:
        minute_string = "".join(per_date_datum['minute_data'])
        print("{}\t{}\t{}".format(per_date_datum['date'], per_date_datum['id'], minute_string))
    # end for
# end print_formatted_data


if __name__ == "__main__":
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

    print_formatted_data(data)
# end if

