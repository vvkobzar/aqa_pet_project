class Headers:

    basic = lambda self, token: {
        'Authorization': f"Bearer {token}"
    }