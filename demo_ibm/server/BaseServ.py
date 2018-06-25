from core._mysql import Session
import logging


class Meta(type):
    def __new__(meta_cls, cls_name, cls_parents, cls_attr):
        cls_attr['__repr__'] = lambda obj: f'<{cls_name} obj at: 0x{id(obj):x}>'

        return type.__new__(meta_cls, cls_name, cls_parents, cls_attr)


class BaseServer(metaclass=Meta):

    def __init__(self):
        self.open()

    def __del__(self):
        if self.__open:
            self.close()

    def open(self):
        self.session = Session()
        self._mq = []
        self.__open = True

    def close(self, err=None):
        assert self.__open
        self.__open = False

        if err is None:
            try:
                self.session.commit()
            except Exception as e:
                self.session.rollback()
                raise e
        else:
            logging.error(err)
            self.session.rollback()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close(value)