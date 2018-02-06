from masonite.exceptions import DriverNotFound
from masonite.managers.Manager import Manager

class MailManager(Manager):

    def create_driver(self, driver=None):
        if not driver:
            driver = self.container.make('MailConfig').DRIVER.capitalize()
        else:
            driver = driver.capitalize()

        try:
            self.manage_driver = self.container.make('Mail{0}Driver'.format(driver))
        except KeyError:
            raise DriverNotFound('Could not find the Mail{0}Driver from the service container. Are you missing a service provider?'.format(driver))
