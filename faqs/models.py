from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

# Model for FAQs
from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField(blank=True, null=True)  # Allow blank content


    answer = RichTextField(verbose_name=_("Answer"))
    question_hi = models.TextField(null=True, blank=True, verbose_name=_("Question in Hindi"))
    question_bn = models.TextField(null=True, blank=True, verbose_name=_("Question in Bengali"))
    answer_hi = RichTextField(null=True, blank=True, verbose_name=_("Answer in Hindi"))
    answer_bn = RichTextField(null=True, blank=True, verbose_name=_("Answer in Bengali"))

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_text(self, lang='en'):
        cache_key = f'faq_{self.id}_{lang}'
        data = cache.get(cache_key)
        if not data:
            if lang == 'hi':
                data = {'question': self.question_hi, 'answer': self.answer_hi}
            elif lang == 'bn':
                data = {'question': self.question_bn, 'answer': self.answer_bn}
            else:
                data = {'question': self.question, 'answer': self.answer}
            cache.set(cache_key, data, timeout=3600)
        return data

    def __str__(self):
        return self.question
