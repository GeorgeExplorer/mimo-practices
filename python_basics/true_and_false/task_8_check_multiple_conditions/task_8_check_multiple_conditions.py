is_admin = False
is_verified = True

access_availability = "granted" if is_admin or is_verified else "denied"
print(f"Access {access_availability}")
