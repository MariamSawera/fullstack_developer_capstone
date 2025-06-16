"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import TemplateView
# from django.conf.urls.static import static
# from django.conf import settings
# from django.http import JsonResponse

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('contact/', TemplateView.as_view(template_name="Contact.html")),
#     path('about/', TemplateView.as_view(template_name="About.html")),
#     path('djangoapp/', include('djangoapp.urls')),
#     path('login/', TemplateView.as_view(template_name="index.html")),
#     path('', TemplateView.as_view(template_name="Home.html")),
#     path('register/', TemplateView.as_view(template_name="index.html")),
#     path('dealers/', TemplateView.as_view(template_name="index.html")),
#     path('dealer/<int:dealer_id>/',               TemplateView.as_view(template_name="index.html")),   # single dealer
#     path('dealer/<int:dealer_id>',TemplateView.as_view(template_name="index.html")),

# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import TemplateView
# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("djangoapp/", include("djangoapp.urls")),
#     path("", TemplateView.as_view(template_name="Home.html")),
#     path("about/", TemplateView.as_view(template_name="About.html")),
#     path("contact/", TemplateView.as_view(template_name="Contact.html")),
#     path("login/", TemplateView.as_view(template_name="index.html")),
#     path("register/", TemplateView.as_view(template_name="index.html")),
#     path("dealers/", TemplateView.as_view(template_name="index.html")),
#     path(
#         "dealer/<int:dealer_id>",
#         TemplateView.as_view(template_name="index.html"),
#     ),
#     path(
#         "manifest.json",
#         TemplateView.as_view(
#             template_name="manifest.json", content_type="application/json"
#         ),
#         name="manifest.json",
#     ),
#     path(
#         "postreview/<int:dealer_id>/",
#         TemplateView.as_view(template_name="index.html"),
#     ),
#     path("dealer/<int:dealer_id>/", TemplateView.as_view(template_name="index.html")),

# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.contrib import admin
from django.urls import path, include, re_path          # ← added re_path
from django.views.generic import TemplateView
from django.views.static import serve                  # ← added serve
from django.conf.urls.static import static
from django.conf import settings
import os                                              # ← added os

urlpatterns = [
    path("admin/", admin.site.urls),
    path("djangoapp/", include("djangoapp.urls")),
    path("",        TemplateView.as_view(template_name="Home.html")),
    path("about/",  TemplateView.as_view(template_name="About.html")),
    path("contact/",TemplateView.as_view(template_name="Contact.html")),
    path("login/",  TemplateView.as_view(template_name="index.html")),
    path("register/",TemplateView.as_view(template_name="index.html")),
    path("dealers/",TemplateView.as_view(template_name="index.html")),
    path("dealer/<int:dealer_id>/",
         TemplateView.as_view(template_name="index.html")),  # single dealer
    path("manifest.json",
         TemplateView.as_view(template_name="manifest.json",
                              content_type="application/json"),
         name="manifest.json"),
    path("postreview/<int:dealer_id>/",
         TemplateView.as_view(template_name="index.html")),
] + static(settings.            STATIC_URL, document_root=settings.STATIC_ROOT)

# ── serve the React‑build icons that sit at the site root ────────────
spa_static_root = os.path.join(settings.BASE_DIR, 'frontend', 'build')

urlpatterns += [
    re_path(r'^logo192\.png$', serve,
            {'document_root': spa_static_root, 'path': 'logo192.png'}),
    re_path(r'^logo512\.png$', serve,
            {'document_root': spa_static_root, 'path': 'logo512.png'}),
    re_path(r'^favicon\.ico$', serve,
            {'document_root': spa_static_root, 'path': 'favicon.ico'}),
]


