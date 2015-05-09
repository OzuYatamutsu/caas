import mongoengine

user = authenticate(username=username, password=password)
assert isinstance(user, mongoengine.django.auth.User)
