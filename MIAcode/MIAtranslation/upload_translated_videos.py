"""
some ideas here

- will YouTube kill us?
- is there a public api?
"""
import logging

def upload_translated_videos(**kwargs):
    """
    upload videos from local .mp4 files
    """
    task_instance = kwargs['ti']
    generated_video_path = task_instance.xcom_pull(
            key=None, 
            task_ids='translate_scripts') 
    logging.info("retrieved generated_video_path from xcom_pull")
    logging.info(generated_video_path)

    ## TODO (ALEX)
    # given local path upload videos on youtube 
    # and update video link

