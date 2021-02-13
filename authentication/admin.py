from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from .models import Profile
from .forms import UserChangeForm, UserCreationForm

User = get_user_model()



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name', 'is_verified', )
    list_display_links = ('email', 'name',)
    list_filter = ('is_staff', 'is_superuser', 'is_verified', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal Info', {'fields': ('is_verified',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
    def name(self, obj):
        url = reverse("admin:authentication_profile_change", args=[obj.profile.id])
        return mark_safe("<a href='{}'>{}</a>".format(url, obj.profile.full_name))

    name.short_description = 'Name'
    name.admin_order_field = 'user__profile__name'
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    # filter_horizontal = ()

class ProfileAdmin(admin.ModelAdmin):

    # change_list_template = "admin/change_list_filter_confirm_sidebar.html"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        if isinstance(obj, Profile):
            if request.path == reverse("admin:authentication_user_delete", args=[obj.user.id]):
                return True
        return False
    list_filter = ('dob',)
    list_display = ('full_name', 'email', 'dob', 'phone_number', 'is_verified')
    readonly_fields = ["user",]
    list_display_links = ('full_name', 'email')
    search_fields = ('full_name', 'user__email', 'phone_number')

    def is_verified(self, obj):
        return "Yes" if obj.user.is_verified else "No"
    is_verified.short_description = 'Verified?'
    is_verified.admin_order_field = 'user__is_verified'

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email Address'
    email.admin_order_field = 'user__email'

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Group)