from requests_html import HTMLSession

inf_url = ''
session = HTMLSession()
response_in = session.get(inf_url)
gpu_offers = response_in.json()