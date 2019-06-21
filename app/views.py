from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomRegisterForm
from .models import Placement, PlacementBid, Bid
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    else:
        form = CustomRegisterForm()
    
    context = {'form': form}

    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('app:home')
        else:
            return render(request, 'login.html') 
            
    else:
        return render(request, 'login.html') 


def logout(request):
    auth_logout(request)
    return redirect('app:login')


def home(request):

    return render(request, 'home.html')


@login_required
def placements(request):
    
    placements = Placement.objects.all()

    context = {'placements': placements}

    return render(request, 'placements.html', context)


@login_required
def placement_detail(request, placement_slug):

    placement = get_object_or_404(Placement, placement_slug=placement_slug)

    if request.method == 'POST':
        submitted_quantity = request.POST.get('quantity')
        submitted_amount = request.POST.get('amount')

        # Create or store Bid object based on conditional
        bid_queryset = Bid.objects.filter(user=request.user, bid_status=False)
        
        if bid_queryset.exists():
            bid = bid_queryset[0]
        else:
            bid = Bid.objects.create(user=request.user)
        
        # Create PlacementBid given the above objects
        placement_bid = PlacementBid.objects.create(user=request.user, 
                                                    placement=placement, 
                                                    bid=bid,
                                                    offer=submitted_amount,
                                                    shares=submitted_quantity)
        return redirect('app:home')

    context = {'placement': placement}

    return render(request, 'placement_detail.html', context)


@login_required
def bid_summary(request):

    bids = PlacementBid.objects.filter(user=request.user)

    context = {'bids': bids}

    return render(request, 'bid-summary.html', context)



@login_required
def confirm_bids(request):

    bids_queryset = PlacementBid.objects.filter(user=request.user, confirmed=False)
    
    if bids_queryset.exists():

        # First get the order ID
        bid_id = bids_queryset[0].bid.id

        # Update PlacementBid Objects confirmed flag
        for bid in bids_queryset:
            bid.confirmed = True
            bid.save()
        
        # Update the Bid object status
        bid = Bid.objects.filter(id=bid_id)[0]
        bid.bid_status = True
        bid.save()

    return redirect('app:bid-summary')
