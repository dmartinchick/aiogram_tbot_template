def get_unsubs_list(list_all, list_subs):
    user_teams_unsubs = []
    for team in list_all:
        if team not in list_subs:
            user_teams_unsubs.append(str(team[0]))

    return user_teams_unsubs


def convert_to_list(tuple):
    list_result = []
    for item in tuple:
        list_result.append({'name':item[0], 'id':item[1]})
    return list_result