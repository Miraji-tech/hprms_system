from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import registerHostelForm, registerBlockForm, registerRoomForm, allocateBlockForm, allocateRoomForm
from .models import allocate_block, allocate_room, hostel, hostel_block, room
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
def register_room(request):

    form = registerRoomForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            form.save
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, "New room has been added successfully")

            return redirect('register-room')

    return render(request, 'hostel/register_room.html', {'form':form})


@login_required
def view_rooms(request):

    view_room_block = room.objects.all()

    context = {
        'room': view_room_block
    }

    return render(request, 'hostel/rooms.html', context)


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


@login_required
def update_room(request, room_id):
    students_room = room.objects.get(pk=room_id)
    form = registerRoomForm(request.POST or None, instance=students_room)
    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, " Room has been updated successful")

        return redirect('rooms-registered')
    
    context = {
        'form':form,
    }

    return render(request, 'hostel/update_room.html', context)


@login_required
def delete_room(request, room_id):
    room_del = room.objects.get(pk=room_id)
    room_del.delete()
    return redirect('rooms-registered')


@login_required
def allocate_room_student(request):

    form = allocateRoomForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            form.save
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, "A student has allocated a room successfully")

            return redirect('allocate-student-room')

    return render(request, 'hostel/allocate_student.html', {'form':form})


@login_required
def allocate_block_warden(request):

    form = allocateBlockForm(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            form.save
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            messages.success(request, "A warden has allocated a block successfully")

            return redirect('allocate-warden-block')

    return render(request, 'hostel/allocate_warden.html', {'form':form})


@login_required
def view_student_allocation(request):

    view_st_room = allocate_room.objects.all()

    context = {
        'allocate_room': view_st_room
    }

    return render(request, 'hostel/student_allocation.html', context)


@login_required
def view_warden_allocation(request):

    view_wd_block = allocate_block.objects.all()

    context = {
        'allocate_block': view_wd_block
    }

    return render(request, 'hostel/warden_allocation.html', context)


@login_required
def update_student_allocation_room(request, allocate_room_id):
    allocate_student_room = allocate_room.objects.get(pk=allocate_room_id)
    form = allocateRoomForm(request.POST or None, instance=allocate_student_room)
    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, " Student Allocation has been updated successful")

        return redirect('student-allocations')
    
    context = {
        'form':form,
    }

    return render(request, 'hostel/update_student_allocation.html', context)


@login_required
def delete_student_allocation_room(request, allocate_room_id):
    allocate_room_del = allocate_room.objects.get(pk=allocate_room_id)
    allocate_room_del.delete()
    return redirect('student-allocations')


@login_required
def update_warden_allocation(request, allocate_block_id):
    allocate_warden_block = allocate_block.objects.get(pk=allocate_block_id)
    form = allocateBlockForm(request.POST or None, instance=allocate_warden_block)
    if form.is_valid():
        form.save()
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, " Warden Allocation has been updated successfully")

        return redirect('warden-allocations')
    
    context = {
        'form':form,
    }

    return render(request, 'hostel/update_warden_allocation.html', context)


@login_required
def delete_warden_allocation(request, allocate_block_id):
    allocate_block_del = allocate_block.objects.get(pk=allocate_block_id)
    allocate_block_del.delete()
    return redirect('warden-allocations')