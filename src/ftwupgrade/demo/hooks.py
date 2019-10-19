from plone import api


def default_profile_installed(site):
    for i in range(1001):
        api.content.create(site, type='talk', title='foo')
