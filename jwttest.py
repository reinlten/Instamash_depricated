
import jwt
encoded = jwt.encode({"some": "payload"}, "", algorithm="HS256")
print(encoded)
print(jwt.encode({"soe": "payload"}, "secret", algorithm="HS256"))
print(jwt.encode({"stp":"cp0_dst-jpg_p80x80",
                  "_nc_ohc":"JKgdTYaDn3YAX-GTA5a",
                  "_nc_ht":"scontent.fmuc4-1.fna"}, "facebook", algorithm="HS256"))


jwt.decode("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdHAiOiJjcDBfZHN0LWpwZ19wODB4ODAiLCJfbmNfb2hjIjoiSktnZFRZYURuM1lBWC1HVEE1YSIsIl9uY19odCI6InNjb250ZW50LmZtdWM0LTEuZm5hIn0.AhWIt-3ZJ-Zj4lPbxmevHMsoLU0bRkdACw25jJrDezQ", "secret", algorithms=["HS256"])