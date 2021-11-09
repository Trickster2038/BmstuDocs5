import argparse
import pandas as pd
import json

parser = argparse.ArgumentParser()
parser.add_argument('--json', nargs='?', default="")

args = parser.parse_args()

json_mode = args.json is None

names = ["ip", "1", "2", "3", "4", "url", "status", "size", "5", "6", "7"]
df = pd.read_csv("access.log", sep=" ", usecols=range(
    11), low_memory=False, header=None, names=names)
df = df.iloc[:, [0, 5, 6, 7, 8, 9, 10]]


def total_size(df):
    return df.shape[0]


def groupby_methods(df):
    df_methods_1 = df.copy()
    df_methods_1["method"] = df_methods_1.apply(
        lambda row: row["url"].split()[0], axis=1)
    df_methods_2 = pd.DataFrame(df_methods_1["method"])
    df_methods_2["cnt"] = 0
    return df_methods_2.groupby(by=["method"], as_index=False).count().reset_index(drop=True)


def groupby_methods_normal(df):
    df_meths = groupby_methods(df)
    return df_meths.loc[(df_meths["method"].astype('str').str.len() < 10)].reset_index(drop=True)


def groupby_methods_unnormal(df):
    df_meths = groupby_methods(df)
    return df_meths.loc[(df_meths["method"].astype('str').str.len() >= 10)].reset_index(drop=True)


def top10_urls(df):
    df_urls = pd.DataFrame(df.iloc[:, 1])
    df_urls["cnt"] = 0
    df_urls2 = df_urls.copy()
    df_urls2["url_without_params"] = df_urls.apply(
        lambda row: row["url"].split()[1], axis=1)
    del df_urls2["url"]
    df_urls_g = df_urls2.groupby(
        by=["url_without_params"], as_index=False).count()
    return df_urls_g.sort_values("cnt", ascending=False).head(10).reset_index(drop=True)


def top5_size_4xx(df):
    df_filtered = df.query(
        "status >= 400 and status < 500 and size != '-'").iloc[:, 0:4].copy()
    df_filtered["size"] = df_filtered["size"].astype(int)
    return df_filtered.sort_values("size", ascending=False).head(5).reset_index(drop=True)


def top5_users_5xx(df):
    df_5xx = df.query("status >= 500 and status < 600").iloc[:, [0]]
    df_5xx["cnt"] = 0
    return df_5xx.groupby(by=["ip"], as_index=False).count().sort_values("cnt", ascending=False).head(5).reset_index(drop=True)


def df_to_json(df):
    return json.loads(df.to_json(orient="split"))


if not json_mode:
    s = "Отчет по логу\n"
    s += "Кол-во запросов: " + str(total_size(df))

    s += "\n\nЧисло запросов (по типу):\n"
    s += groupby_methods_normal(df).to_string(index=False)

    s += "\n\nЧисло нестандартных запросов (по типу):\n"
    s += groupby_methods_unnormal(df).to_string(index=False)

    s += "\n\nТоп 10 самых частых запросов:\n"
    s += top10_urls(df).to_string(index=False)

    s += "\n\nТоп 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:\n"
    s += top5_size_4xx(df).to_string(index=False)

    s += "\n\nТоп 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:\n"
    s += top5_users_5xx(df).to_string(index=False)

    with open("report.txt", "w+") as f:
        f.writelines(s)
else:
    report_json = {'total quaries': total_size(df),
                   'by_types_normal': df_to_json(groupby_methods_normal(df)),
                   'by_types_unnormal': df_to_json(groupby_methods_unnormal(df)),
                   'top10_by_rate': df_to_json(top10_urls(df)),
                   'top5_client_fails_by_size': df_to_json(top5_size_4xx(df)),
                   'top5_users_by_requests_num': df_to_json(top5_users_5xx(df))}
    with open('report.json', 'w') as outfile:
        json.dump(report_json, outfile, indent=4)
