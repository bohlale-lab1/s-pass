# result.py
def display_result(asset, student_id):
    if not asset:
        return "UNREGISTERED"

    if asset["student"] == student_id:
        return "AUTHORISED"
    else:
        return "DENIED"
