from django.contrib import admin
from django.urls import path
from un_app.views import (
                            home,
                            plot_1,
                            plot_2,
                            plot_3,
                            plot_4,
                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
    path('plot_1/', plot_1),
    path('plot_2/', plot_2),
    path('plot_3/', plot_3),
    path('plot_4/', plot_4),
]
