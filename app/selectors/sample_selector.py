from app.models.samples import Sample,SampleRequest

def get_samples():
    return SampleRequest.objects.all()

def get_sample(sample_id):
    return Sample.objects.get(pk=sample_id)