import csv

class Metrics:

    TIME_LATENCY = "time_latency"
    TIME_WAIT =  "time_wait"
    TIME_RESPONSE = "time_response"
    TIME_SERVICE = "time_service"
    TIME_TOTAL_RESPONSE = "time_total_response"

    WATT_SERVICE = "byService"
    WATT_UPTIME = "byUptime"


    def __init__(self, default_results_path="result"):
        columns_event = ["id","type", "app", "module", "message","DES.src","DES.dst","TOPO.src","TOPO.dst","module.src","service", "time_in","time_out",
                         "time_emit","time_reception"]
        columns_link = ["id","type", "src", "dst", "app", "latency", "message", "ctime", "size","buffer"]

        path = default_results_path
        if path is not None:
            self.__filef = open("%s.csv" % path, "w")
            self.__filel = open("%s_link.csv"%path, "w")
            self.__ff = csv.writer(self.__filef)
            self.__ff_link = csv.writer(self.__filel)
            self.__ff.writerow(columns_event)
            self.__ff_link.writerow(columns_link)
        else:
            self.__filef = None
            self.__filel = None
            self.__ff = None
            self.__ff_link = None

    def flush(self):
        if self.__filef is not None:
            self.__filef.flush()
        if self.__filel is not None:
            self.__filel.flush()

    def insert(self,value):
        if self.__ff is None:
            return
        self.__ff.writerow([value["id"],value["type"],
                    value["app"],
                    value["module"],
                    value["message"],
                    value["DES.src"],
                    value["DES.dst"],
                    value["TOPO.src"],
                    value["TOPO.dst"],
                    value["module.src"],
                    value["service"],
                    value["time_in"],
                    value["time_out"],
                    value["time_emit"],
                    value["time_reception"]
                            ])

    def insert_link(self, value):
        if self.__ff_link is None:
            return
        self.__ff_link.writerow([value["id"],value["type"],
                    value["src"],
                    value["dst"],
                    value["app"],
                    value["latency"],
                    value["message"],
                    value["ctime"],
                    value["size"],
                    value["buffer"],

                            ])

    def close(self):
        if self.__filef is not None:
            self.__filef.close()
        if self.__filel is not None:
            self.__filel.close()
