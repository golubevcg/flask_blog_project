from typing import Any


def validate_input(input_val: Any, desired_type: type, arg_name: str):
    if not input_val or not desired_type or not arg_name:
        raise ValueError(f"Cannot validate data, given arguments are empty."
                         f"(input_val:{str(desired_type)}, "
                         f"desired_type{str(desired_type)}, "
                         f"arg_name{str(arg_name)}")

    if type(arg_name) != str:
        raise TypeError(f"Cannot validate data, {arg_name} is not str.")

    if not input_val:
        raise ValueError(f"Cannot return posts by {arg_name}, "
                         f"given {arg_name} to search is empty.")

    if type(input_val) != desired_type:
        raise TypeError(f"Cannot return posts by {arg_name}, "
                        f"given {arg_name} is wrong type, must be {str(desired_type)} type.")
