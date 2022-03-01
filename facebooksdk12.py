

# facebook-sdk is a python library for the Facebook Graph API.
# code example
import facebook as fb
import json
def main():
    token = "EAAGWibRZAzKQBABGfMa1RhjSEZB9gKjANdZCxNtoIWDyNJQWw2wILSFerk25cG6GrxSg460VqQE0ZBT7gA2QwqLZBoDwDSagEyIuQ96ahq7zHQQj7hd71tdRAY7lZBZCAN6M1yJfiZBpx5c3vwx8edv1ioRsgGjXiwCT6EDiB0lssyZBwbBfHEXGi2M1YKZBA7VZAGiW3fMmgbQugZDZD"
    asafb = fb.GraphAPI(token)
#fields = ['first_name', 'location{location}','email','link']
    profile = asafb.get_object('me',fields='first_name,location,link,email')
#return desired fields
    print(json.dumps(profile, indent=4))

    # post a message in the facebok
    asafb.put_object("me", "feed", message="hello this amazing technology")
    # get a message in the facebook page

    asafb.get_object("id that was generated")
    fb.put_like("my page id _my post id")

    # post  PHOTO WITH CAPTIONS
    asafb.put_photo(open("name.jpg", "rb"), message="automated message")

if __name__ == '__main__':
	main()