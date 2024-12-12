from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def user_profile_view(request):
    user = request.user
    profile = user.profile
    if not profile:
        return JsonResponse({'error': 'Profile not found'}, status=404)
    return JsonResponse(profile)
