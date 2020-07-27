class FileReaderService:
    @staticmethod
    def read_line(line):
        values = line.split("|")
        values = list(map(lambda value: "\"{}\"".format(value) if value != "" else "NULL", values))
        return values

    @staticmethod
    def get_professional_id(line):
        return FileReaderService.read_line(line)[1]

    @staticmethod
    def get_code_mode_exercice(line):
        code_mode_exercice = FileReaderService.read_line(line)[17]
        code_mode_exercice = code_mode_exercice.replace("\"", "")
        if code_mode_exercice == "NULL":
            return None
        return code_mode_exercice

    @staticmethod
    def convert_instance_to_line(instance):
        instance = list(map(lambda field: field if field is not None else "", instance))
        return "|".join(instance)
