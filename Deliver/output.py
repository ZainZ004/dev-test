word = {'filechoose': '选择文件',
        'check': '确认[y/n]',
        'none': '无此选项',
        'loading': '加载中',
        'nodata': '工作表中无数据',
        'choosefiles': '请选择文件:',
        'IndexError': '不在可选范围',
        'InputError': '请输入数值',
        'TypeError': '请输入数字',
        'unknown': '未知错误',
        'FileNotFound': '无法找到文件'
        }
from finder import Files


class IO(object):
    def choose(self=None):
        s = 0
        files = Files.search()
        if len(files) > 1:
            for fileshow in files:
                s = s+1
                print('[', s, ']', fileshow)
            while True:
                try:
                    discion = input(word['choosefiles'])
                    discion = int(discion)-1
                    return files[discion]
                except IndexError:
                    print(word['IndexError'])
                except TypeError:
                    print(word['TypeError'])
                except ValueError:
                    print(word['InputError'])
                else:
                    print(word['unknown'])
        elif len(files) == 1:
            print(word['filechoose'], files[0])
            dis = input(word['check'])
            if dis == 'y':
                return files[0]
            elif dis == 'n':
                raise FileNotFoundError(word['FileNotFound'])
            else:
                raise TypeError(word['none'])
        else:
            raise FileExistsError(word['FileNotFound'])
    def report(self=None):
        file = IO.choose()
        Files.search_in_file(Files.check_data(None,file))
