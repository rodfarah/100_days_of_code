import cookie_and_store as cas
import time


cookie = cas.Cookie()
store = cas.Store()

ZERO = time.time()
first_time = time.time()
check_store_each = 5
game_over_after = 60 * 5

while first_time < ZERO + game_over_after:
    cookie.click_on_cookie()
    second_time = time.time()
    if second_time - first_time >= check_store_each:
        first_time = second_time
        score = cas.get_score()
        store.generate_dict_click_element(score)
        

print(cas.cookies_per_second())
