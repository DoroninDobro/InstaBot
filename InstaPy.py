from instapy import InstaPy

session = InstaPy(username="vovka_dobro", password="Doronin7")#, headless_browser=True)
session.login()
session.set_quota_supervisor(enabled=True, peak_comments_daily=40, peak_comments_hourly=5)
session.like_by_tags(["love", "bodypositive"], amount=1) 
session.set_dont_like(["war"])
session.set_do_follow(True, percentage=50)
session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
# session.set_do_comment(True, percentage=50)
# session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
# session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=20)
session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=False,
                       no_profile_pic_percentage=100,
                       skip_business=False,
		                   skip_non_business=False,
                       business_percentage=100,
                       skip_business_categories=[],
                       dont_skip_business_categories=[])
session.set_relationship_bounds(enabled=True,
				       potency_ratio=1.34,
				       delimit_by_numbers=True,
				       max_followers=8500,
				       max_following=4490,
				       min_followers=100,
				       min_following=56,
				       min_posts=10,
               max_posts=1000)
session.accept_follow_requests(amount=100, sleep_delay=1)
session.end()
