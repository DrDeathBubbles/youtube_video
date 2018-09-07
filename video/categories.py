# Sample python code for videoCategories.list

import os.path
import gdata.data
import gdata.acl.data
import gdata.docs.client
import gdata.docs.data
import gdata.sample_util


#  """Create a Documents List Client."""
#  client = gdata.docs.client.DocsClient(source=SampleConfig.APP_NAME)
#  client.http_client.debug = SampleConfig.DEBUG
#  # Authenticate the user with CLientLogin, OAuth, or AuthSub.
#  try:
#    gdata.sample_util.authorize_client(
#        client,
#        service=client.auth_service,
#        source=client.source,
#        scopes=client.auth_scopes
#    )
#  except gdata.client.BadAuthentication:
#    exit('Invalid user credentials given.')
#  except gdata.client.Error:
#    exit('Login Error')
#  return client







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