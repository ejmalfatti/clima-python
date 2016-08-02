#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################################
# Obtiene informacion del clima
# Autor: Emanuel Malfatti 
# E-mail: ejmalfatti@outlook.com
# GitHub: https://ejmalfatti.github.io
# Licencia: GPLv3
##################################################################

from pyql.weather.forecast import Forecast
woeid = 91862968
forecast = Forecast.get(woeid=woeid, u="c")
ciudad = forecast.location.city
region = forecast.location.region
pais = forecast.location.country

#El siguiente bloque comentado, muestra el pronostico extendido
"""
print("Condiciones del clima para la ciudad de {0},{1}, {2}: \n".format(ciudad, region, pais))
for day in forecast.item.forecast:
    print("Fecha: {0} {1}".format(day['day'], day['date']))
    print("Pronóstico: {0} ({1})".format(day['text'], day['code']))
    print("Temperatura Mínima: {0}º {1}".format(day['low'], forecast.units.temperature))
    print("Temperatura Máxima: {0}º {1}".format(day['high'], forecast.units.temperature))
    print("*****************************************************************************")
"""
print("Condiciones del clima en {0},{1}, {2}.\n".format(ciudad, region, pais))
print("Fecha: {0}".format(forecast.item.condition.date))
print("Temperatura: {0}º {1}".format(forecast.item.condition.temp, forecast.units.temperature))
print("Condición: {0} ({1})".format(forecast.item.condition.text, forecast.item.condition.code))
