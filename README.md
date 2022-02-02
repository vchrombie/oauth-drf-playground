# oauth-drf-playground

### authentication using `username` and `password`

```bash
$ curl -X POST -d "grant_type=password&username=root&password=root" -u"drYC0wA7wRlRcJSqfwTFs1ga8zEdFiE1dZtEct3n:r6XP7gRaNKEbAiZwwv749jYbqL9xXlGPY1V3LBAz8UCt1R6C8MZJAO14Ptadtt4dhJY4Qk0QTfg1t8ShHBF5J9w7t4lw5dhAHGjP0E91z9iq2I2FAMTDJrdi74UvimVt" http://localhost:8000/o/token/
{"access_token": "p5HITeM6Ulj1snEctUTPQ1fIQZPbZs", "expires_in": 36000, "token_type": "Bearer", "scope": "read write groups", "refresh_token": "2temE1W9PEHeLFh5vRb8IPahSN6xUS"}%

$ curl http://127.0.0.1:8000/users/
{"detail":"Authentication credentials were not provided."}%

$ curl -H "Authorization: Bearer p5HITeM6Ulj1snEctUTPQ1fIQZPbZs" http://127.0.0.1:8000/users/
[{"username":"root","email":"","first_name":"","last_name":""},{"username":"spiderman","email":"","first_name":"","last_name":""},{"username":"superman","email":"","first_name":"","last_name":""},{"username":"batman","email":"","first_name":"","last_name":""},{"username":"ironman","email":"","first_name":"","last_name":""},{"username":"aquaman","email":"","first_name":"","last_name":""},{"username":"gentleman","email":"","first_name":"","last_name":""}]%

$ curl -H "Authorization: Bearer p5HITeM6Ulj1snEctUTPQ1fIQZPbZs" http://127.0.0.1:8000/users/1/
{"username":"root","email":"","first_name":"","last_name":""}%

$ curl -H "Authorization: Bearer p5HITeM6Ulj1snEctUTPQ1fIQZPbZs" http://127.0.0.1:8000/groups/
[{"name":"marvel"},{"name":"dc"}]%

$ curl -H "Authorization: Bearer p5HITeM6Ulj1snEctUTPQ1fIQZPbZs" -X POST -d"username=foo&password=bar" http://localhost:8000/users/
{"username":"foo","email":"","first_name":"","last_name":""}%

$ curl -H "Authorization: Bearer p5HITeM6Ulj1snEctUTPQ1fIQZPbZs" http://127.0.0.1:8000/users/
[{"username":"root","email":"","first_name":"","last_name":""},{"username":"spiderman","email":"","first_name":"","last_name":""},{"username":"superman","email":"","first_name":"","last_name":""},{"username":"batman","email":"","first_name":"","last_name":""},{"username":"ironman","email":"","first_name":"","last_name":""},{"username":"aquaman","email":"","first_name":"","last_name":""},{"username":"gentleman","email":"","first_name":"","last_name":""},{"username":"foo","email":"","first_name":"","last_name":""}]%
```

