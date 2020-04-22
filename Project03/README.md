# CS 1XA3 Project03 - <fanh11>

## Usage
   - Install conda enivornment with 
   ```
   conda create -n djangoenv python=3.7
   conda activate djangoenv
   ```
   - Conda install django with
   ```
   conda install -c anaconda django
   ```
   - Run locally with
   ```
   python manage.py runserver localhost:8000
   ```
   -Run on mac1xa3.ca with
   ```
   python manage.py runserver localhost:10025
   ```
   - Log in with
   
    - Username		Password
     
    - "HaoZheng"	"#Hao123456"
    - "Noa"		"#Hao123456"
    - "David"	"#Hao123456"
    - "Yi"		"#Hao123456"
    - "WuKong"	"#Hao123456"
    - "Eugene"	"#Hao123456"
   
## Objective 01; Sign Up

 Description:
 
	- this feature is displayed in 'signup.djhtml' which is rendered by 
	  'signup_view'
	- provides a form for users to enter their username and password  
	- creates a new UserInfo entry from the POST request sent by the 
	  UserCreationform
	- automatically logs the new user in and redirects to the message page
	
 Exception:
 
	- If the following situation occur, new UserInfo object will not be 
	  created and the 'sign up' page will be reloaded:
		- username and/or password and/or confirm password are not entered
		- username and/or password do not meet the criteria
		- password and confirm password do not match
		- username already exist
		
## Objective 02; User Profile & Interest Display

 Description:
 
	- this feature is displayed in 'social_base.djhtml' which renders the
	  left_column used by 'message.djhtml', 'people.djhtml' and 'account.djhtml'
	- displays the profile (e.g. Employment, Location and Birthday) and the 
	  interests of the currently logged in user by using Django Template 
	  Variable
	  
 Exception:
 
	- If the user is not authenticated, it redirects to the 
	  'login' page
	  
## Objective 03; Account Settings Page

 Description:
 
	- this feature is displayed in 'account.djhtml' which is rendered by
	  'account_view'
	- provides forms for users to change their passwords, edit their profiles
	  and interests
	- changes and saves the user's new password from the POST request sent 
	  by the PasswordChangeForm. After the password is changed, it redirects
	  to the 'login' page
	- changes and saves the user's new profile from the POST request sent 
	  by the UserInfoForm - a custom form created in 'soical/models.py'
	- adds a new interest to the user's interests list from the POST 
	  request sent by the form  
	- deletes an interest from the user's interests list. This process starts
	  by clicking an interest button in the delete interest section, 
	  a POST request is then sent to the function 'deleteInterest' in 'account.js' to 
	  '/e/fanh11/interestdelete' which is handled by 'interest_delete_view'.
	  The call back function 'delIntReponse' then reloads the page 
	  
 Exception:
 
	- if the user is not authenticated, it redirects to the 'login'
	  page
	  
## Objective 04; Displaying People List

 Description:
 
	- this feature is displayed in 'people.djhtml' which is rendered by 
	  'people_view'
	- displays actual Users in the middle column who are not friend of 
	  the current user
	- only one User is displayed initially. once the 'More' button is 
	  clicked, a POST request is sent to from the function 'submitMorePpl' in 'people.js' 
	  to '/e/fanh11/moreppl' which is handle by 'more_ppl_view'. The call 
	  back function 'morePplResponse' then reloads the page
	- the 'more_ppl_view' function increments the "request.session['count']"
	  key by one which allows the 'people_view' page to display one more User
	- the "request.session["count"]" is initialized in 'people_view' and it 
	  is reseted to 1 after the user logged out
	  
 Exception:
 
	- if the user is not authenticated, it redirects to the 'login_view'
	  page
	- if the status after clicking the 'More' button is not equal to 'success',
	  an alert message will be displayed
	  
## Objective 05; Sending Friend Requests

 Description:
 
	- this feature is displayed in 'people.djhtml' which is rendered by
	  'people_view'
	- when a 'Friend Request' button is clicked, its id which contains the
	  person's username is sent from the function 'friendRequest' in 'people.js' 
	  to '/e/fanh11/friendrequest' which is handle by 'friend_request_view'.
	  The call back function 'frResponse' then reloads the page
	- the function 'friend_request_view' handle the POST by inserting a new entry to the 
	  FriendRequest model with 'to_user' being assigned to the person and 
	  'from_user' being assigned to the current logged in user
	- displays a list of friend requests sent to the current user on 
	  right column of 'people.djhtml'
	  
 Exception:
 
	- if the user is not authenticated, it redirects to the 'login_view'
	  page
	- if the '/e/fanh11/friendrequest' is called without arguments, a 404
	  error message will be displayed
	- if the status after clicking the 'Friend Request' button is not equal
	  to 'success', an alert message will be displayed
	- if the same 'Friend Request' button is clicked more than once, new 
	  entries to FriendRequest model will not be created
	  
