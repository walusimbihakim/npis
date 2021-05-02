from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template


from app.utils import render_to_pdf


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('quality_assurance/sample_request_details.html')
        # data = {
        #     'today': datetime.date.today(),
        #     'amount': 39.99,
        #     'customer_name': 'Cooper Mann',
        #     'order_id': 1233434,
        # }
        # pdf = render_to_pdf('pdf/invoice.html', data)
        # return HttpResponse(pdf, content_type='application/pdf')
        html = template.render({""})
        return template.render
