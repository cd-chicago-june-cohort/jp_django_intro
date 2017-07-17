# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def index(request):
    
    if 'item_count' not in request.session:
        request.session['item_count'] = 0
    if 'cart_total' not in request.session:
        request.session['cart_total'] = 0.00
    return render(request, 'amadon_purchase/index.html')

#---------------------------------------------------------------------
#---------------------------------------------------------------------


def buy(request):
    if request.POST['button'] == 'sweatshirt':
        quantity = int(request.POST['quant_one'])
        request.session['item_count'] += quantity
        request.session['add_to_cart'] = (19.99 * quantity)
        request.session['cart_total'] += request.session['add_to_cart']
        return redirect('/checkout')
    elif request.POST['button'] == 'sweater':
        quantity = int(request.POST['quant_two'])
        request.session['item_count'] += quantity
        request.session['add_to_cart'] = (29.99 * quantity)
        request.session['cart_total'] += request.session['add_to_cart']
        return redirect('/checkout')
    elif request.POST['button'] == 'cup':
        quantity = int(request.POST['quant_three'])
        request.session['item_count'] += quantity
        request.session['add_to_cart'] = (4.99 * quantity)
        request.session['cart_total'] += request.session['add_to_cart']
        return redirect('/checkout')
    elif request.POST['button'] == 'book':
        quantity = int(request.POST['quant_four'])
        request.session['item_count'] += quantity
        request.session['add_to_cart'] = (49.99 * quantity)
        request.session['cart_total'] += request.session['add_to_cart']
        return redirect('/checkout')


#---------------------------------------------------------------------
#---------------------------------------------------------------------


def checkout(request):
    request.session['item_count_str'] = str(request.session['item_count'])
    request.session['add_to_cart_str'] = "$" + str(request.session['add_to_cart'])
    request.session['total_price'] = "$" + str(request.session['cart_total'])
    return render(request, 'amadon_purchase/checkout.html')