from rest_framework import permissions


# カスタムパーミッション: BasePermissionクラスの has_object_permissionをオーバーライドして作成する
# @see https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user