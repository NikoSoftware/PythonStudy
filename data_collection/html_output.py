# coding=utf-8
class HtmlOutPuter(object):

    def __init__(self):
        self.datas = set()

    def collect_data(self, data):

        if data is None:
            return
        for i in data:
            self.datas.add(i)
        return

    def output_data(self):

        for data in self.datas:
            print(data)

    def output_html(sel, html):
        fout = open("output.html", "w")
        fout.write(html)
        fout.close()

    def output_text(self):
        file = open("output.text", "w")
        for index, data in enumerate(self.datas):
            file.write(str(index)+".")
            file.write(str(data))
            file.write("\n")


        file.close()