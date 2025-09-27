'''
a simple file system with add, remove, show functionality.
'''

class FileSystem:
    def __init__(self):
        self.root = {}

    def add_file(self, file_path, content):
        '''
        e.g. file_path = /home/user/file.txt, content = "hello world"
        '''
        parts = file_path.strip('/').split('/')  # strip leading '/', split by '/'
        current = self.root
        for part in parts[:-1]:  # traverse to the directory
            if part not in current:
                current[part] = {}
            current = current[part]
        
        if parts[-1] in current:
            raise Warning(f"File {file_path} already exists. Overwriting.")
        current[parts[-1]] = content  # add the file with content

    def remove_file(self, file_path):
        '''
        e.g. file_path = /home/user/file.txt
        '''
        parts = file_path.strip('/').split('/')
        current = self.root
        for part in parts[:-1]:  # traverse to the directory
            if part not in current:
                raise FileNotFoundError(f"Directory {part} does not exist.")
            current = current[part]
        
        if parts[-1] not in current:
            raise FileNotFoundError(f"File {file_path} does not exist.")
        del current[parts[-1]]  # remove the file

    def show_file(self, file_path):
        parts = file_path.strip('/').split('/')
        current = self.root
        for part in parts[:-1]:  # traverse to the directory
            if part not in current:
                raise FileNotFoundError(f"Directory {part} does not exist.")
            current = current[part]
        if parts[-1] not in current:
            raise FileNotFoundError(f"File {file_path} does not exist.")
        return current[parts[-1]]  # return the file content
    
    def rename(self, old_path, new_path):
        content = self.show_file(old_path)  # get content of old file
        self.add_file(new_path, content)  # add new file with same content
        self.remove_file(old_path)  # remove old file

    def move(self, old_path, new_dir):
        parts = old_path.strip('/').split('/')
        file_name = parts[-1]
        new_path = f"{new_dir.rstrip('/')}/{file_name}"
        self.rename(old_path, new_path)

    def list_files_recursive(self):
        '''
        List all files in the filesystem recursively.
        '''
        def recurse(current, path):
            files = []
            for name, item in current.items():
                if isinstance(item, dict):
                    files.extend(recurse(item, f"{path}/{name}"))
                else:
                    files.append(f"{path}/{name}")
            return files
        
        return recurse(self.root, '')

    
if __name__=='__main__':
    fs = FileSystem()
    fs.add_file('/home/user/file.txt', 'hello world')
    print(fs.show_file('/home/user/file.txt'))  # should print 'hello world'
    fs.remove_file('/home/user/file.txt')
    try:
        print(fs.show_file('/home/user/file.txt'))  # should raise FileNotFoundError
    except FileNotFoundError as e:
        print(e)