import os
import sys
import json
import datetime
import requests
from rich import print
from rich.panel import Panel
from bs4 import BeautifulSoup

os.system('clear')

date = datetime.datetime.now()


def cari():
    url_cari = "https://api.myquran.com/v2/sholat/kota/semua"
    respone_url = requests.get(url_cari)

    if respone_url.status_code == 200:
        data = json.loads(respone_url.text)

        data_json = data['data']
        for data_id in data_json:
            semua_id = data_id['id']
            semua_lokasi = data_id['lokasi']
            print(Panel(f'ID : {semua_id} LOKASI : {semua_lokasi}',title=f"{semua_id}"))
        print('')

def jadwal_solat():
    m = date.strftime("%m")
    d = date.strftime("%d")
    y = date.strftime("%Y")
    print('')
    cari()
    no = input(" => Choice : ")
    url_jadwal = f'https://api.myquran.com/v2/sholat/jadwal/{no}/{y}-{m}-{d}'
    respone_jadwal = requests.get(url_jadwal)

    if respone_jadwal.status_code == 200:
        data_jadwal = json.loads(respone_jadwal.text)

        data_json2 = data_jadwal['data']
        id_1 = data_json2['id']
        lokasi_1 = data_json2['lokasi']
        daerah_1 = data_json2['daerah']
        print('')
        print(Panel(f'ID : {id_1} \nLOKASI : {lokasi_1} \nDAERAH : {daerah_1}',title=f'{daerah_1}'))
        print('')
        jadwal_1 = data_json2['jadwal']
        tanggal = jadwal_1['tanggal']
        imsak = jadwal_1['imsak']
        subuh = jadwal_1['subuh']
        terbit = jadwal_1['terbit']
        dhuha = jadwal_1['dhuha']
        dzuhur = jadwal_1['dzuhur']
        ashar = jadwal_1['ashar']
        maghrib = jadwal_1['maghrib'] 
        isya = jadwal_1['isya']
        dates = jadwal_1['date']
        print(Panel(f'TANGGAL : {tanggal} \nIMSAK : {imsak} \nSUBUH : {subuh} \nTERBIT : {terbit} \nDHUHA : {dhuha} \nDZUHUR : {dzuhur} \nASHAR : {ashar} \nMAGHRIB : {maghrib} \nISYA : {isya} \nDATE : {dates}',title="JADWAL SOLAT"))

def banner():
    print(Panel("[bold white]Jadwal -[bold yellow] solat [bold red] By [bold cyan] Zaunksssc_\n",title="[bold cyan] PYhonCOde"))

banner()
jadwal_solat()
