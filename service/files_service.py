import os


class FileService:

    @staticmethod
    def get_abs_dirname():
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def get_aujourdhui_file_path():
        scrap_dir_name = "../docs/aujourdhui.txt"
        scrap_dir_path = os.path.join(FileService.get_abs_dirname(), scrap_dir_name)
        return scrap_dir_path

    @staticmethod
    def get_hier_file_path():
        scrap_dir_name = "../docs/hier.txt"
        scrap_dir_path = os.path.join(FileService.get_abs_dirname(), scrap_dir_name)
        return scrap_dir_path
