# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
    _name = "manage.task"
    _description = "manage.task"

    name = fields.Char(
        string="Nombre", readonly=False, required=True, help="Introduzca el nombre"
    )
    description = fields.Text()
    nit = fields.Char()
    creation_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()
    sprint = fields.Many2one(
        "manage.sprint", ondelete="set null", help="Sprint relacionado"
    )
    technologies = fields.Many2many(
        comodel_name="manage.technology",
        relation_name="technologies_tasks",
        column1="task_id",
        column2="technology_id",
    )


class sprint(models.Model):
    _name = "manage.sprint"
    _description = "manage.sprint"

    name = fields.Char(string="Nombre")
    description = fields.Text()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    task = fields.One2many(
        comodel_name="manage.task", inverse_name="sprint", string="Tareas"
    )


class technology(models.Model):
    _name = "manage.technology"
    _description = "manage.technology"

    name = fields.Char(string="Nombre")
    description = fields.Text()
    photo = fields.Image(max_width=200, max_height=200)
    # tasks = fields.Many2many(
    #     model_name="manage.task",
    #     relation_name="technologies_tasks",
    #     column1="technology_id",
    #     column2="task_id",
    # )