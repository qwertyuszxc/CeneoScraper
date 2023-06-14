def get_element(ancestor, selector = None, attribute = None, return_list = False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except (AttributeError,TypeError):
        return None