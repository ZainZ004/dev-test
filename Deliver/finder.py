import glob
import xlrd
from output import IO


class Files(object):

    def search(self=None):
        files = []
        types = ("*.xls", "*.xlsx")
        for typesc in types:
            for filess in glob.glob(typesc):
                files.insert(0, filess)
        return files

    def check_data(self=None, file=IO.choose):
        havedata=[]
        data = xlrd.open_workbook(file)
        for search_sheets in range(data.nsheets):
            try:
                table = data.sheet_by_index(search_sheets)
                nrows = table.nrows
                if nrows == 0:
                    pass
                else:
                    havedata.insert(0,search_sheets)
            except:
                continue
        if len(havedata) < 1:
            return 'Error'
        return havedata

    def search_in_file(self=None,search_sheet=Files.check_data,search_word='姓名'):
        pass        