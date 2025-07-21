from django.shortcuts import render
from django.http import JsonResponse
from .models import WheelSpecification, BogieChecksheet
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from django.utils.timezone import now
# Create your views here.


@csrf_exempt
def submit_wheel_specification(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received wheel data:", data)

            spec = WheelSpecification.objects.create(
                tread_diameter=data.get("tread_diameter", ""),
                last_shop_issue=data.get("last_shop_issue", ""),
                condemning_dia=data.get("condemning_dia", ""),
                wheel_gauge=data.get("wheel_gauge", ""),
                axle_box_housing_bore_dia=data.get('axle_box_housing_bore_dia', ''),
                wheel_disc_width=data.get('wheel_disc_width', ''),
                intermediate_wwp = data.get("intermediate_wwp", ''),
                bearing_seat_diameter = data.get("bearing_seat_diameter", ''),
                roller_bearing_outer_dia = data.get("roller_bearing_outer_dia", ''),
                roller_bearing_bore_dia = data.get("roller_bearing_bore_dia", ''),
                roller_bearing_width = data.get("roller_bearing_width", ''),
            )

            return JsonResponse({
                "success": True,
                "message": "Wheel specification submitted successfully",
                "data": {
                    "id": spec.id,
                    "submitted_at": str(now())
                }
            }, status=201)

        except Exception as e:
            print("Error while saving wheel specification:", str(e))  # Add this for debug
            return JsonResponse({"error": str(e)}, status=400)


    return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def get_wheel_specifications(request):
    if request.method == 'GET':
        try:
            specs = WheelSpecification.objects.all()
            data = [
                {
                    "id": spec.id,
                    "tread_diameter": spec.tread_diameter,
                    "last_shop_issue": spec.last_shop_issue,
                    "condemning_dia": spec.condemning_dia,
                    "wheel_gauge": spec.wheel_gauge,
                    "axle_box_housing_bore_dia": spec.axle_box_housing_bore_dia,
                    "wheel_disc_width": spec.wheel_disc_width,
                    "intermediate_wwp": spec.intermediate_wwp,
                    "bearing_seat_diameter": spec.bearing_seat_diameter,
                    "roller_bearing_outer_dia": spec.roller_bearing_outer_dia,
                    "roller_bearing_bore_dia": spec.roller_bearing_bore_dia,
                    "roller_bearing_width": spec.roller_bearing_width,
                }
                for spec in specs
            ]
            return JsonResponse({"success": True, "data": data}, status=200)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def submit_bogie_checksheet(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)

            def parse_incoming_date(date_str):
                if date_str:
                    # Extract date part before 'T' if present
                    date_only = date_str.split('T')[0]
                    return parse_date(date_only)
                return None

            checksheet = BogieChecksheet.objects.create(
                bogie_no = data.get("bogie_no", "Not Available"),
                maker_year_built = data.get("maker_year_built", "Not Available"),
                incoming_div_date = parse_incoming_date(data.get("incoming_div_date")),
                deficit_components = data.get("deficit_components", ""),
                date_of_ioh = parse_incoming_date(data.get("date_of_ioh")),

                bogie_frame_condition = data.get("bogie_frame_condition", "Not Available"),
                bolster = data.get("bolster", "Not Available"),
                bolster_suspension_bracket = data.get("bolster_suspension_bracket", "Not Available"),
                lower_spring_seat = data.get("lower_spring_seat", "Not Available"),
                axle_guide = data.get("axle_guide", "Not Available"),
                axle_guide_assembly = data.get("axle_guide_assembly", "Not Available"),
                protective_tubes = data.get("protective_tubes", "Not Available"),
                anchor_links = data.get("anchor_links", "Not Available"),
                side_bearer = data.get("side_bearer", "Not Available"),

                cylinder_body_dome_cover = data.get("cylinder_body_dome_cover", "Not Available"),
                piston_trunnion_body = data.get("piston_trunnion_body", "Not Available"),
                adjusting_tube_screw = data.get("adjusting_tube_screw", "Not Available"),
                plunger_spring = data.get("plunger_spring", "Not Available"),
                tee_bolt_hex_nut = data.get("tee_bolt_hex_nut", "Not Available"),
                pawl_pawl_spring = data.get("pawl_pawl_spring", "Not Available"),
                dust_excluder = data.get("dust_excluder", "Not Available")
            )

            return JsonResponse({
                "success": True,
                "message": "Checksheet submitted successfully",
                "data": {
                    "id": checksheet.id,
                    "bogie_no": checksheet.bogie_no,
                    "submitted_at": str(checksheet.created_at)
                }
            }, status=201)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid method"}, status=405)