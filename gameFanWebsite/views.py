import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

playerList = [
    {
        "name": "Bryn Kenney",
        "pic": "https://media.cardplayer.com/assets/000/026/576/BRYN_Q_A_FEAT.jpg",
        "ranking": 1,
        "description": "Bryn KenneyはTriton Pokerのライブポーカートーナメント史上最大の＄20,563,324を受け取った経験があります。プロポーカープレイヤーになる前に世界で有名なマジック・ザ・ギャザリングというトレーディングカードゲームを熱狂的にプレイしていたことで有名です。",
    },
    {
        "name": "Justin Bonomo",
        "pic": "https://www.4media.tv/wp-content/uploads/2021/12/39751991242_5ae6e8fa09_b-1024x683-1.jpg",
        "ranking": 2,
        "description": "Justin Bonomoもプロポーカープレイヤーになる前は世界で有名なマジック・ザ・ギャザリングのプレイヤーとして活躍していました。彼は500ドルから始めて10000ドルにし、そのお金を軍資金に、全仏オープンでのEPTの初年度に史上最年少で4位になった経歴を持っています。",
    },
    {
        "name": "Daniel Negreanu",
        "pic": "https://cdn.pocketfives.com/p5wp/2019/04/daniel-negreanu-leaves-team-pokerstars.jpg",
        "ranking": 3,
        "description": "Daniel Negreanuは6つのWSOPのブレスレットと2つのWPTチャンピョンシップを勝ち取ったプロポーカープレイヤーです。また、2004年と2013年にWSOP年間最優秀プレイヤーに選ばれ、世界で賞賛を2回以上受けた唯一のプレイヤーになりました。",
    },
]

def indexView(request):
    samplePicList = [
        'https://cdn.pixabay.com/photo/2016/02/15/14/45/playing-cards-1201257_1280.jpg',
        'https://img.freepik.com/free-vector/playing-casino-card-chips-and-dice-flying-background_1017-30143.jpg?t=st=1658662634~exp=1658663234~hmac=c8db1caf344d477fbb32c3714761570309f901cd2082912beb17ecb45ac1146a&w=1800',
        'https://img.freepik.com/premium-photo/poker-player-showing-a-pair-of-aces_306105-9.jpg?w=1800',
        'https://img.freepik.com/premium-photo/gambling-close-up-cards-for-playing-poker-on-a-gaming-table-in-a-casino_391052-1268.jpg?w=1800',
    ]
    ctx = {"pic": random.choice(samplePicList)}
    return HttpResponse(render(request, 'index.html', ctx))


def rulesView(request):
    return HttpResponse(render(request, 'rules.html'))

def notablesDetail(request):
    return redirect('notablesDetail', notableIndex=0)


def notablesList(request):
    ctx = {"data": playerList}
    return HttpResponse(render(request, 'notables.html', ctx))


def externalLinks(request):
    return HttpResponse(render(request, 'externalLinks.html'))