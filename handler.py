# Import JSON Web Token from jose for Encode / Decode function
# Import datatime for epoch time conversion
from jose import jwt
import datetime

def handler(context, inputs):
    # 'iat' is the current epoch time as a whole number
    current = datetime.datetime.now()
    iat = int(current.timestamp())

    # 'exp' is the current epoch time plus 60 minutes, as a whole number
    expiry = current + datetime.timedelta(seconds=3600)
    exp = int(expiry.timestamp())

    # Set the 'headers' to include the 'kid' value to match your 'private_key_id' from the Service Account JSON file
    headers = { "alg": "RS256", "typ": "JWT", "kid": "9f94a655fb7803596886737a96e44032cbd00645" }

    # Set the 'payload' to include the 'iss' and 'sub' values to match your 'client_email' from the Service Account JSON file
    # In the 'payload', update the 'scope' url to limit the permissions for the Auth Code
    payload =   { "iss": "svc-vra8-db@dev1-iaas-playground-9e0c.iam.gserviceaccount.com",
                "sub": "svc-vra8-db@dev1-iaas-playground-9e0c.iam.gserviceaccount.com",
                "aud": "https://www.googleapis.com/oauth2/v4/token",
                "scope": "https://www.googleapis.com/auth/compute",
                "iat": iat,
                "exp": exp }
    
    # Set the 'private_key' to match the value of your 'private_key' in your Service Account JSON file
    private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDEZ86eyfwuAQuT\nXSWh7xZNaO4W+v5P+KScQ4RfFKHBCl1karGcu9WcUgyJezEqxZXSJtN96CHskV53\niUQFgnRpe8YVTF1hDTn1N+7thqn1ldrjAYqmzn7fIljhuNotzZR4LWwn6W6j6p7n\nfCsRY3EKK3Iew0nlh+KdTlgShO5RwibGUoU3vFkMSx8Auc6Y8tSGOch0G2m7d9pM\n2UdAKCkoW1pyiaJaIwpYrweKFMSMFAkHI8+leJGz6K7hvsA55zdr2Z34HhEq87cc\nouFHyxCZOMEyD7rYKc9plh+Mr8zEUft1iFYfEkryA7h+ZR/Cf3h3iTUwNYD3B6AI\n58mS5XX9AgMBAAECggEAEwgWEvfymkiapQx1HZRr3lNpIsvugbRPyx6VwJrgs7J7\n60OVc2EWKWAf++B2mrTruCHwA3bPdrt9YmroLvp9qk0GnEC6mbFs6NCjM9wFMxly\nzOV02IYQ8DFFWJYPejm+Bcks/k8V3Adbn4W+LKCsrvYXyFhXHElHEcQqL5029LAG\nmfqUok6yNxM/eBIsnWhcV4HI66cXEKz3OvnNjTHYPhiYsvNEcPaBwzhq67nwXwUY\nl8AHii+GQW+Clt8pGM9I/9yhOj5uI7px6r+1QOej+cqjMkXg5pBgEgPQ959LRQes\nr7KT8MN+LfqTDgYSFlV7Xv4MlGzaCCjwtS+Bq4j7FwKBgQDgSCwCHEcmHSlNBx1Z\nKrhy6f90GNy7qL2O+I3aY4P6Leropng4SygkQCqUTIZJXerLSfBJ6u9MF2egEz+q\nqydeAoQN8e+Azm2B4gqZ/GV3voadJ4tf/YjM9Anv3JrZm6XoC7dhYe69F6iMIHEg\nAKPhFZKGbw8Q89A5pDOKHu3KBwKBgQDgLmgIzkmpTHm9ClW0O6hsIxDPsV7cMwQm\nNFigUemaWeJF6nbnUW+nHp4K3hBH/Grst/SvTTVDt+Khqs93mNouOLaHbDRkxypp\ngWW/YPfK53MxxVbGgktxQrLoDmagOXbbBbYfecfTsbtV8dT0WlWWMctTC9SbOfDW\n6yzyedjO2wKBgA/LJUY0xZHahdkFwjxQNNLqxXFgetLALDEQMbUKQvXwG9WsO1UD\nfd0no5fz15T9BxavqzsZTyaVk1eDY31aNhh5puDwg4QXhUCbMVHsoxyOjx4r9bWZ\nvfNoz/ZTG5htTH6NrKkv40bvjo/njO/K+79S7JGI6o+wC56zgGmeifIrAoGAPE2f\nZIcBH45XzPcjuLi3hGcmVYgTyU3b1t8L3AxMt11oVYBNfcnVK/I7dxbm8EZBCO4u\n3pz5L/8d8nj9F+HBBt/wkZsUuOsuSHUrRoCyBx2dSg0YW4ue+ZeEgpGlH4J1q1Ls\n+6iJjTNo/iRwMU6/aQh59hvfk+XRGC7ox0zpejMCgYEAxCiaMoJxjyqUWV9HIjzN\ncr4dUyrvZznBNNz5y6ar1ILtIa/5zwH00sIUPukXsu5H8rsGn+2FlL6uicwzUU7B\n9pTRQ0LWflaQbmS26OC/KM4GwuvCj5x1zQn2AIQ5Jg0dNEbqCQvsuix+MUSijQtv\n9PHXk4+fRBX8kfGfwCm7Qv8=\n-----END PRIVATE KEY-----\n"

    # Encode the 'payload' and 'headers' against the 'private_key' and return the Authorization Code
    auth_code = jwt.encode(payload, private_key, algorithm='RS256', headers=headers)

    # Return the Authorization Code
    return auth_code