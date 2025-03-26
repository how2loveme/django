from django.http import HttpResponse
from django.template import Context, Template, loader
from .utils import checkdeploy

def index(request):
    template = loader.get_template("checkdeploy/index.html")
    return HttpResponse(template.render({}, request))

def run(request):
    exists, non_exists, targets, non_targets = checkdeploy(request.GET['ticket_arr'])
    template = loader.get_template("checkdeploy/result.html")
    return HttpResponse(
        template.render(
            {
                "exists": exists,
                "non_exists": non_exists,
                "targets": targets,
                "non_targets": non_targets,
            },
            request
        )
    )
    # template = loader.get_template("checkdeploy/result.html")
    # return render(request, "checkdeploy/result.html", {})
    # return render(request, "checkdeploy/result.html", {exists, non_exists, targets, non_targets})
    # return render(
    #     request,
    #     "checkdeploy/result.html",
    #     {
    #         exists: exists,
    #         non_exists: non_exists,
    #         targets: targets,
    #         non_targets: non_targets
    #     }
    # )

    # question = get_object_or_404(Question, pk=question_id)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST["choice"])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(
    #         request,
    #         "polls/detail.html",
    #         {
    #             "question": question,
    #             "error_message": "You didn't select a choice.",
    #         },
    #     )
    # else:
    #     selected_choice.votes = F("votes") + 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))