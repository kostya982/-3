def find_common_participants(participants1, participants2, separator=','):
    first_group = participants1.split(separator)
    second_group = participants2.split(separator)

    common_participants = list(set(first_group).intersection(second_group))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", result)