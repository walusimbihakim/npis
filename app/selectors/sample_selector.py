from app.models.samples import Sample,SampleRequest

def get_sample_requests():
    return SampleRequest.objects.all()

def get_sample_request(request_id):
    return SampleRequest.objects.get(pk=request_id)

def get_samples_on_request(sample_request):
    return Sample.objects.filter(sample_request=sample_request)

def generate_auto_number():
    request_count = SampleRequest.objects.all().count()
    
    return f"{(request_count+1):04}"