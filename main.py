from instapy import InstaPy

session = InstaPy(username="eb3nez3r", password="##07085621im26")
session.login()

#Adding tags it should like
session.like_by_tags(["python programming language", "computer science", "programming", "No To Racism", "Black lives matter" ], amount=5)

#Adding tags it should not live 
session.set_dont_like(["naked"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(False, percentage=100)
session.end()

