from django.core.mail.backends.console import EmailBackend as ConsoleBackend

from django_mailjet.backends import MailjetBackend

class EmailBackend(ConsoleBackend):
    def write_message(self, message):
        super().write_message(message)
        self.stream.write('Mailjet fields\n')
        self.stream.write("".join("{}: {}\n".format(t, getattr(message, t))
                                  for t in MailjetBackend.mailjet_attrs
                                  if hasattr(message, t)))
