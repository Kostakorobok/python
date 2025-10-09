from users import Admin
from users import Privileges
from users import admin_privileges

admin1 = Admin("Costa", "Mathew", 34, "male")
admin1_privileges = Privileges(admin_privileges)
admin1.describe_privileges(admin1.first_name, admin_privileges)
