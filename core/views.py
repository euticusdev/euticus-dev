from django.shortcuts import render


def home(request):
    context = {
        "brand_name": "Euticus",
        "brand_suffix": "dev",
        "tagline": "BUILD. LEARN. SHARE.",
        "headline": "BUILD YOUR",
        "highlight": "Next Big Idea.",
        "description": (
            "Build projects, learn new technologies, "
            "and share knowledge with the world."
        ),
    }

    return render(request, "home.html", context)

