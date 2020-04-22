from django.http import HttpResponse,HttpResponseNotFound, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from . import models

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
    	user_info = models.UserInfo.objects.get(user=request.user)
    	pcount = request.session.get("pcount",2)
    	request.session["pcount"] = pcount
    	# TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
    	posts = [post for post in models.Post.objects.all().order_by('-timestamp')][:request.session["pcount"]]
    	# TODO Objective 10: check if user has like post, attach as a new attribute to each post
    	context = { 'user_info' : user_info, 'posts' : posts }
    	return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
    if request.user.is_authenticated:
    	user_info = models.UserInfo.objects.get(user=request.user)

    	if request.method == 'POST':

    		pswdc_form = PasswordChangeForm(user_info.user, request.POST)
    		if pswdc_form.is_valid():
    			user = pswdc_form.save()
    			update_session_auth_hash(request, user)
    			return redirect('login:login_view')

    		update_form = models.UserInfoForm(request.POST,instance=user_info)
    		if update_form.is_valid():
    			user_info.employment = update_form.cleaned_data.get('employment')
    			user_info.location = update_form.cleaned_data.get('location')
    			user_info.birthday = update_form.cleaned_data.get('birthday')
    			user_info.save()
    			return redirect('social:account_view')

    		interest = request.POST.get('interest')
    		if interest:
    			Int_db = models.Interest(label=interest)
    			Int_db.save()
    			aInt = models.Interest.objects.get(label=interest)
    			user_info.interests.add(aInt)
    			return redirect('social:account_view')
    		else:
    			messages.error(request, "Please enter an interest.")
    			return redirect('social:account_view')

    	else:
    		update_form = models.UserInfoForm(instance=user_info)
    		pswdc_form = PasswordChangeForm(request.user)

    	# TODO Objective 3: Create Forms and Handle POST to Update UserInfo / Password

    	context = { 'user_info' : user_info, 'pswdc_form' : pswdc_form, 'update_form' : update_form}
    	return render(request,'account.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
    	user_info = models.UserInfo.objects.get(user=request.user)
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)
    	count = request.session.get('count',1)
    	request.session['count'] = count 
    	all_people = [auser for auser in models.UserInfo.objects.exclude(user=user_info) if user_info not in auser.friends.all()][:request.session['count']]

        # TODO Objective 5: create a list of all friend requests to current user
    	friend_requests = [friend for friend in models.FriendRequest.objects.filter(to_user=user_info)]
    	context = { 'user_info' : user_info,
                    'all_people' : all_people,
                    'friend_requests' : friend_requests }

    	return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    if postIDReq is not None:
    	# remove 'post-' from postID and convert to int
    	# TODO Objective 10: parse post id from postIDReq
    	postID = int(postIDReq[5:])
    	if request.user.is_authenticated:
    		user_info=models.UserInfo.objects.get(user=request.user)
    		liked = False
    		post = models.Post.objects.get(pk=postID)
    		for x in post.likes.all():
    			if x.user.username == user_info.user.username:
    				liked = True
    				break
    		if not liked:
    			post.likes.add(user_info)
    			data = {'postID':postIDReq}
    			return JsonResponse(data)
    		# TODO Objective 10: update Post model entry to add user to likes field
    		# return status='success'
    		return HttpResponse()
    	else:
    		return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    if postContent is not None:
    	if request.user.is_authenticated:
    		user_info = models.UserInfo.objects.get(user=request.user)
    		post = models.Post(owner=user_info, content=postContent)
    		post.save()
    		# TODO Objective 8: Add a new entry to the Post model
    		# return status='success'
    		return HttpResponse()
    	else:
    		return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
    	all_post=models.Post.objects.all().count()
    	if request.session['pcount']<all_post:
    		request.session['pcount'] += 1
    	# update the # of posts dispalyed
    	# TODO Objective 9: update how many posts are displayed/returned by messages_view
    	# return status='success'
    	return HttpResponse()

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
    	user_info = models.UserInfo.objects.get(user=request.user)
    	all_ppl = len([auser for auser in models.UserInfo.objects.exclude(user=user_info) if user_info not in auser.friends.all()])
    	if request.session['count'] < all_ppl:
    		request.session['count'] += 1

        # update the # of people dispalyed

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed

        # return status='success'
    	return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
    	username = frID[3:]
    	if request.user.is_authenticated:
    		user_info = models.UserInfo.objects.get(user=request.user)
    		friend_info = models.UserInfo.objects.get(user__username=username)
    		fri_request = False
    		for afr in models.FriendRequest.objects.all():
    			if afr.to_user.user.username == friend_info.user.username:
    				fri_request = True
    				break
    		if not fri_request:
    			# TODO Objective 5: add new entry to FriendRequest
    			fr = models.FriendRequest(to_user=friend_info,from_user=user_info)
    			fr.save()
    			data = { 'frID' : frID }
    			# return status='success'
    			return JsonResponse(data)
    		return HttpResponse()
    	else:
    		return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    if data is not None:
        # TODO Objective 6: parse decision from data
    	decision = data[0]
    	fname = data[2:]

    	if request.user.is_authenticated:
    		# TODO Objective 6: delete FriendRequest entry and update friends in both Users
    		fr_entry = models.FriendRequest.objects.filter(from_user__user__username=fname)
    		fr_entry.delete()
    		if decision == 'A':
    			user_info = models.UserInfo.objects.get(user=request.user)
    			friend_info = models.UserInfo.objects.get(user__username=fname)
    			user_info.friends.add(friend_info)
    			friend_info.friends.add(user_info)
    		# return status='success'
    		return HttpResponse()
    	else:
    		return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')

def interest_delete_view(request):
    interest = request.POST.get('interest')
    if interest is not None:
    	if request.user.is_authenticated:
    		user_info = models.UserInfo.objects.get(user=request.user)
    		inter_del = user_info.interests.get(label=interest[9:])
    		inter_del.delete()
    		return HttpResponse()
    	else:
    		return redirect('login:login_view')
    return HttpResponseNotFound('interest_delete_view called without decision in POST')