```bash
$ curl -X POST -d "grant_type=password&username=root&password=root&scope=read" -u"drYC0wA7wRlRcJSqfwTFs1ga8zEdFiE1dZtEct3n:r6XP7gRaNKEbAiZwwv749jYbqL9xXlGPY1V3LBAz8UCt1R6C8MZJAO14Ptadtt4dhJY4Qk0QTfg1t8ShHBF5J9w7t4lw5dhAHGjP0E91z9iq2I2FAMTDJrdi74UvimVt" http://localhost:8000/o/token/
{"access_token": "RGQ84qr2btBO6jF2UrBgLO5WHsVR5E", "expires_in": 36000, "token_type": "Bearer", "scope": "read", "refresh_token": "b49H3XGZDQyjnYssHDVHO8QF3GG2YB"}%

$ curl http://127.0.0.1:8000/users/
{"detail":"Authentication credentials were not provided."}%

$ curl -H "Authorization: Bearer RGQ84qr2btBO6jF2UrBgLO5WHsVR5E" http://127.0.0.1:8000/users/
[{"username":"root","email":"","first_name":"","last_name":""},{"username":"spiderman","email":"","first_name":"","last_name":""},{"username":"superman","email":"","first_name":"","last_name":""},{"username":"batman","email":"","first_name":"","last_name":""},{"username":"ironman","email":"","first_name":"","last_name":""},{"username":"aquaman","email":"","first_name":"","last_name":""},{"username":"gentleman","email":"","first_name":"","last_name":""},{"username":"foo","email":"","first_name":"","last_name":""}]%

$ curl -H "Authorization: Bearer RGQ84qr2btBO6jF2UrBgLO5WHsVR5E" http://127.0.0.1:8000/users/1/
{"username":"root","email":"","first_name":"","last_name":""}%

$ curl -H "Authorization: Bearer RGQ84qr2btBO6jF2UrBgLO5WHsVR5E" http://127.0.0.1:8000/groups/
{"detail":"You do not have permission to perform this action."}%

$ curl -H "Authorization: Bearer RGQ84qr2btBO6jF2UrBgLO5WHsVR5E" -X POST -d"username=foo2&password=bar2" http://localhost:8000/users/
{"detail":"You do not have permission to perform this action."}%
```

### authentication using `phone_number` and `password`

```bash
$ curl http://127.0.0.1:8000/users/
{"detail":"Authentication credentials were not provided."}%

$ curl -X POST -d "grant_type=password&username=918186866445&password=root" -u"WcjI8vEyxd5lys1kMABGKwq2nb0RS9pa0vJ5JMSv:ej5sEvUm56ItCRKJLiEejUzoYFwdVBxnlzc8zH4wddFdmZdsjSFDLnd4zV1p42cHuolv3WUJlVPn7ctrRE1vuF8hDhZKT6CstrUAhn6OC5NqUeWT6Il3RicHKKYSmHQq" http://localhost:8000/o/token/
{"access_token": "pomHUrUDc7XdKmVxdZOaS9PcsehgIC", "expires_in": 36000, "token_type": "Bearer", "scope": "read write groups", "refresh_token": "iusJoz6ScPMWP4gvyYkfCrzU1eHPMn"}%

$ curl -H "Authorization: Bearer pomHUrUDc7XdKmVxdZOaS9PcsehgIC" http://127.0.0.1:8000/users/
[{"phone_number":"+918186866445","email":"","first_name":"","last_name":""},{"phone_number":"+919948241405","email":"","first_name":"","last_name":""},{"phone_number":"918186866445","email":"","first_name":"","last_name":""}]%

$ curl -H "Authorization: Bearer pomHUrUDc7XdKmVxdZOaS9PcsehgIC" http://127.0.0.1:8000/users/1/
{"phone_number":"+918186866445","email":"","first_name":"","last_name":""}%

$ curl -H "Authorization: Bearer pomHUrUDc7XdKmVxdZOaS9PcsehgIC" http://127.0.0.1:8000/groups/
[{"name":"marvel"},{"name":"dc"}]%

$ curl -H "Authorization: Bearer pomHUrUDc7XdKmVxdZOaS9PcsehgIC" -X POST -d"phone_number=919948241405&password=bar" http://localhost:8000/users/
{"phone_number":"919948241405","email":"","first_name":"","last_name":""}%

$ curl -H "Authorization: Bearer pomHUrUDc7XdKmVxdZOaS9PcsehgIC" http://127.0.0.1:8000/users/
[{"phone_number":"+918186866445","email":"","first_name":"","last_name":""},{"phone_number":"+919948241405","email":"","first_name":"","last_name":""},{"phone_number":"918186866445","email":"","first_name":"","last_name":""},{"phone_number":"919948241405","email":"","first_name":"","last_name":""}]%             
```

### rerieve only specific user items based on authentication
![Screenshot from 2022-02-02 16-53-08](https://user-images.githubusercontent.com/25265451/152144945-aefc0f66-b6ab-4480-96a4-929a873b6273.png)
![Screenshot from 2022-02-02 16-53-45](https://user-images.githubusercontent.com/25265451/152144951-aa678b6f-e579-4615-9814-1ed272c128a7.png)



