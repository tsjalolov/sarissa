from rest_framework.permissions import BasePermission



class MyPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user.has_perm,'jjjjjjjjjjjj')
        if request.user.has_perm("fuqaro.my_group"):
            print('noo')
            return True
        return True