# coding: utf-8
__author__ = "Reo Kontani (reokt99@gmail.com)"
__date__ = "19 Mar 2015"
__status__ = "development"
__version__ = "0.1"

# ============================================================
# Log
# ============================================================
import logging
from traceback import format_exc
LOGGING_LEVEL = logging.INFO if __status__ == "production" else logging.DEBUG # 開発状態がdevelopmentの場合はlogging.DEBUGが
logging.basicConfig(format="%(asctime)s %(levelname)s %(module)s %(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S", level=LOGGING_LEVEL)

                    #logガ出力した時刻、loglevel,ファイルname,ログメッセージが出てくるなど



# ============================================================
# MySQL
# ============================================================
import mysql.connector
CONFIG = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'quixote'
}


def save(table_name, data):
    cnx = mysql.connector.connect(**CONFIG)
    cur = cnx.cursor(buffered=True)

    try:
        for d in data:
            col, val = "", ""

             #col, val ="","">>> col''>>> val''

            for k, v in d.items():
                col += "%s," % str(k)
                val += "'%s'," % str(v)

            sql = "INSERT INTO %s (%s) VALUES (%s)"
            cur.execute(sql % (table_name, col[:-1], val[:-1]))

        cnx.commit()
        logging.info("insert %d records successfully" % len(data))

    except Exception, e:
        raise e

    finally:
        cur.close()
        cnx.close()


# ============================================================
# Scraping
# ============================================================
import requests
import json
import re

URL_PREV_PROG = ("https://demanda.ree.es/WSvisionaMoviles%sRest"
                 "/resources/prevProg%s")
URL_DEMANDA = ("https://demanda.ree.es/WSvisionaMoviles%sRest"
               "/resources/demandaGeneracion%s")
REGIONS = {
    "Peninsula": ["DEMANDA"],
    "Baleares": ["MALLORCA", "MENORCA", "IBI-FORM", "MALL-MEN"],
    "Canarias": ["TENERIFE", "EL_HIERRO", "GCANARIA", "LZ_FV",
                 "FUERTEVE", "LA_GOMERA", "LANZAROT", "LA_PALMA"]
    }


def cleanse_one(url_1, item_1):
    prog = re.compile(r'[A-Z]+')

    for k, v in item_1.items():
        if k != "ts":
            continue

        tmp = v.split(" ")[1].split(":")[0]
        # EXAMPLE: "2015-03-15 02:00" => "02"

        if prog.search(tmp) is not None:
            item_1[k] = v.replace(tmp, ("0" + tmp[:-1])[-2:])
            # EXAMPLE: "2A" => "02", "12B" => "12"

            save("dulcinea", [{"url": url_1}])

    return item_1


def fetch_one(region, area, dt):
    payload = {"curva": area, "fecha": dt, "callback": ""}
    headers = {"User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8;"
                              " rv:38.0) Gecko/20100101 Firefox/38.0")}

    result = []
    try:
        # API 1
        api_1 = URL_PREV_PROG % (region, region)
        req_1 = requests.get(api_1, params=payload, headers=headers)
        req_1.raise_for_status()
        res_1 = list(json.loads(req_1.text[1:-2]).values())[0]

        # API 2
        api_2 = URL_DEMANDA % (region, region)
        req_2 = requests.get(api_2, params=payload, headers=headers)
        req_2.raise_for_status()
        res_2 = list(json.loads(req_2.text[1:-2]).values())[0]

        # Merge
        for item_1, item_2 in zip(res_1, res_2):
            item_1.update(item_2)
            item_1 = cleanse_one(req_1.url, item_1)
            item_1.update({"curva": area})
            result.append(item_1)

        return result
    except Exception, e:
        raise e


def fetch(dt):
    result = []
    for region, areas in REGIONS.items():
        [result.extend(fetch_one(region, _a, dt)) for _a in areas]

    return result


# ============================================================
# Launch
# ============================================================
from datetime import datetime
from datetime import timedelta
THE_ORIGIN = datetime(2014, 10, 26)
ONE_DAY = timedelta(days=1)


def main():
    dt = THE_ORIGIN

    for i in range(365):
        dt_str = dt.strftime("%Y-%m-%d")
        print "==================== %s ====================" % dt_str

        result = fetch(dt_str)
        save("sancho", result)
        dt -= ONE_DAY


if __name__ == '__main__':
    try:
        logging.info("Start")
        main()
    except Exception, e:
        logging.error(format_exc())
        raise e
    finally:
        logging.info("Finish")
