from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm

	list_display = ('email', 'username', 'first_name', 'last_name', 'admin')
	list_filter = ('admin',)
	fieldsets = (
		(None, {'fields': ('email', 'username', 'password', 'active')}),
		('Personal info', {'fields': ('first_name', 'last_name')}),
		('Permissions', {'fields': ('staff', 'admin',)}),
	)

	# add_fieldsets to override by UserAdmin
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'username', 'password1', 'password2')}
		),
	)
	search_fields = ('email', 'last_name', 'first_name',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(User, UserAdmin)

# Remove group model from admin
admin.site.unregister(Group)
