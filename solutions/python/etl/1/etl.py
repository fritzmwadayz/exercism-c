def transform(legacy_data):
    transformed_data = {}

    for key, value in legacy_data.items():
        for item in value:
            transformed_data[item.lower()] = key

    return transformed_data
