from django.shortcuts import render
import markdown2
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_to_HTML(entry_name):
    md = markdown2.Markdown()
    entry  = util.get_entry(entry_name)
    html = md.convert(entry) if entry else None
    return html

def entry(request, entry_name):
    html = convert_to_HTML(entry_name)
    if html is None:
        return render(request, "encyclopedia/wrong_entry.html", {
            "entryTitle": entry_name
    })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": html,
            "entryTitle": entry_name
        })


def search(request):

    if request.method == 'POST':

        input = request.POST['q']
        html = convert_to_HTML(input)
        if html:
            return render(request, "encyclopedia/entry.html", {
                "entry": html,
                "entryTitle": input
            })
        else:
            result = []
            entries = util.list_entries()
            for entry in entries:
                if input.lower() in entry.lower():
                    result.append(entry)
            return render(request, "encyclopedia/search.html", {
                "entries": result,
            })

def new(request):
      return render(request, "encyclopedia/new.html")

def save(request):
    if request.method == 'POST':

        input_title = request.POST['title']
        input_text = request.POST['text']
        entries = util.list_entries()
        if input_title in entries:
            return render(request, "encyclopedia/already_exist.html")
        else:
            util.save_entry(input_title, input_text)
            html = convert_to_HTML(input_title)
            return render(request, "encyclopedia/entry.html", {
                "entry": html,
                "entryTitle": input_title
            })

def rand(request):
    arr = util.list_entries()
    entry_title = random.choice(arr)
    html = convert_to_HTML(entry_title)
    return render(request, "encyclopedia/entry.html", {
            "entry": html,
            "entryTitle": entry_title
        })


def edit(request):
    if request.method == 'POST':
        input_title = request.POST['title']
        text = util.get_entry(input_title)
        return render(request, "encyclopedia/edit.html", {
            "entry": text,
            "entryTitle": input_title
        })

def save_edit(request):
    if request.method == 'POST':
        input_title = request.POST['title']
        input_text = request.POST['text']
        util.save_entry(input_title, input_text)
        html = convert_to_HTML(input_title)
        return render(request, "encyclopedia/entry.html", {
            "entry": html,
            "entryTitle": input_title
        })