from django import forms

class PropertyForm(forms.Form):
    area = forms.FloatField(label='Area (sq. ft.)', min_value=0)
    bedrooms = forms.IntegerField(label='Number of Bedrooms', min_value=0)
    bathrooms = forms.IntegerField(label='Number of Bathrooms', min_value=0)
    city = forms.ChoiceField(label='City', choices=[
        ('Bhairahawa', 'Bhairahawa'),
        ('Bhaktapur', 'Bhaktapur'),
        ('Biratnagar', 'Biratnagar'),
        ('Butwal', 'Butwal'),
        ('Chitwan', 'Chitwan'),
        ('Dhading', 'Dhading'),
        ('Dharan', 'Dharan'),
        ('Illam', 'Illam'),
        ('Jhapa', 'Jhapa'),
        ('Kapilvastu', 'Kapilvastu'),
        ('Kaski', 'Kaski'),
        ('Kathmandu', 'Kathmandu'),
        ('Kavre', 'Kavre'),
        ('Kirtipur', 'Kirtipur'),
        ('Lalitpur', 'Lalitpur'),
        ('Mahottari', 'Mahottari'),
        ('Makwanpur', 'Makwanpur'),
        ('Morang', 'Morang'),
        ('Nawalparasi', 'Nawalparasi'),
        ('Nawalpur', 'Nawalpur'),
        ('Parsa', 'Parsa'),
        ('Pokhara', 'Pokhara'),
        ('Rupandehi', 'Rupandehi'),
        ('Surkhet', 'Surkhet'),
        ('Tanahu', 'Tanahu'),
    ])