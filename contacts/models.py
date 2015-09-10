from django.db import models

""" Basic address book tables """


TITLE_CHOICES = (
    # common
    (None, 'None'),
    ('Mr.', 'Mr'), ('Miss', 'Miss'), ('Ms.', 'Ms'), ('Mrs.', 'Mrs'),
    # less common
    ('Dr.', 'Dr'), ('Prof.', 'Prof'), ('Rev.', 'Rev'),
    # military
    ('Lt.', 'Lt'), ('Cpt.', 'Cpt'), ('Maj.', 'Maj'), ('Gen.', 'Gen'),
    # rare
    ('Esq', 'Esq'), ('Sr.', 'Sr'), ('Jr.', 'Jr'), ('Hon.', 'Hon'), ('Rt. Hon.', 'Rt Hon')
)


class Contact(models.Model):
    name = models.CharField(blank=False, max_length=254)
    nick = models.CharField(blank=True, null=True, max_length=64)
    company = models.BooleanField(default=False)
    title = models.CharField(blank=True, null=True, max_length=16, choices=TITLE_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Country(models.Model):
    abbrev = models.CharField(max_length=5)
    name = models.CharField(max_length=64)

    def __str__(self):
        return "%s (%s)" % (self.abbrev, self.name)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'countries'


class State(models.Model):
    country = models.ForeignKey(Country)
    name = models.CharField(max_length=64)
    abbrev = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Locality(models.Model):
    state = models.ForeignKey(State)
    name = models.CharField(max_length=64)
    postcode = models.CharField(max_length=8)

    def __str__(self):
        return "%s (%s)" % (self.name, self.state.abbrev)

    class Meta:
        ordering = ('name', 'state')
        verbose_name_plural = 'localities'


ADDRESS_TYPES = (
    (None, 'Unspecified'),
    ('Home', 'Home'),
    ('Work', 'Work'),
    ('Main', 'Main'),
    ('Branch', 'Branch'),
    ('Mailing', 'Mail'),
    ('Billing', 'Billing'),
    ('Legal', 'Legal'),
    ('Campus', 'Campus'),
    ('Dormitory', 'Dormitory'),
    ('Other', 'Other'),
)


class Address(models.Model):
    type = models.CharField(max_length=16, choices=ADDRESS_TYPES, null=True, blank=True)
    locality = models.ForeignKey(Locality)
    contact = models.ForeignKey(Contact, null=True)
    title = models.CharField(blank=True, null=True, max_length=254)
    address_1 = models.CharField(blank=False, max_length=1022)
    address_2 = models.CharField(blank=True, null=True, max_length=1022)

    def __str__(self):
        result = "%s %s %s %s %s %s" % (self.title, self.addres_1, self.address_2, self.locality.name,
                                        self.locality.state.name, self.locality.postcode)
        return result.replace('  ', ' ').strip()

    class Meta:
        ordering = ('title', 'address_1', 'address_2')
        verbose_name_plural = 'addresses'


EMAIL_TYPES = (
    (None, 'Unspecified'),
    ('Home', 'Home'),
    ('Work', 'Work'),
    ('Campus', 'Campus'),
    ('Dormitory', 'Dormitory'),
    ('Other', 'Other'),
)


class Email(models.Model):
    type = models.CharField(max_length=16, choices=EMAIL_TYPES, null=True, blank=True)
    contact = models.ForeignKey(Contact, null=True)
    address = models.EmailField(blank=False)

    @property
    def is_valid(self):
        return self.address and '@' in self.address

    @property
    def username(self):
        return self.address.split('@', 1)[0] if self.is_valid else ''

    @property
    def domain(self):
        return self.address.split('@', 1)[1] if self.is_valid else ''

    def __str__(self):
        return self.address


PHONE_TYPES = (
    (None, 'Unspecified'),
    ('Home', 'Home'),
    ('Work', 'Work'),
    ('Main', 'Main'),
    ('A/H', 'After Hours'),
    ('Campus', 'Campus'),
    ('Dormitory', 'Dormitory'),
    ('Other', 'Other'),
)


class PhoneNumber(models.Model):
    type = models.CharField(max_length=16, choices=PHONE_TYPES, null=True, blank=True)
    contact = models.ForeignKey(Contact, null=True)
    number = models.CharField(max_length=32)

    def __str__(self):
        return self.phone_number

