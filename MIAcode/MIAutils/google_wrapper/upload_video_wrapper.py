from upload_video import get_authenticated_service, initialize_upload, VALID_PRIVACY_STATUSES
import os
import logging
import oauth2client

class wrapperArgs():
    def __init__(self):
        self.file='./20191002_173038.mp4'
        self.title='test_title'
        self.description='test_description'
        self.keywords='test_keyword_1,test_keyword2'
        self.category='22'
        self.auth_host_port = []
    def __getattr__(self, item):
        return None


def wrapper(
        video_path,
        video_title,
        video_description,
        video_keywords='',
        video_category='22',
        ):
    """
    wrapper for uploading video with Youtube APIs
    """
    # setting arguments for running upload_video script
    try:
        args = oauth2client.tools.argparser.parse_args()
        args.file = video_path
        args.title = video_title
        args.description = video_description
        args.keywords = video_keywords
        args.category = video_category
        args.logging_level = 'INFO'
        args.privacyStatus = VALID_PRIVACY_STATUSES[0]
        logging.info(args.__dict__)
        if not os.path.exists(args.file):
            exit("Please specify a valid file using the --file= parameter.")

        youtube = get_authenticated_service(args)
        initialize_upload(youtube, args)
        return True
    except Exception as e:
        logging.error(e)
        return False

if __name__ == "__main__":
    result = wrapper( './20191002_173038.mp4','test_title','test_description' )
    print(result)
