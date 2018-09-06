# Sample python code for videoCategories.list

import os.path
import gdata.data
import gdata.acl.data
import gdata.docs.client
import gdata.docs.data
import gdata.sample_util





def video_categories_list_for_region(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.videoCategories().list(
    **kwargs
  ).execute()

  return print_response(response)

video_categories_list_for_region(client,
    part='snippet',
    hl='es',
    regionCode='ES')


if __name__ == '__main__':
    client = 