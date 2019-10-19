from ftw.upgrade import UpgradeStep


class SetTalkTitle(UpgradeStep):
    """Set talk title.
    """

    def __call__(self):
        for talk in self.objects({'portal_type': 'talk'},
                                 'Set talk title'):
            self.set_talk_title(talk)

    def set_talk_title(self, talk):
        talk.title = u'Talk {}'.format(talk.getId())
        talk.reindexObject(idxs=['Title'])
