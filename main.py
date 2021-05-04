import Standard
import Utils
import pandas
import math
import FAIRNessInfo
import Config
import imgkit
import os

class StandardsUtils:

    UTILS = Utils.Utils()

    def __init__(self, input_file):
        self.INPUT_FILE = input_file

    def generate_standards_images(self):
        standards = []
        excel_data_df = pandas.read_excel(self.INPUT_FILE, header=(Config.HEADER_START_ROW - 1),
                                          sheet_name=Config.DATA_SHEET_NAME)

        for i in excel_data_df.index:
            standard_name = self.__clean_string__(excel_data_df[Config.STANDARD_NAME_COL][i])
            if standard_name:
                fair_info = self.__get_fairness_info__(excel_data_df, i)
                standard = Standard.Standard(None, standard_name, None)
                standard.FAIRNESS_INFO = fair_info
                standards.append(standard)
        print(len(standards))
        tables = self.UTILS.get_standards_tables(standards)

        options = {
            'crop-w': '540',
        }

        for std_name, std_table in tables.items():
            std_name = self.__clean_file_name(std_name)
            file_name = "data/images/" + std_name + ".jpg"
            print("File name == " + file_name)
            imgkit.from_string(std_table, file_name, options=options)

    def generate_html_table(self):
        standards = []
        excel_data_df = pandas.read_excel(self.INPUT_FILE, header=(Config.HEADER_START_ROW - 1),
                                          sheet_name=Config.DATA_SHEET_NAME)

        for i in excel_data_df.index:
            standard_name = self.__clean_string__(excel_data_df[Config.STANDARD_NAME_COL][i])
            if standard_name:
                fair_info = self.__get_fairness_info__(excel_data_df, i)
                standard = Standard.Standard(None, standard_name, None)
                standard.FAIRNESS_INFO = fair_info
                standards.append(standard)
        print(len(standards))
        text = self.UTILS.get_standards_body(standards)
        print(text)
        f = open("data/standards.html", "w")
        f.write(text)
        f.close()

    def __get_fairness_info__(self, data_df, index):
        fair_info = FAIRNessInfo.FAIRNessInfo()

        is_standard_for_findable = self.__clean_string__(data_df[Config.FINDABLITY_FLAG_COL][index])
        if is_standard_for_findable.lower() == Config.FLAG_STRING.lower():
            fair_info.IS_FINDABLE = True

        is_standard_for_accessible = self.__clean_string__(data_df[Config.ACCESSIBLITY_FLAG_COL][index])
        if is_standard_for_accessible.lower() == Config.FLAG_STRING.lower():
            fair_info.IS_ACCESSIBLE = True

        is_standard_for_interoperable = self.__clean_string__(data_df[Config.INTEROPERABLITY_FLAG_COL][index])
        if is_standard_for_interoperable.lower() == Config.FLAG_STRING.lower():
            fair_info.IS_INTEROPERABLE = True

        is_standard_for_reusable = self.__clean_string__(data_df[Config.REUSABLITY_FLAG_COL][index])
        if is_standard_for_reusable.lower() == Config.FLAG_STRING.lower():
            fair_info.IS_REUSABLE = True

        is_standard_for_machines = self.__clean_string__(data_df[Config.MACHINES_FLAG_COL][index])
        if is_standard_for_machines.lower() == Config.FLAG_STRING.lower():
            fair_info.IS_FOR_MACHINES = True

        is_standard_for_humans = self.__clean_string__(data_df[Config.HUMANS_FLAG_COL][index])
        if is_standard_for_humans.lower() == Config.FLAG_STRING.lower():
            fair_info.IS_FOR_HUMANS = True

        is_standard_for_catalogue = self.__clean_string__(data_df[Config.FOR_CATALOGUES_FLAG_COL][index])
        if is_standard_for_catalogue.lower() == Config.FLAG_STRING.lower():
            fair_info.IS_FOR_CATALOGUE = True

        is_standard_for_database = self.__clean_string__(data_df[Config.FOR_DATABASE_FLAG_COL][index])
        if is_standard_for_database.lower() == Config.FLAG_STRING.lower():
            fair_info.IS_FOR_DATABASE = True

        is_standard_for_record_level = self.__clean_string__(data_df[Config.FOR_RECORD_FLAG_COL][index])
        if is_standard_for_record_level.lower() == Config.FLAG_STRING.lower():
            fair_info.IS_FOR_DATA_RECORD = True

        return fair_info

    def __clean_string__(self, input):
        if isinstance(input, float) and math.isnan(input):
            return ""
        input = input.strip()
        return input

    def __clean_file_name(self, input):
        input = input.strip()
        input = input.replace(" ", "_")
        input = input.replace("/", "_")
        input = input.replace("*", "")
        input = input.replace(",", "_")


        return input


test = StandardsUtils(Config.INPUT_EXCEL_FILE)
test.generate_standards_images()