import json

json_file = "card_list.json"
full_deck_json_key = "fullDeck"
numbers_json_key = "numberCards"
action_json_key = "actionCards"
wild_json_key = "wilds"


def read_json(file_name: str) -> dict:
    """Read full json file"""
    with open(file_name, 'r') as f:
        data: dict = json.load(f)
    return data


def read_json_by_key(file_name: str, key: str) -> list:
    """Read json file by key"""
    with open(file_name, 'r') as f:
        data: list = json.load(f)[key]
    return data


def get_full_card_list() -> list:
    """Get full card list"""
    return read_json_by_key(json_file, "fullDeck")


def get_card_list_by_key(key) -> list:
    """Get card list by key"""
    return read_json_by_key(json_file, key)


def get_number_card_list() -> list:
    """Get number card list"""
    return get_card_list_by_key(numbers_json_key)


def get_action_card_list() -> list:
    """Get action card list"""
    return get_card_list_by_key(action_json_key)


def get_wild_card_list() -> list:
    """Get wild card list"""
    return get_card_list_by_key(wild_json_key)
