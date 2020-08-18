from django.conf.urls import url

from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

app_name = "benchmarking"

urlpatterns = [
    path("", TemplateView.as_view(template_name="404.html"),),
    # Applications
    path("M59", TemplateView.as_view(template_name="benchmarking/app-x1-1-M59/benchmarking-home.html"),
         name="benchmark-home-x1-1"),
    path("X82", TemplateView.as_view(template_name="benchmarking/app-x1-2-X82/benchmarking-home.html"),
         name="benchmark-home-x1-2"),
    path("T84", TemplateView.as_view(template_name="benchmarking/app-x2-1-T84/benchmarking-home.html"),
         name="benchmark-home-x2-1"),
    path("Q69", TemplateView.as_view(template_name="benchmarking/app-x2-2-Q69/benchmarking-home.html"),
         name="benchmark-home-x2-2"),
    # Download input file page
    path("input-file", TemplateView.as_view(template_name="benchmarking/input-file.html"),
         name="input-file"),
    # Introduction to MPC video
    path("introduction-to-mpc", TemplateView.as_view(template_name="benchmarking/app-x1-1-M59/mpc-introduction.html"),
         name="mpc-introduction"),
    # Assume pages-1
    path("assume-sfErgdfXr",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-1/assume-page-source-code.html"),
         name="assume-page-source-1"),
    path("assume-rwXCVEezQ",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-1/assume-page-function.html"),
         name="assume-page-function-1"),
    path("assume-dfXVDwfES",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-1/assume-page-download-template.html"),
         name="assume-page-download-template-file-1"),
    path("assume-introduction-video-gfjHSerSt",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-1/assume-introduction-video.html"),
         name="assume-introduction-video-1"),
    path("assume-page-guidelines-BdrAfyufQ",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-1/assume-page-guidelines.html"),
         name="assume-page-guidelines-1"),
    # Assume pages-2
    path("assume-BfGFRGfXr",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-2/assume-page-source-code.html"),
         name="assume-page-source-2"),
    path("assume-EgTTGgezQ",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-2/assume-page-function.html"),
         name="assume-page-function-2"),
    path("assume-DWGRGfES",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-2/assume-page-download-template.html"),
         name="assume-page-download-template-file-2"),
    path("assume-introduction-video-CEGFgrgr",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-2/assume-introduction-video.html"),
         name="assume-introduction-video-2"),
    path("assume-page-guidelines-CGHrwegVt",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-1-2/assume-page-guidelines.html"),
         name="assume-page-guidelines-2"),
    # Assume pages-3
    path("assume-RtyxvTHtd",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-2-1/assume-page-function.html"),
         name="assume-page-function-3"),
    path("assume-OPTRvdfd",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-2-1/assume-page-download-template.html"),
         name="assume-page-download-template-file-3"),
    path("assume-page-guidelines-LFgrtedhji",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-2-1/assume-page-guidelines.html"),
         name="assume-page-guidelines-3"),
    # Assume pages-4
    path("assume-CBbtrgRRg",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-2-2/assume-page-function.html"),
         name="assume-page-function-4"),
    path("assume-ZXgdfsDGF",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-2-2/assume-page-download-template.html"),
         name="assume-page-download-template-file-4"),
    path("assume-page-guidelines-VRrhusdAS",
         TemplateView.as_view(template_name="benchmarking/assume-pages/gr-2-2/assume-page-guidelines.html"),
         name="assume-page-guidelines-4"),
    # End of demo pages
    path("M59/end-of-demo", TemplateView.as_view(template_name="benchmarking/app-x1-1-M59/end-of-demo.html"),
         name="endofdemo-x1-1"),
    path("X82/end-of-demo", TemplateView.as_view(template_name="benchmarking/app-x1-2-X82/end-of-demo.html"),
         name="endofdemo-x1-2"),
    path("T84/end-of-demo", TemplateView.as_view(template_name="benchmarking/app-x2-1-T84/end-of-demo.html"),
         name="endofdemo-x2-1"),
    path("Q69/end-of-demo", TemplateView.as_view(template_name="benchmarking/app-x2-2-Q69/end-of-demo.html"),
         name="endofdemo-x2-2"),
]
