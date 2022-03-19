def get_id_from_url_path(path):
    url_as_array = path.split("/")
    user_id = [int(item) for item in url_as_array if item.isdigit()]
    return user_id[0]
