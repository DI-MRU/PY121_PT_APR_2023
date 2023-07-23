from django.shortcuts import render
from django.http import HttpResponse  # pass view information into the browser

# Create your views here.


# takes a request, returns a response
def index(request):
    return render(request, "landing_page.html")


def about(request):
    return HttpResponse("<h1>Welcome Users</h1> <p>This is the about us page.</p>")


from django.shortcuts import render


def homepage(request):
    user = {"first_name": "John", "last_name": "Doe"}

    subjects = [
        {
            "title": "How to setup Django",
            "author": "Maria",
            "content": "iuyteisuyatfiu7as6r783w6c4w38tah4ow, ajkegtrc783twcr879tw3r esarvweiuryfo futdf78taw4",
            "approval": False,
        },
        {
            "title": "How to cake an amazing pie",
            "author": "Chef Mark",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "approval": True,
        },
        {
            "title": "How to be good at Django",
            "author": "Guru Vincent",
            "approval": True,
        },
    ]

    context = {"user": user, "subjects": subjects}
    return render(request, "posts/homepage.html", context)


def profile(request):
    context = {
        "users": [
            {"username": "Safidy", "gender": "F"},
            {"username": "Naiza", "gender": "F"},
            {"username": "Sleeping Dhivyesh", "gender": "M"},
            {"username": "Gone Martine", "gender": "F"},
        ]
    }

    return render(request, "profile_user.html", context)
