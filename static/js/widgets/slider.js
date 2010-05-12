function slider_behavior() {
    $('.slider').each(function (index) {
        var input_id = '#id_' + this.id.replace('_slider', '');
        var slider_slider = '#' + this.id;
        var slider_val = '#' + this.id + '_value';
        var slider_val_text = '#' + this.id + '_value_text';
        var slider_vals = '#' + this.id + '_values';
        var slider_val_texts = '#' + this.id + '_value_texts';
        var red = 255 - $(slider_val).html() * 255 / $(input_id).attr('max');
        var green = 255;
        var blue = red;
        var rgb = (red << 16) + (green << 8) + blue;
        var color = rgb.toString(16);
        while(color.length < 6)
          color = '0' + color;
        color = '#' + color;
        $(slider_slider).css('background', color);
        //$(slider_val_text).css('color', color);
        $('#'+this.id).slider({
            max:+$(input_id).attr('max'),
            min:+$(input_id).attr('min'),
            step:+$(input_id).attr('step'),
            value:+$(slider_val).html(),
            slide: function(event, ui) {
                $(input_id).val($(slider_vals).html().split(',')[ui.value]);
                $(slider_val).html(ui.value);
                $(slider_val_text).html($(slider_val_texts).html().split(',')[ui.value]);
                var red = 255 - ui.value * 255 / $(input_id).attr('max');
                var green = 255;
                var blue = red;
                var rgb = (red << 16) + (green << 8) + blue;
                var color = rgb.toString(16);
                while(color.length < 6)
                  color = '0' + color;
                color = '#' + color;
                $(slider_slider).css('background', color);
                //$(slider_val_text).css('color', color);
            }
        })
    }); 
}       

add_behavior(slider_behavior);
