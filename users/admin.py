from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogifyUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

class BlogifyUserCreationForm(UserCreationForm):

    """
    inheriting  UserCreationForm which is required for admin
    to work with custom user model 
    """

    class Meta:
        model = BlogifyUser
        fields = ('email',)

class BlogifyUserChangeForm(UserChangeForm):

    """
    inheriting  UserChangeForm which is required for admin
    to work with custom user model 
    """
    class Meta:
        model = BlogifyUser
        fields = ('email',)


class BlogifyUserAdmin(UserAdmin):

    """
    inheriting UserAdmin class to override required fields
    for custom user model
    """

    form = BlogifyUserChangeForm
    add_form = BlogifyUserCreationForm
    model = BlogifyUser
    list_display = ('email','first_name','last_name',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','profile_pic','bio')}),
        (_('Permissions'), {
            'fields': ('is_active','is_staff', 'is_superuser','groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    ordering = ('email',)

admin.site.register(BlogifyUser,BlogifyUserAdmin)