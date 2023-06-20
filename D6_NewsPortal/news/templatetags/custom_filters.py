from django import template


register = template.Library()

unacceptable_words = [
    'прохладно',
    'прогноз'
]

@register.filter()
def censor(text):
    if type(text) is not str:
        raise TypeError
    censored_text = []
    for word in text.split():
        if word in unacceptable_words:
            censored_text.append(word[0]+''.join(['*' for i in word]))
        else: censored_text.append(word)
    return ' '.join(censored_text)