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

from pathlib import Path
from django.views.static import serve
from django.urls import re_path
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("djangoapp/", include("djangoapp.urls")),
    path("", TemplateView.as_view(template_name="Home.html")),
    path("about/", TemplateView.as_view(template_name="About.html")),
    path("contact/", TemplateView.as_view(template_name="Contact.html")),
    path("login/", TemplateView.as_view(template_name="index.html")),
    path("register/", TemplateView.as_view(template_name="index.html")),
    path("dealers/", TemplateView.as_view(template_name="index.html")),
    path(
        "dealer/<int:dealer_id>",
        TemplateView.as_view(template_name="index.html"),
    ),
    path(
        "manifest.json",
        TemplateView.as_view(
            template_name="manifest.json", content_type="application/json"
        ),
        name="manifest.json",
    ),
    path(
        "postreview/<int:dealer_id>",
        TemplateView.as_view(template_name="index.html"),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# absolute folder that actually holds logo192.png
spa_root = Path(settings.BASE_DIR) / "frontend" / "build"


# sanity check at import‑time: print once so you see it in the console
print("Serving React root files from:", spa_root)


urlpatterns += [
    re_path(
        r"^logo192\.png$",
        serve,
        {"document_root": spa_root, "path": "logo192.png"}
    ),
    re_path(
        r"^logo512\.png$",
        serve,
        {"document_root": spa_root, "path": "logo512.png"}
    ),
    re_path(
        r"^favicon\.ico$",
        serve,
        {"document_root": spa_root, "path": "favicon.ico"}
    ),
]
