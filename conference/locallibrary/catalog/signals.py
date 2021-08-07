def populate_models(sender, **kwargs):
    from django.contrib.auth.models import Group

    Group.objects.get_or_create(name='admin')
    Group.objects.get_or_create(name='listener')
    Group.objects.get_or_create(name='presenter')
