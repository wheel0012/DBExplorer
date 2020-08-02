from django.shortcuts import render, redirect
from django.http import HttpResponse
from influxdb import InfluxDBClient
from dbexplorer import settings

def index(request):
    client = InfluxDBClient(settings.INFLUXDB_HOST, settings.INFLUXDB_PORT)
    str = client.get_list_database()
    return HttpResponse(str)

def home(request):
    return redirect('polls/index/')
