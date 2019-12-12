from upload_video import get_authenticated_service, initialize_upload
import os

class wrapperArgs():
    def __init__(self):
        self.file='./20191002_173038.mp4'
        self.title='test_title'
        self.description='test_description'
        self.keywords='test_keyword_1,test_keyword2'
        self.category='22'

def wrapper(args):
    """
    wrapper for uploading video with Youtube APIs
    """
    print(args.__dict__)
    if not os.path.exists(args.file):
        exit("Please specify a valid file using the --file= parameter.")

    youtube = get_authenticated_service(args)
    initialize_upload(youtube, args)

if __name__ == "__main__":
    test_args =wrapperArgs()
    wrapper(test_args)
