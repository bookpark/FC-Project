from django.conf.urls import url

from accounts import views

urlpatterns = [
    # Auth
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
    # url(r'^(?P<pk>\d+)/change-password/$', views.ChangePasswordView.as_view(), name='change-password'),

    # Activate
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z_\-]+)/$', views.activate, name='activate'),
    # url(r'^withdraw/$', views.WithdrawView.as_view(), name='widthraw'),

    # Profile
    # url(r'^(?P<pk>\d+)/profile/$', views.UpdateProfileView.as_view(), name='profile'),
    # url(r'^(?P<pk>\d+)/owner-profile/$', views.OwnerProfileView.as_view(), name='owner-profile'),
    # url(r'^(?P<pk>\d+)/preference/$', views.PreferenceUpdate.as_view(), name='preference')
    # url(r'(?P<user_pk>\d+)/my-reservation/$' ),

    # Facebook
    # url(r'^facebook-login/$', views.FacebookLoginView.as_view(), name='fb-login')
]
