from django.shortcuts import redirect, render
from .rules import QUESTIONS, SOURCES, build_result

ORDER = [
    "duracao", "origem", "diabetes", "local", "sinais_urgencia",
    "queimadura_especial", "cor", "odor", "secrecao", "bordas",
]

def inicio(request):
    request.session.flush()
    return render(request, "triagem/inicio.html")

def questionario(request):
    if request.method == "POST":
        answers = request.session.get("answers", {})
        answers.update({k: v for k, v in request.POST.items() if k in QUESTIONS})
        request.session["answers"] = answers

        if answers.get("sinais_urgencia") == "sim":
            return redirect("triagem:resultado")
        if answers.get("queimadura_especial") == "sim":
            return redirect("triagem:resultado")

        current = request.POST.get("current")
        try:
            idx = ORDER.index(current)
        except ValueError:
            idx = -1

        next_key = None
        for key in ORDER[idx + 1:]:
            if key == "queimadura_especial" and answers.get("origem") != "queimadura":
                continue
            next_key = key
            break

        if next_key:
            request.session["current"] = next_key
            return redirect("triagem:questionario")
        return redirect("triagem:resultado")

    answers = request.session.get("answers", {})
    current = request.session.get("current", ORDER[0])
    question = QUESTIONS[current]
    visible_order = [
        key for key in ORDER
        if key != "queimadura_especial" or answers.get("origem") == "queimadura"
    ]
    position = visible_order.index(current) + 1
    progress = round(position * 100 / len(visible_order), 1)

    return render(request, "triagem/questionario.html", {
        "question": question,
        "question_key": current,
        "position": position,
        "total": len(visible_order),
        "progress": progress,
        "source": SOURCES[question["source"]],
    })

def resultado(request):
    data = request.session.get("answers", {})
    return render(request, "triagem/resultado.html", {
        "result": build_result(data),
        "answers": data,
    })
