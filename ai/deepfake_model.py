import random


def predict(face):

    """
    Dummy prediction.
    Later this will use a real AI model.
    """

    score = random.randint(70, 99)

    if score > 85:
        status = "Fake"
    else:
        status = "Real"

    return {
        "status": status,
        "confidence": score
    }
