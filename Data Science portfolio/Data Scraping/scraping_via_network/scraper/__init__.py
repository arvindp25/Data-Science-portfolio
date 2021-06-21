import re
def query_finder(url):
    p_id = None
    initiative_id = None
    url_split = re.split(r"[/?]",url)
    for i in url_split:
        if re.match(r'^[0-9]+', i):
            initiative_id = re.findall(r'^[0-9]+', i)[0]

        if i.startswith("p_id="):
            p_id = i.replace("p_id=", "")

    assert p_id != None, "No p_id is found, please check your url"
    assert initiative_id != None, "No initiative_id is found, please check your url"
    return p_id, initiative_id