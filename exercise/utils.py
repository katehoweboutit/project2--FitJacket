from .models import Exercise
import requests

muscle_groups = ["abdominals","abductors", "adductors", "biceps", "calves",
                 "chest", "forearms", "glutes", "hamstrings", "lats", "lower_back",
                 "middle_back", "neck", "quadriceps", "traps", "triceps"]


def create_new_exercises(api_response):
    for exercise_info in api_response:
        Exercise.objects.create(
            muscle_group=exercise_info['muscle'],
            name=exercise_info['name'],
            equipment_needed=exercise_info['equipment'],
            instructions=exercise_info['instructions']
        )

def update_db_exercises(muscle_groups):
    """
    Given a list of muscle groups, adds each corresponding exercise to the database
    as an Exercise object. Does this by calling the Exercise API

    :param muscle_groups: muscle groups to add the exercises of to the db
    :return: None
    """
    for muscle_group in muscle_groups:
        if muscle_group in Exercise.objects.values_list('muscle_group', flat=True):
            continue

        api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={muscle_group}'
        response = requests.get(api_url, headers={'X-Api-Key': 'OKMD5CjRpp/+YzrvUO4PRw==e4bBrbFUzF62n4Aj'})
        if response.status_code == requests.codes.ok:
            create_new_exercises(response.json())

        else:
            print(f"The Exercise API is down and gave an error: {response.text}")
            return
