import glob
import xlrd


class Files(object):

    def search(self=None):
        files = []
        types = ("*.xls", "*.xlsx")
        for typesc in types:
            for filess in glob.glob(typesc):
                files.insert(0, filess)
        return files

    def check_data(self=None, file=''):
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
            raise FileNotFoundError('No data')
        return havedata

    def search_in_file(self=None,search_sheet=None,search_word='姓名'):
        pass        