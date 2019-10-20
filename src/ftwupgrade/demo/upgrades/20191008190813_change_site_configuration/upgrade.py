from ftw.upgrade import UpgradeStep


class ChangeSiteConfiguration(UpgradeStep):
    """Change site configuration.
    """

    def __call__(self):
        self.install_upgrade_profile()
