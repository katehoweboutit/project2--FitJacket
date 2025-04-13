from .models import Exercise
import requests

muscle_groups = ['abdominals', 'abductors', 'adductors', 'biceps', 'calves',
                 'chest', 'forearms', 'glutes', 'hamstrings', 'lats', 'lower_back',
                 'middle_back', 'neck', 'quadriceps', 'traps', 'triceps']

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

def get_gpt_prompt(user, exercise_options):
    cardinality_indicators = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
                              'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth',
                              'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth']

    single_exercise = len(exercise_options) == 1

    prompt = (f"Your job is to recommend {len(exercise_options)} exercise{'s' * (not single_exercise)} "
    f"to the user of a fitness recommendation website.\nThis user is {user.age} years old, and their weight "
    f"is {user.weight} lbs. Here are some optional lifestyle habits the user entered when they made their account:"
    f"\n\"{user.LifestyleHabits}\"\n"
    f"And here are some optional additional notes the user entered when they made their account:"
    f"\n\"{user.AdditionalNotes}\"\n"

    f"\nYou will recommend {len(exercise_options)} exercise{'s' * (not single_exercise)}.")

    for index, exercise_option_group in enumerate(exercise_options):
        prompt += (f"\nfor the {(not single_exercise) * cardinality_indicators[index]} exercise that you "
        f"recommend, pick one from the following exercises:\n[")
        for exercise_option in exercise_option_group:
            prompt += f"{exercise_option}, "
        prompt = prompt[:-2] + ']\n' # remove the redundant comma from the last exercise

    prompt += (f"\nThen for {('the' * single_exercise) + ('each' * (not single_exercise))} exercise, decide on a "
    f"duration (in minutes) that the user should spend doing the exercise, keeping in mind their age, "
    f"weight, and lifestyle habits. Also come up with a number that is a multiple of 5, 5-100 that "
    f"represents the difficulty and duration of the exercise\n\n"

    f"Please respond in the following format:")

    if single_exercise:
        prompt += """
Exercise 1:
name: {name of the exercise you chose}
duration: {duration} minutes
difficulty: {number 5-100 to represent difficulty}
"""
    else:
        prompt += """
Exercise 1:
name: {name of the first exercise you chose}
duration: {duration} minutes
difficulty: {number 5-100 to represent difficulty}

Exercise 2:
name: {name of the second exercise you chose}
duration: {duration} minutes
difficulty: {number 5-100 to represent difficulty}
""" + ("\n..." * (len(exercise_options) > 2))

    return prompt



def get_api_exercises_response(user, exercise_options):
    prompt = get_gpt_prompt(user, exercise_options)
    print(prompt)


def update_assigned_exercises(user, muscle_groups):
    """
    given a user and a list of muscle groups, adds one ExerciseAssignment to the database
    belonging to that user for each muscle group. Does this with an OpenAI API call
    :param user: that the new ExerciseAssignments will belong to
    :param muscle_groups: one ExerciseAssignment will be added per muscle group
    :return: None
    """
    if len(muscle_groups) == 0:
        return

    exercise_options = []
    for muscle_group in muscle_groups:
        # gets a list of all the names of all the exercises in all the muscle groups
        exercise_options.append(Exercise.objects.filter(
                muscle_group=muscle_group).values_list('name', flat=True))

    api_response = get_api_exercises_response(user, exercise_options)
