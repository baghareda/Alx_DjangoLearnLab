from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name != 'relationship_app':
        return

    groups_permissions = {
        'Admin': ['add_book', 'change_book', 'delete_book', 'view_book'],
        'Librarian': ['add_book', 'change_book', 'view_book'],
        'Member': ['view_book'],
    }

    Book = apps.get_model('relationship_app', 'Book')

    for group_name, perm_codes in groups_permissions.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        for code in perm_codes:
            perm = Permission.objects.filter(codename=code, content_type__model='book').first()
            if perm:
                group.permissions.add(perm)
            else:
                # Optional: Log missing permission to debug if needed
                print(f"Warning: Permission with codename '{code}' for model 'book' not found.")
