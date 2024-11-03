def find_common_participants(str1, str2, n=','):
    participants1 = str1.split(n)
    participants2 = str2.split(n)

    common = list(set(participants1).intersection(participants2))
    common.sort()

    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, n='|')
print("Общие участники:", common_participants)


