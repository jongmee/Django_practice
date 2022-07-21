from django import forms
from .models import Review


class menuReservationForm(forms.Form):
    date = forms.IntegerField()
    time = forms.IntegerField()


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "리뷰를 입력해주세요",
            'rows': 10,
        }
