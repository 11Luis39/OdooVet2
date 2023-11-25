# -*- coding: utf-8 -*-

 from odoo import models, fields, api

 class mascota(models.Model):
     _name = 'mascota.veterinaria'
     _description = 'mascota'

     name = fields.Char(string='name', required=True)
     edad = fields.Char(string='edad', required=True)
     color = fields.Char(string='color', required=True)
     type = fields.Selection([
                ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('otros', 'Otros')], string = 'type', default= "perro", required =  True
     )