from django.db import models
from django.urls import reverse
from app.models.company import Company


class Field_enforcement(models.Model):
    
    id = models.AutoField(primary_key=True)
    status = [
        ('Yes', 'Yes'),
        ('No', 'No')
        

    ]
    serial_number = models.CharField(max_length=200)
    date = models.DateField(default='2021-05-12')
    company_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    seal_number_placed_on_nozzle = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200,unique=True)
    contact = models.CharField(max_length= 200)
    truck_number = models.CharField(max_length=200,null=True,blank=True)
    subcounty = models.CharField(
        verbose_name="Subcounty/Divison/Municipality", max_length=200)
    seal_placed_on = models.CharField(verbose_name="Seal Number(s) placed on underground tanks ",
     max_length=200, null=True, blank=True)
    illegal_operation = models.CharField(
        verbose_name="Continuous illegal operation of petroleum facility", max_length=200, choices=status,default="Yes")
    illegal_construction = models.CharField(
        verbose_name="Continuous illegal construction of petroleum facility", max_length=200, choices=status, default="Yes")
    Adulteraon_fuel = models.CharField(
        verbose_name="Adulteraon of fuel", max_length=200, choices=status, default="Yes")
    continuous_operation = models.CharField(
        verbose_name="Continuous operation without carrying out annual EIA audit", max_length=200, choices=status, default="Yes")
    illegal_operation_business = models.CharField(
        verbose_name="Continuous illegal operation and construction in front of congested business premises ",
        max_length=200, choices=status, default="Yes")
    illegal_operation_power_line = models.CharField(
        verbose_name="Continuous illegal operation and construction under high voltage power transmission line  ",
        max_length=200, choices=status, default="Yes")
    illegal_operation_dangerous_corner = models.CharField(
        verbose_name="Continuous illegal operation and construction in a dangerous corner  ",
        max_length=200, choices=status, default="Yes")
    illegal_operation_reserve_area = models.CharField(
        verbose_name="Continuous illegal operation and construction in a road reserve area  ",
        max_length=200, choices=status, default="Yes")
    illegal_operation_bypassing_seals = models.CharField(
        verbose_name="Continuous illegal operation aer breaking and/ or bypassing seals  ",
        max_length=200, choices=status, default="Yes")
    already = models.CharField(
        verbose_name="Already has knowledge of requirement to obtain POL & PCP  ",
        max_length=200, choices=status, default="Yes")
    facility_standards = models.CharField(
        verbose_name="Continuous illegal operation and construction which does not meet petroleum facility standards  ",
        max_length=200, choices=status, default="Yes")
    Social_aspects = models.CharField(
        verbose_name="Social aspects involving facility ",
        max_length=200, choices=status, default="Yes")
    facility_operator = models.CharField(
        verbose_name="Misrepresentaon of branding by facility operator ",
        max_length=200, choices=status, default="Yes")
    Impersonaon = models.CharField(
        verbose_name="Impersonaon by using another's license / permit  ",
        max_length=200, choices=status, default="Yes")
    displaying_license = models.CharField(
        verbose_name="Continuous illegal operation and /or construction without displaying license /permit from MEMD  ",
        max_length=200, choices=status, default="Yes")
    uganda_police = models.CharField(
        verbose_name="Continuous illegal operation aer having been reported to uganda police  ",
        max_length=200, choices=status, default="Yes")
    land_plot_size = models.CharField(
        verbose_name="Continuous illegal operation and construction on inadequate land plot size (show size )",
        max_length=200, choices=status, default="Yes")
    under_reference = models.CharField(
        verbose_name="Continuous illegal operation and / or construction reported to uganda police under reference",
        max_length=200, choices=status, default="Yes")
    inadequate_size_land = models.CharField(
        verbose_name="Continuous illegal operation and / or construction using a POL and PCP respecvely on an inadequate size of land",
        max_length=200, choices=status, default="Yes")
    others = models.CharField(max_length=200, choices=status, default="Yes")
    remarks = models.TextField(max_length=200)
    name_of_inspector = models.CharField(max_length=200)
    Name_Dealer = models.CharField(
        verbose_name="Name of Dealer / Representave",
        max_length=200)
    
    def __str__(self):
        return self.company_name
    

# class Inspection(models.Model):
    
