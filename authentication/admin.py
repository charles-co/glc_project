from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from .models import Profile
from .forms import UserChangeForm, UserCreationForm

from django.contrib import messages
from django.contrib.admin import helpers
from django.contrib.admin.utils import model_ngettext
from django.core.exceptions import PermissionDenied
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _, gettext_lazy
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

User = get_user_model()

def delete_user(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    app_label = opts.app_label

    deletable_objects, model_count, perms_needed, protected = modeladmin.get_deleted_objects(queryset, request)

    if perms_needed == {'outstanding token', 'profile'}:
        perms_needed = set()

    if request.POST.get('post') and not protected:
        if perms_needed:
            raise PermissionDenied
        n = queryset.count()
        if n:
            for obj in queryset:
                obj.profile.delete()
                OutstandingToken.objects.filter(user=obj).delete()
                obj_display = str(obj)
                modeladmin.log_deletion(request, obj, obj_display)
            modeladmin.delete_queryset(request, queryset)
            modeladmin.message_user(request, _("Successfully deleted %(count)d %(items)s.") % {
                "count": n, "items": model_ngettext(modeladmin.opts, n)
            }, messages.SUCCESS)
        # Return None to display the change list page again.
        return None

    objects_name = model_ngettext(queryset)

    if perms_needed or protected:
        title = _("Cannot delete %(name)s") % {"name": objects_name}
    else:
        title = _("Are you sure?")

    context = {
        **modeladmin.admin_site.each_context(request),
        'title': title,
        'objects_name': str(objects_name),
        'deletable_objects': [deletable_objects],
        'model_count': dict(model_count).items(),
        'queryset': queryset,
        'perms_lacking': perms_needed,
        'protected': protected,
        'opts': opts,
        'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        'media': modeladmin.media,
    }

    request.current_app = modeladmin.admin_site.name

    # Display the confirmation page
    return TemplateResponse(request, [
        "admin/%s/%s/delete_user_confirmation.html" % (app_label, opts.model_name),
        "admin/%s/delete_user_confirmation.html" % app_label,
        "admin/delete_user_confirmation.html"
    ], context)

delete_user.allowed_permissions = ('delete',)
delete_user.short_description = gettext_lazy("Delete selected %(verbose_name_plural)s")

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    actions = [delete_user]
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name', 'is_verified', 'last_login',)
    list_display_links = ('email', 'name',)
    list_filter = ('is_staff', 'is_superuser', 'is_verified', 'is_active', 'groups')
    readonly_fields = ('date_joined', 'last_login',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal Info', {'fields': ('is_verified', 'date_joined', 'last_login',)}),
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

# admin.site.disable_action('delete_selected')
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Group)