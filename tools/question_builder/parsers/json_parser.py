def parse_json_material(content):
    if isinstance(content, list):
        return content

    return [content]