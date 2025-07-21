from django.db import models
from django.utils import timezone


# Create your models here.


class WheelSpecification(models.Model):
    # Example fields
    condemning_dia = models.CharField(max_length=100, blank=True, null=True)
    tread_diameter = models.CharField(max_length=100, blank=True, null=True)
    wheel_gauge = models.CharField(max_length=100, blank=True, null=True)
    last_shop_issue = models.CharField(max_length=100, blank=True, null=True)
    # Add other fields similarly
    axle_box_housing_bore_dia = models.CharField(max_length=100, blank=True, null=True)
    wheel_disc_width = models.CharField(max_length=100, blank=True, null=True)
    intermediate_wwp = models.CharField(max_length=100, blank=True, null=True)
    bearing_seat_diameter = models.CharField(max_length=100, blank=True, null=True)
    roller_bearing_outer_dia = models.CharField(max_length=100, blank=True, null=True)
    roller_bearing_bore_dia = models.CharField(max_length=100, blank=True, null=True)
    roller_bearing_width = models.CharField(max_length=100, blank=True, null=True)


class BogieChecksheet(models.Model):
    # Section: Bogie Details
    bogie_no = models.CharField(max_length=100, null=True, blank=True)
    maker_year_built = models.CharField(max_length=100, null=True, blank=True)
    incoming_div_date = models.DateField(null=True, blank=True)
    deficit_components = models.TextField(blank=True)
    date_of_ioh = models.DateField(null=True, blank=True)

    # Section: Bogie Checksheet
    bogie_frame_condition = models.CharField(max_length=100, null=True, blank=True)
    bolster = models.CharField(max_length=100, null=True, blank=True)
    bolster_suspension_bracket = models.CharField(max_length=100, null=True, blank=True)
    lower_spring_seat = models.CharField(max_length=100, null=True, blank=True)
    axle_guide = models.CharField(max_length=100, null=True, blank=True)
    axle_guide_assembly = models.CharField(max_length=100, null=True, blank=True)
    protective_tubes = models.CharField(max_length=100, null=True, blank=True)
    anchor_links = models.CharField(max_length=100, null=True, blank=True)
    side_bearer = models.CharField(max_length=100, null=True, blank=True)

    # Section: BMBC Checksheet
    cylinder_body_dome_cover = models.CharField(max_length=100, null=True, blank=True)
    piston_trunnion_body = models.CharField(max_length=100, null=True, blank=True)
    adjusting_tube_screw = models.CharField(max_length=100, null=True, blank=True)
    plunger_spring = models.CharField(max_length=100, null=True, blank=True)
    tee_bolt_hex_nut = models.CharField(max_length=100, null=True, blank=True)
    pawl_pawl_spring = models.CharField(max_length=100, null=True, blank=True)
    dust_excluder = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"BogieChecksheet #{self.id} - Bogie No: {self.bogie_no}"
