distance_mi = 3
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = False

if distance_mi:
    if distance_mi <= 1:
        if is_raining:
            print("False")
        else:
            print("True")
    elif distance_mi > 1 and distance_mi <= 6:
        if has_bike and is_raining == False:
            print("True")
        else:
            print("False")
    else:
        if has_car or has_ride_share_app:
            print("True")
        else:
            print("False")
else:
    print("False")