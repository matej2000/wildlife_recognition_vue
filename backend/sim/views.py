from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import json
import pdb

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, UploadFileForm
from .validators import FileValidator
from .services.fastapi_client import call_fastapi


@ensure_csrf_cookie
@require_http_methods(["GET"])
def set_csrf_token(request):
    """
    We set the CSRF cookie on the frontend.
    """
    return JsonResponse({"message": "CSRF cookie set"})


@require_http_methods(["POST"])
def login_view(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        email = data["email"]
        password = data["password"]
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Invalid JSON"}, status=400)

    user = authenticate(request, username=email, password=password)

    if user:
        login(request, user)
        return JsonResponse({"success": True})
    return JsonResponse(
        {"success": False, "message": "Invalid credentials"}, status=401
    )


def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logged out"})


@require_http_methods(["GET"])
def user(request):
    if request.user.is_authenticated:
        return JsonResponse(
            {"username": request.user.username, "email": request.user.email}
        )
    return JsonResponse({"message": "Not logged in"}, status=401)


@require_http_methods(["POST"])
def register(request):
    data = json.loads(request.body.decode("utf-8"))
    form = CreateUserForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({"success": "User registered successfully"}, status=201)
    else:
        errors = form.errors.as_json()
        return JsonResponse({"error": errors}, status=400)


@require_http_methods(["POST"])
def upload_file(request, model_name):
    form = UploadFileForm(request.POST, request.FILES)

    if not form.is_valid():
        print("FORM ERRORS:", form.errors)
        return JsonResponse({"error": form.errors.get_json_data()}, status=400)

    image = request.FILES.get("file")

    if image is None:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    print("Filename:", image.name)
    print("Content type:", image.content_type)
    print("File size:", image.size)

    try:
        validate_file = FileValidator(
            max_size=10 * 1024 * 1024, content_types=["image/png", "image/jpeg"]
        )
        validate_file(image)

        result = call_fastapi(model_name, image)
        return JsonResponse(result)

    except Exception as e:
        import traceback

        traceback.print_exc()

        return JsonResponse({"error": str(e)}, status=400)
