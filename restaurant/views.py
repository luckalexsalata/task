from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models import Q
from django.conf import settings
from .serializers import *
from users.models import User, Employee


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.BasePermission]


class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RestaurantUpdateView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RestaurantDestroyView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.BasePermission]


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuUpdateView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuDestroyView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UploadMenuAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        try:
            req = request.data.dict()
            todays_date = settings.CURRENT_DATE.date()
            menu = Menu.objects.filter(
                Q(restaurant__id=int(req.get('restaurant')))
                and Q(created_at__date=todays_date))

            # if menu.exists():
            #     res = {
            #         "msg": "Menu already added.",
            #         "success": False,
            #         "data": None}
            #     return Response(data=res, status=status.HTTP_200_OK)

            serializer = UploadMenuSerializer(data=req)

            if serializer.is_valid():
                serializer.save()
                res = {
                    "msg": "Menu uploaded",
                    "success": True,
                    "data": serializer.data}
                return Response(data=res, status=status.HTTP_201_CREATED)

            res = {
                "msg": str(
                    serializer.errors),
                "success": False,
                "data": None}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            res = {"msg": str(e), "success": False, "data": None}
            return Response(data=res, status=status.HTTP_400_BAD_REQUEST)


class CurrentDayMenuList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        todays_date = settings.CURRENT_DATE.date()

        qs = Menu.objects.filter(Q(created_at__date=todays_date))
        serializer = MenuSerializer(qs, many=True)
        res = {"msg": 'success', "data": serializer.data, "success": True}
        return Response(data=res, status=status.HTTP_200_OK)


class VoteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, menu_id):
        username = request.user.username
        todays_date = settings.CURRENT_DATE.date()

        employee = User.objects.get(username=username)
        menu = Menu.objects.get(id=menu_id)
        print(menu)
        if Vote.objects.filter(
                employee=employee,
                voted_at__date=todays_date,
                menu__id=menu_id).exists():
            res = {"msg": 'You already voted!', "data": None, "success": False}
            return Response(data=res, status=status.HTTP_200_OK)
        else:
            new_vote = Vote.objects.create(
                employee=employee,
                menu=menu
            )
            menu.votes += 1
            menu.save()

            qs = Menu.objects.filter(Q(created_at__date=todays_date))
            serializer = ResultMenuListSerializer(qs, many=True)
            res = {
                "msg": 'You voted successfully!',
                "data": serializer.data,
                "success": True}
            return Response(data=res, status=status.HTTP_200_OK)


class ResultsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        todays_date = settings.CURRENT_DATE.date()
        restaurant = Restaurant.objects.get(pk=pk)
        current_menu = Menu.objects.filter(
            Q(created_at__date=todays_date), restaurant__pk=pk, votes__gt=0).order_by('-votes')
        if len(current_menu) == 0:
            res = {
                "msg": 'Results not found! no menus found for today.',
                "data": None,
                "success": False}
            return Response(data=res, status=status.HTTP_200_OK)
        queryset = current_menu[: 3] #get first tree menu
        result = [{"name": item.name, "votes": item.votes} for item in queryset]

        res = {"restaurant": restaurant.name, "data": result, "success": True}
        return Response(data=res, status=status.HTTP_200_OK)