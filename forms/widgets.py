from django.utils.safestring import mark_safe
from django import forms

class SliderInput(forms.Select):
    """
    A slider widget to include in your form
    """ 

    # TODO(davidc): wtf is choices for if i use self.choices?
    def render(self, name, value, attrs={}, choices=()):
        attributes = attrs
        attributes['min'] = 0
        attributes['max'] = len(self.choices) - 1
        attributes['step'] = 1
        # TODO(jayen): replace this and the super.render with a regular label 
        # and use '<div%s class="slider-value">' % 
        # flatatt(self.build_attrs(attrs, name=name))
        attributes['style'] = 'display:none'

        #TODO(davidc): clean up dodgy hack
        values = []
        values_text = []
        #value_index = 0
        for i in range(0, len(self.choices)):
            values.append(self.choices[i][0])
            values_text.append(self.choices[i][1])
            #if self.choices[i][0] == value:
            #    value_index = i
        value_index = values.index(value)

        res = super(SliderInput, self).render(name, value, attrs = attributes)
        res += '<div class="slider-wrapper">'
        res += '<div id="%s_slider_value" class="slider-value" style="display:none;">%d</div>' % (name, value_index)
        res += '<div id="%s_slider_value_text" class="slider-value-text">%s</div>' % (name, values_text[value_index])
        res += '<div id="%s_slider_values" style="display:none;">%s</div>' % (name, ','.join(values))
        res += '<div id="%s_slider_value_texts" style="display:none;">%s</div>' % (name, ','.join(values_text))
        res += '<div id="%s_slider" class="slider"></div>' % name
        res += '</div>'
        return mark_safe(res)

    class Media:
        css = {'screen':('/media/css/widgets/slider.css',)}
        js = ('/media/js/widgets/slider.js',)
