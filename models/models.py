# -*- coding: utf-8 -*-

from odoo import models, fields, api

class casa(models.Model):
    _name = 'viv.casa'
    _description = 'mi segundo intento'

    # ATRIBUTOS DE LA CLASE 
    name = fields.Char("Nombre", required=True)
    description = fields.Text("Descripcion")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Fecha de Disponibilidad")
    expected_price = fields.Float("Precio Esperado")
    selling_price = fields.Float("Precio de Venta", default=0)
    bedrooms = fields.Integer("Cuartos", default=0)
    living_area = fields.Integer("Sala de Estar")
    facedes = fields.Integer("Fachada")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Jardin")
    garden_area = fields.Integer("Area del Jardin")
    garden_orientation = fields.Selection(selection=[("Izquierda", "Izq"), ("Derecha", "Der")])
    total_house = fields.Float("Ganancia", compute="set_total_houses")

    # DENTRO DE UN METODO LOS ATRIBUTOS SON VARIABLES
    # SELF ES UNA LLAMADA AL MISMO OBJETO 
    # PRIMERO ES EL CAMPO DEL OBJETO

    @api.depends('expected_price','selling_price')
    def set_total_houses(self):
        for record in self:
            record.total_house=record.expected_price-record.selling_price
            # record.update(
            #     {
            #         'total_house': record.expected_price-record.selling_price,
            #     }
            # )

# class fin(models.Model):
#     _name = 'fin.fin'
#     _description = 'fin.fin'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
