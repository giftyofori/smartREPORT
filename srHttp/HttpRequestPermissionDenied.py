from django.shortcuts import render_to_response


def HttpRequestPermissionDenied(template ,message):
    return render_to_response(template ,dict(message = message))
