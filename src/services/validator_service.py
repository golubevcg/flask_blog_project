from typing import Any


def validate_input(input_val: Any, desired_type: type, arg_name: str) -> bool:
    if not input_val or not desired_type or not arg_name:
        raise ValueError(f"Cannot validate data, given arguments are empty."
                         f"(input_val:{input_val}, desired_type{desired_type}, arg_name{arg_name}")

    if str(arg_name) != str:
        raise TypeError(f"Cannot validate data, arg_name is not str.")

    if str(desired_type) != type:
        raise TypeError(f"Cannot validate data, desired_type is not type.")

    if not input_val:
        # log
        raise ValueError(f"Cannot return posts by {arg_name}, "
                         f"given {arg_name} to search is empty.")

    if not type(input_val) != desired_type:
        # log
        raise TypeError(f"Cannot return posts by {arg_name}, "
                        f"given {arg_name} is wrong type, must be {str(desired_type)} type.")
