
class Open:
    """
    This class will open the file on the path passed and provide users
    with function to manipulate and modify the file.
    """

    def __init__(self, path, data):
        self.data = data
        self.path = path
        self.page_length = 4096
        self.first_free_frame = len(data['frames'])

        if self.path in data['process']:
            self.exists = True
            self.process = data['process'][self.path]
        else:
            self.exists = False
            self.process = []

        # print(self.process)

    def write_to_file(self, text, write_at=None):
        pages_left = self.get_page(text)
        text_start_idx = 0

        if write_at is None:
            new_text = self.read_from_file()
            for i in self.process[:]:
                # print(i)
                self.process.remove(i)
                del self.data['frames'][i]
                self.data['clear'] += [i]

            text = new_text + text
            pages_left = self.get_page(text)

            if len(self.data['clear']) > 0 and pages_left > 0:
                for c in self.data['clear'][:]:
                    self.data['frames'][int(c)] = text[text_start_idx:
                                                  text_start_idx + self.page_length]
                    self.process += [int(c)]
                    text_start_idx = text_start_idx + self.page_length
                    pages_left = pages_left - 1
                    self.data['clear'].remove(c)

                    if pages_left == 0:
                        break

            if pages_left > 0:
                for i in range(pages_left):
                    self.data['frames'][self.first_free_frame] = text[text_start_idx:
                                                                      text_start_idx + self.page_length]
                    text_start_idx = text_start_idx + self.page_length
                    self.process += [self.first_free_frame]
                    self.first_free_frame = self.first_free_frame + 1

        else:
            newText = self.read_from_file()
            newText = newText[:write_at] + text
            process_len = len(self.process)
            for i in self.process[:]:
                self.process.remove(i)
                del self.data['frames'][i]
                self.data['clear'] += [i]
            
            target_page = -(-write_at // self.page_length)
            if target_page > process_len:
                print('write_to_file(): write_at is invalid and out of bound')
            else:
                pages_left = self.get_page(newText)

                if len(self.data['clear']) > 0 and pages_left > 0:
                    for c in self.data['clear'][:]:
                        self.data['frames'][int(c)] = newText[text_start_idx:
                                                         text_start_idx + self.page_length]
                        self.process += [int(c)]
                        text_start_idx = text_start_idx + self.page_length
                        pages_left = pages_left - 1
                        self.data['clear'].remove(c)

                        if pages_left == 0:
                            break

                if pages_left > 0:
                    for i in range(pages_left):
                        self.data['frames'][self.first_free_frame] = newText[text_start_idx:
                                                                             text_start_idx + self.page_length]
                        text_start_idx = text_start_idx + self.page_length
                        self.process += [self.first_free_frame]
                        self.first_free_frame = self.first_free_frame + 1

    def read_from_file(self, start=None, size=None):
        text = ''

        if start is None and size is None:
            for i in self.process:
                text += self.data['frames'][i]
        else:
            for i in self.process:
                text += self.data['frames'][i]
            text = text[start:start + size]
        return text

    def move_within_file(self, start, size, target):
        pass

    def truncate_file(self, max_size):
        pass

    def get_page(self, text):
        return -(-len(text) // self.page_length)

    def close(self):
        self.data['process'][self.path] = self.process
        return self.data
