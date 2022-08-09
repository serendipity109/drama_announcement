import requests
from pyquery import PyQuery as pq
import pickle


def check_new():
    with open("dcu", "rb") as fp:
        history = pickle.load(fp)

    html = requests.get('https://dramasq.biz/jp220116b/')
    html.encoding = 'utf-8'
    doc = pq(html.text)
    new_rec = []
    for item in doc('.items.sizing a').items():
        new_rec.append(item.text())

    if history:
        new_episode = ','.join(list(set(new_rec) - set(history)))
    new_episode = ','.join(list(set(new_rec) - set(history))) if history else ','.join(new_rec)
    if not new_episode: return False
    else:
        with open("dcu", "wb") as fp:
            pickle.dump(new_rec, fp)
        return new_episode
        # return True
