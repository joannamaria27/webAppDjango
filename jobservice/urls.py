from django.urls import path
from . import views
from companyusers.views import (OfferListView, OfferCreateView, OfferDetailView,OfferUpdateView)

urlpatterns = [
    path('', OfferListView.as_view(), name='jobs-home'),
    path('about/', views.about, name='about-job'),
    #path('start/', views.start, name='start'),
    path('profilecompany/', views.profilecompany, name='profilecompany'),
    path('profileuser/', views.profileuser, name='profileuser'),
    path('createcv/', views.createcv, name='createcv'),
    #path('createoffer/', views.createoffer, name='createoffer'),
    path('offer/<int:pk>/', OfferDetailView.as_view(), name='offer-details'),
    path('offer/new/', OfferCreateView.as_view(), name='offer-create'),
    path('offer/<int:pk>/update', OfferUpdateView.as_view(), name='offer-update'),
    path('cv/<int:cv_id>/', views.cv, name='cv'),
    path('company/<int:company_id>/', views.companyview, name='companyview'),
    # path('person/<int:person_id>/', views.personview, name='personview'),
]
 