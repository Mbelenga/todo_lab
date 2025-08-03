from django.shortcuts import render

def index(request):
    """The Home Page for learning_log. """
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ show all topics """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topics = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    fgfggfggfgggfggf
    gggfggfgggfggggg
    ggfggggfgggfgggg
    ffggfgfgfgfgfgffuy

    j;l;j';lj;lhg;j';glj;''ghj;'g';jl';g
    ggfgggfgfgfgfgretretg
    reygfgdgvccvtrtr
    tt