from ftw.upgrade import UpgradeStep
from plone import api


class AddTalkType(UpgradeStep):
    """Add talk type.
    """

    def __call__(self):
        self.install_upgrade_profile()

        for i in range(1001):
            api.content.create(self.portal, type='talk', title='foo')
