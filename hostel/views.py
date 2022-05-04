from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import registerHostelForm, registerBlockForm
from .models import hostel, hostel_block
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.


def register_hostel(request):

    form = registerHostelForm(request.POST)
    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, " New hostel has been added successful")

        return redirect('register_hostel')

    return render(request, 'hostel/register_hostel.html', {'form':form})


def view_hostel(request):

    htl = hostel.objects.all()

    context = {

        'hostel': htl,
    }
    return render(request, 'hostel/hostel.html', context)


@login_required
def register_hostel_block(request):

    form = registerBlockForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            form.save
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, "New hostel block has been added successfully")

            return redirect('register_block')

    return render(request, 'hostel/register_block.html', {'form':form})


@login_required
def view_hostel_blocks(request):

    view_htl_block = hostel_block.objects.all()

    context = {
        'hostel_block': view_htl_block
    }

    return render(request, 'hostel/view_blocks.html', context)
    

@login_required
def update_hostel(request, hostel_id):
    students_hostel = hostel.objects.get(pk=hostel_id)
    form = registerHostelForm(request.POST or None, instance=students_hostel)
    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, " hostel has been updated successful")

        return redirect('hostel-list')
    
    context = {
        'form':form,
    }

    return render(request, 'hostel/update_hostel.html', context)


@login_required
def delete_hostel(request, hostel_id):
    hostel_del = hostel.objects.get(pk=hostel_id)
    hostel_del.delete()
    return redirect('hostel-list')


@login_required
def update_block(request, hostel_block_id):
    students_block = hostel_block.objects.get(pk=hostel_block_id)
    form = registerBlockForm(request.POST or None, instance=students_block)
    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, " hostel Block has been updated successful")

        return redirect('Blocks-list')
    
    context = {
        'form':form,
    }

    return render(request, 'hostel/update_block.html', context)


@login_required
def delete_block(request, hostel_block_id):
    hostel_block_del = hostel_block.objects.get(pk=hostel_block_id)
    hostel_block_del.delete()
    return redirect('blocks-list')