## Objective 06; Accepting/Declining Friend Requests

 Description:
 
	- this feature is displayed in 'people.djhtml' which is rendered by
	  'people_view'
	- when the accept button (green) is clicked, its id containing the 
	  the person's username with an "A-" prefix is sent from the function 
	  'acceptDeclineRequest' in 'people.js' to '/e/fanh11/acceptdecline' 
	  which is handled by 'accept_decline_view'. The call back function
	  'adResponse' then reloads the page
	- the 'accept_decline_view' function handles the POST by deleting
	  the corresponding FriendRequest entry, and updating both Users friends 
	  relation in the UserInfo table if the POST data has a "A-" as its prefix   
	- when the decline button (red) is clicked, its id containing the
	  the person's username with a "D-" prefix is sent from the function 'acceptDeclineRequest' to
	  '/e/fanh11/acceptdecline'. The 'accept_decline_view' function 
	  handlesthe POST by deleting the corresponding FriendRequest entry. The call back function
	  'adReponse' then reloads the page 
	  
 Exception:
 
	- if the user is not authenticated, it redirects to the 'login_view'
	  page
	- if the status after clicking the accept/decline button is not equal
	  to 'success', an alert message will be displayed
	- if '/e/fanh11/acceptdecline' is called without arguments, a 404 error
	  message will be displayed
	  
## Objective 07; Displaying Friends

 Description:
 
	- this feature is displayed by 'messages.djhtml' which is rendered by
	  'message_view'
	- displays a list of current user's friends on the right column of 
	  'messages.djhtml'
	  
 Exception:
 
	- if the user is not authenticated, it redirects to the 'login_view'
	  page
	  
## Objective 08; Submitting Posts

 Description:
 
	- this feature is displayed by 'messages.djhtml' which is rendered by
	  'message_view'
	- provides a text field (id - 'post-text') and button (id - 'post button')
	  for submitting posts
	- when the 'Post' button is clicked, the content of 'post-text' is sent
	  from the function 'submistPost' in 'message.js' to '/e/fanh11/postsubmit' 
	  which is handled by 'post_submit_view'. The call back function 'subResponse'
	  then reloads the page
	- the 'post_submit_view' function handles the POST by adding a new entry to
	  the Post model
	  
 Exception:
 
	- if the user is not authenticated, it redirects to 'login_view' page
	- if '/e/fanh11/postsubmit' is called without arguments, a 404 error
	  message will be displayed
	- if the status after clicking the 'Post' button is not equal 'success',
	  an alert message will be displayed
	  
## Objective 09; Displaying Post List

 Description:
 
	- this feature is displayed by 'messages.djhtml' which is rendered by 
	  'message_view'
	- displays a list of posts in the middle column of 'messages.djhtml'
	  sorted from newest to oldest
	- only 2 posts are displayed initially, once the 'More' button is clicked,
	  a POST request is sent from the function 'submitMore' in 'messages.js' 
	  to '/e/fanh11/morepost' which is handled by 'more_post_view'. The call
	  back function 'moreResponse' then reloads the page
	- the 'more_post_view' functino handles the POST by incrementing the 
	  'request.session['pcount']' key by 1 which allows the 'message_view'
	  page to display 1 more post
	- the 'reqeust.seesion['pcount']' is initialized in 'message_view' and
	  it is reseted to 2 after the user logged out
	  
 Exception:
 
	- if the user is not authenticated, it redirects to 'login_view' page
	- if the status after clicking the 'More' button is not equal to 
	  'success', an alert message will be displayed
	  
## Objective 10; Liking Posts (and Displaying Like Count)

 Description:
 
	- this feature is displayed by 'messages.djhtml' which is rendered by
	  'message_view'
	- when the 'like' button of a post is clicked, its id containing the 
	  post's id is sent from the function 'submitLike' in 'message.js' to 
	  '/e/fanh11/like' which is handled by 'like_view'. The call back 
	  function 'subLikeResponse' then reloads the page
	- the 'like_view' function handles the POST by adding a new UserInfo 
	  object to the 'likes' attribute of the corresponding post object
	- disables the 'like' button of a post for the user after he/she clicked
	  it once
	- diplays the number of likes of a post based on the number of users 
	  who clicked its 'like' button
	  
 Exception:
 
	- if the user is not authenticated, it redirects to the 'login_view' page
	- if '/e/fanh11/like' is called without arguments, a 404 error message will
	  be displayed
	- if the status after clicking the 'like' button is not equal to 'success',
	  an alert message will be displayed

 
	  
	  
