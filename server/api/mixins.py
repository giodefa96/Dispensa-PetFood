from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    """
    Mixin to add staff editor permissions to a view.
    """
    permission_classes = [permissions.IsAdminUser,
                          IsStaffEditorPermission]