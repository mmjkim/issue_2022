import os
import common.config.folderpath as fp


class FilePathClass:

    def __init__(self):
        # 파일 패스 정의
        self.root_path = fp.ROOT_PATH
        self.data_path = fp.DATA_PATH
        self.collect_path = fp.DATA_COLL_PATH
        self.use_path = fp.DATA_USE_PATH
        self.result_path = fp.DATA_RESULT_PATH
        self.log_path = fp.LOG_PATH

        try:
            if not os.path.exists(self.root_path):
                raise ValueError
        except ValueError:
            print("폴더 확인")

    # 폴더가 존재하는지 check
    def is_path_exist_check(self, path):
        if not os.path.exists(path):
            return False
        else:
            return True

    # 폴더생성
    def make_path(self, path):
        if not os.path.exists(path):
           os.makedirs(path)
        return path

    # get Root 폴더명
    def get_root_path(self):
        return self.root_path + ""

    # get Data 폴더명
    def get_data_path(self):
        folder = self.root_path + '\\' + self.data_path + '\\'
       # print("================ : ", folder)
        return self.make_path(folder)

    # get ResultPath 폴더명
    def get_result_path(self):
        folder = self.root_path + '\\' + self.data_path + '\\' + self.result_path + '\\'
       # print("================ : ", folder)
        return self.make_path(folder)

    # get LogPath 폴더명
    def get_log_path(self):
        folder = self.root_path + '\\' + self.result_path + '\\' + self.log_path + '\\'
       # print("================ : ", folder)
        return self.make_path(folder)

    # get 수집데이터 폴더명
    def get_raw_collect_path(self):
        folder = self.root_path + '\\' + self.data_path + '\\' + self.collect_path + '\\'
       # print("================ : ", folder)
        return self.make_path(folder)

    # get 사용데이터 폴더명
    def get_raw_use_path(self):
        folder = self.root_path + '\\' + self.data_path + '\\' + self.use_path + '\\'
       # print("================ : ", folder)
        return self.make_path(folder)

    # 다운로드 폴더명
    def get_download_path(self):
        folder = self.root_path + '\\' + 'Downloads/'
       # print("================ : ", folder)
        return self.make_path(folder)
