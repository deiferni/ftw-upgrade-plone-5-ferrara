from ftw.upgrade import UpgradeStep


class AddTalkType(UpgradeStep):
    """Add talk type.
    """

    def __call__(self):
        self.install_upgrade_profile()