#     part1 = models.CharField(
#         verbose_name="Possession of certificate of approval of Environment Impact Assessment Certificate", max_length=200)
#     part2 = models.CharField(
#         verbose_name="Possession of a well-designed interceptor on site to control water pollution from accidental spills that could be washed off by storm", max_length=200)
#     part3 = models.CharField(
#         verbose_name="Possession of a standby generator", max_length=200)
#     part4 = models.CharField(
#         verbose_name="Possession of a standby generator", max_length=200)
#     part5 = models.CharField(
#         verbose_name="Possession of a standby generator", max_length=200)
#     part6 = models.CharField(
#         verbose_name="Illuminated retro reflective Sign Post Visible from a distance of at least 50m", max_length=200)
#     part7 = models.CharField(
#         verbose_name="Emergency Telephone contact Displayed", max_length=200)
#     part8 = models.CharField(
#         verbose_name="Proximity to household and High Voltage Supply", max_length=200)
#     part9 = models.CharField(
#         verbose_name="Identify use of inflammable material and any other source of fire on facility", max_length=200)
#     part10 = models.CharField(
#         verbose_name="Identify use of inflammable material and any other source of fire on facility", max_length=200)
#     part11 = models.CharField(
#         verbose_name="Fire Assembly Point Clearly Labeled", max_length=200)
#     part13 = models.CharField(
#         verbose_name="At least one well-maintained 9-Kg Powder fire extinguisher per Pump Island", max_length=200)
#     part14 = models.CharField(
#         verbose_name="Availability of Sand Buckets to handle spilage accidents", max_length=200)
#     part15 = models.CharField(
#         verbose_name="Is Safety training conducted for employees", max_length=200)
#     part16 = models.CharField(
#         verbose_name="Availability of Safety Signs (No smoking,Switch off engine,switch-off Mobile Phone)", max_length=200)
#     part17 = models.CharField(
#         verbose_name="Availability of well-stocked first aid box in accordance to the factory act", max_length=200)
#     part18 = models.CharField(
#         verbose_name="Is there a pump in road reserve", max_length=200)
#     part19 = models.CharField(
#         verbose_name="Well-Constructed Perimeter Fence (at least 1.8 meters)", max_length=200)
#     part20 = models.CharField(
#         verbose_name="Well-Maintained Office Block", max_length=200)
#     part21 = models.CharField(
#         verbose_name="Status of Canopy", max_length=200)
#     part22 = models.CharField(
#         verbose_name="Status of Forecourt", max_length=200)
#     part23 = models.CharField(
#         verbose_name="Status of Power", max_length=200)
#     part24 = models.CharField(
#         verbose_name="Adequate Lighting", max_length=200)
#     part25 = models.CharField(
#         verbose_name="Status of Electrical Installations", max_length=200)
#     part26 = models.CharField(
#         verbose_name="Availability of standard product off loading Point", max_length=200)
#     part27 = models.CharField(
#         verbose_name="Status of over-all layout and type(s) of storage tanks", max_length=200)
#     part28 = models.CharField(
#         verbose_name="Availability of leak detection method on Any tank above 30.000m", max_length=200)
#     part29 = models.CharField(
#         verbose_name="Vapour venting from storage tanks (3m high)", max_length=200)
#     part30 = models.CharField(
#         verbose_name="Schedule and procedure for inspection and cleaning of vent wire gauze", max_length=200)
#     part31 = models.CharField(
#         verbose_name="Tanks should be clearly marked on top with the capacity written and each tank with its own calibrated dipstick", max_length=200)
#     part34 = models.CharField(
#         verbose_name="Are there a lot of spillage around the pump area", max_length=200)
#     part35 = models.CharField(
#         verbose_name="Inspection requirements for compressors in accordance with the factory act", max_length=200)
#     part36 = models.CharField(
#         verbose_name="Inspection requirements for compressors in accordance with the factory act", max_length=200)
#     part37 = models.CharField(
#         verbose_name="Mechanism of waste product disposal", max_length=200)
#     part38 = models.CharField(
#         verbose_name="Proper Drainage system for surface and foul water", max_length=200)
#     part39 = models.CharField(
#         verbose_name="Status of sanitation facilities for staff and customers", max_length=200)
#     part40 = models.CharField(
#         verbose_name="Standard of cleanliness within the petrol filling or service station", max_length=200)
#     part41 = models.CharField(
#         verbose_name="Parking space. One car parking space per 4m3 floor space of the store shop", max_length=200)
#     part42 = models.CharField(
#         verbose_name="Price display Board with correct information", max_length=200)
#     part43 = models.CharField(
#         verbose_name="Is Information required by the NPIS availed regularly and reconcile with the information with the Ministry", max_length=200)
#     id = models.AutoField(primary_key=True)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     date = models.DateField()
#     checklist_No = models.CharField(max_length=200)
#     partcular = models.TextField()
#     status = models.BooleanField(default=True)
#     remarks = models.TextField(null=True)
#     other_details = models.TextField(null=True)
#     waste = models.CharField(
#         verbose_name="Procedure for Handling Conterminated Wastes and Product", max_length=200)

#     def __str__(self):
#         return self.company
   
#     assessment_certificate = models.CharField(max_length=200)
    



    
        


