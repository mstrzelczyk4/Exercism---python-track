def transform(legacy_data):
    return {c.lower(): key for key, value in legacy_data.items() for c in value}
