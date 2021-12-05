from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('Clients', {'fields': ('email', 'subject')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class TaskUserAssociate(admin.ModelAdmin):
    list_display = ['subject', 'academic_level', 'pages',
                    'word_count', 'price',
                    ]
    list_filter = ('subject', 'start_date', 'client',)
    fieldsets = (
        ('TASK_DETAILS', {"fields": (
            'subject',  'academic_level', 'pages',
            'word_count', 'price',
        )}),
        ('EXTRA_DETAILS', {'fields': (
            'additional_files',
            'images'
        )})
    )
    search_fields = ('subjects', 'academic_level', 'word_count')
    ordering = ['-start_date']
    

admin.site.register(Task, TaskUserAssociate)
admin.site.register(CustomUser, CustomUserAdmin)
