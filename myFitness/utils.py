from exercise.utils import all_muscle_groups
from exercise.models import ExerciseAssignment

def get_user_activity_by_muscle(user):
    """
    given a user, returns a dictionary in the format {muscle_group : duration...}
    where muscle_group is a string containing the name of a muscle group and
    duration is an int corresponding to the total number of minutes the user
    has spent working out that muscle group, only considering completed exercises.
    :param user: to get the information for
    :return: a dictionary {muscle_group : duration...} of length len(all_muscle_groups)
    """

    user_activity = {}
    # gets a list of all the exercise assignments this user has completed
    all_user_exercises = ExerciseAssignment.objects.filter(user=user, completed=True)

    # for each muscle group (each key in the dictionary to be returned)
    for muscle_group in all_muscle_groups:
        # first get a list of all the exercises the user has completed in this muscle group
        muscle_exercises = all_user_exercises.filter(exercise__muscle_group=muscle_group)

        # then sum up their total time spent doing each exercise
        muscle_time_spent = 0
        for exercise in muscle_exercises:
            muscle_time_spent += exercise.duration_minutes

        # create a key in the return dictionary whose value is the total time for that muscle group
        user_activity[muscle_group] = muscle_time_spent

    return user_activity