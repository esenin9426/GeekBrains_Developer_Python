import datetime
import csv
import shutil

class Notice:
    def __init__(self, file_name:str = None):
        self.file_name = file_name if file_name else "notebook.csv"
        self.last_number = 0
        try:
            f1 = open(self.file_name, "r")
            last_line = f1.readlines()[-1]
            self.last_number = int(last_line.split(",")[0])
        except FileNotFoundError:
            f1 = open(self.file_name, "x")
        except IndexError:
            pass
        except ValueError:
            pass
        finally:
            f1.close()

    def insert_notice(self, title: str, body:str, date = datetime.date.today()):
        self.last_number += 1
        file = open(self.file_name, 'a')
        writer = csv.writer(file)
        writer.writerow([self.last_number, date, title, body])
        file.close()

    def delete_notice(self, id:int = None, title:str = None):
        try:
            tmp = open(self.file_name + "_tmp", "x")
            tmp_csv = csv.writer(tmp)
            with open(self.file_name, "r") as f:
                for line in f:
                    if id and str(id) == line.split(",")[0]:
                        continue
                    if title and str(title) in line.split(",")[2]:
                        continue
                    tmp_csv.writerow(line.replace("\n", "").split(","))
        finally:
            tmp.close()
        shutil.move(self.file_name + "_tmp", self.file_name)

    def read_notice(self, id:int = None, title:str = None):
        with open(self.file_name, "r") as f:
            for line in f:
                if id and str(id) == line.split(",")[0]:
                    print(line, end="")
                if title and str(title) in line.split(",")[2]:
                    print(line, end="")


    def read_all(self):
        with open(self.file_name, "r") as f:
            for line in f:
                print(line, end="")

    def update_line(self, id, title: str = None, body:str = None,):
        try:
            tmp = open(self.file_name + "_tmp", "x")
            tmp_csv = csv.writer(tmp)
            with open(self.file_name, "r") as f:
                for line in f:
                    insert_str = line.replace("\n", "").split(",")
                    if id and str(id) == line.split(",")[0]:
                        if title:
                            insert_str[2] = title
                        if body:
                            insert_str[3] = body
                    tmp_csv.writerow(insert_str)
        finally:
            tmp.close()
        shutil.move(self.file_name + "_tmp", self.file_name)
