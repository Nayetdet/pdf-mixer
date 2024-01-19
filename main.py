import PyPDF2
import random
import json
import sys
import io
import os


DEFAULTCONFIG = {
    'path': '',
    'randomize': False,
    'deletable_pages': {
        'example': [
            0,
            1,
            2
        ]
    }
}


def dataloader():
    files = os.listdir(os.path.dirname(os.path.realpath(__file__)))
    if 'settings.json' not in files:
        with open('settings.json', 'w') as file:
            json.dump(DEFAULTCONFIG, file, indent = 4)

    try:
        with open('settings.json') as data:
            userconfig = json.load(data)
            if (
                {k: type(v) for k, v in DEFAULTCONFIG.items()} != {k: type(v) for k, v in userconfig.items()}
                or not all(isinstance(value, list) for value in userconfig.get('deletable_pages').values())
            ): sys.exit('O arquivo de configurações foi modificado incorretamente.')
    except FileNotFoundError: sys.exit('O arquivo de configurações foi deletado.')
    return userconfig.values()


class PdfMixer:
    def background_setter(func):
        def wrapper(self, *args, **kwargs):
            self.pdf_processing_setup()
            result = func(self, *args, **kwargs)
            self.tmp_writer(self.writer)
            return result
        return wrapper


    def pdf_processing_setup(self):
        self.reader = PyPDF2.PdfReader(self.file)
        self.writer = PyPDF2.PdfWriter()


    def tmp_writer(self, writer):
        self.tmp = io.BytesIO()
        writer.write(self.tmp)
        self.tmp.seek(0)


    @background_setter
    def page_deleter(self):
        for index, page in enumerate(self.reader.pages):
            if index not in deletable_pages.get(self.file[:-4], []):
                page.compress_content_streams()
                self.writer.add_page(page)


    @background_setter
    def page_orderer(self):
        pages = len(self.reader.pages)
        order = random.sample(range(pages), pages) if randomize else range(pages)
        for page in order:
            self.writer.add_page(self.reader.pages[page])


    def file_processer(self, files):
        merger = PyPDF2.PdfMerger()
        for index, file in enumerate(files):
            self.file = os.path.join(path, file)
            self.page_deleter()

            merger.append(self.tmp)
            print(f'Progresso: {index}/{len(files)}')

        self.tmp_writer(merger)
        self.file = self.tmp
        self.page_orderer()

        self.writer.write('output.pdf')
        print('Processo encerrado.')


if __name__ == '__main__':
    path, randomize, deletable_pages = dataloader()

    if path and not os.path.exists(path): os.makedirs(path)
    files = [f for f in os.listdir(path or None) if f != 'output.pdf' and f.endswith('.pdf')]

    if files: PdfMixer().file_processer(files)
    else: print('Nenhum arquivo .pdf foi encontrado no caminho requisitado.')
