from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
import json
from . import check_url
from django.views.decorators.csrf import csrf_exempt
from .models import reviews, notable_links


@csrf_exempt
def processing_url(request):
    link_list, flag = notable_links.objects.all(), True
    if request.method == 'POST':
        url = request.POST.get('url')
        if len(url) == 0:
            return JsonResponse({"error": 'Link is null error'})
        else:
            for link in link_list:
                if link.url == url:
                    flag, need_reviews, reviews_list = False, {}, reviews.objects.filter(id_url=link.id)
                    need_reviews = [{"email": review.email_author, "comment": review.review} for review in
                                    reviews_list]
                break
            if flag:
                new_url, need_reviews = notable_links(
                    url=url
                ), []
                new_url.save()
            try:
                res = check_url.check_link(url)
            except:
                return JsonResponse({"error": "Invalid link"})
        a = len(need_reviews)
    return JsonResponse({"statistic": res, "reviews": need_reviews, "count_reviews": a})


@csrf_exempt
def add_review(request):
    flag = True
    review_data = request.POST
    links_list = notable_links.objects.all()
    for link in links_list:
        if review_data.get("url") == link.url:
            try:
                new_review = reviews(
                    id_url=link.id,
                    email_author=review_data.get("email"),
                    review=review_data.get("review")
                )
                new_review.save()
            except:
                return JsonResponse({'error': 'Invalid form'})
            flag = False
    if flag:
        return JsonResponse({'error': 'Dont found url'})
    return JsonResponse({'error': 'Add ok!'})


@csrf_exempt
def get_reviews(request):
    links_list = notable_links.objects.all()
    url = request.GET.get("url")
    for link in links_list:
        if link.url == url:
            flag, need_reviews, reviews_list = False, {}, reviews.objects.filter(id_url=link.id)
            need_reviews = [{"email": review.email_author, "comment": review.review} for review in
                            reviews_list]
        break

    return JsonResponse({"reviews": need_reviews})