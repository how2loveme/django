from django.http import HttpResponse
from django.template import Context, Template, loader
from .utils import checkdeploy

def index(request):
    template = loader.get_template("checkdeploy/index.html")
    return HttpResponse(template.render({}, request))

def run(request):
    exists, nonExists, targets, nonTargets = checkdeploy(request.GET['ticketArr'])
    template = loader.get_template("checkdeploy/result.html")
    return HttpResponse(
        template.render(
            {
                "exists": exists,
                "nonExists": nonExists,
                "targets": targets,
                "nonTargets": nonTargets,
            },
            request
        )
    )
    # template = loader.get_template("checkdeploy/result.html")
    # return render(request, "checkdeploy/result.html", {})
    # return render(request, "checkdeploy/result.html", {exists, nonExists, targets, nonTargets})
    # return render(
    #     request,
    #     "checkdeploy/result.html",
    #     {
    #         exists: exists,
    #         nonExists: nonExists,
    #         targets: targets,
    #         nonTargets: nonTargets
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