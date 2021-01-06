class Tania:
    file = ""
    file_content = []

    def __init__(self, file, interval = None):
        pointer = 1
        self.file = file

        # File management
        packet = open(file, 'r')
        packet_content = packet.readlines()
        packet.close()

        # If None return everything
        if interval == None:
            self.file_content = packet_content

        # If Tuple return everything between
        elif type(interval) == type((2,5)):
            for i in packet_content:
                if pointer >= interval[0] and pointer <= interval[1]:
                    self.file_content.append(i)
                pointer += 1

        # If Int return that one file
        elif type(interval) == type(1):
            self.file_content.append(packet_content[interval - 1])

        # Save memory
        del pointer
        del packet
        del packet_content

    def find_by_tag(self, tag, to_return = None):
        for i in self.file_content:
            if i.split(';')[0] == tag:
                if to_return == None:
                    return i
                elif to_return == "data":
                    return i.split(';')[1]

    def add_data(self, tag, data):
        # Get file content
        file = open(self.file, "r")
        file_data = file.read()
        file.close()

        tag_list = []
        for i in self.file_content:
            tag_list.append(i.split(";")[0])

        if not tag in tag_list:

            file = open(self.file, "w")

            line = tag + ";" + data
            file_data += "\n" + line
            self.file_content.append(line)
            file.write(file_data)
            file.close()