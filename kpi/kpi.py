
# -*- coding: utf-8 -*-
from openerp import models, fields

class ProjectInfo(models.Model):
    _name='project.info'

    proj_name = fields.Char('Project Name')
    proj_date = fields.Date('Start Date')
    proj_dated = fields.Date('Deadline')
    proj_ids = fields.One2many('project.tasks', 'task_id', string="Task")
    gl_id = fields.Many2one('goals', 'goal_id1')


class ProjectTask(models.Model):
    _name='project.tasks'
    task_name = fields.Char('Task Name')
    status = fields.Selection([('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ], default='not_started')
    objective_id=fields.One2many('objective.info','obj_id',string='Obejctive')
    task_id = fields.Many2one('project.info', ondelete='cascade', string="Project", required=True)
    sop_ids = fields.One2many('task.sop','sop_id', string="SOP")

class ObjectiveInfo(models.Model):
    _name='objective.info'
    obj_name= fields.Char('Objectives')
    target = fields.Char('Target')
    measure = fields.Char('Measure')
    emp_id = fields.Many2one('hr.employee','assigned_to')
    obj_id = fields.Many2one('project.tasks', 'Select_Task')

class TaskSop(models.Model):
    _name = 'task.sop'
    steps = fields.Text(string='SOPs')
    sop_id = fields.Many2one('project.tasks', 'Select_Tasks',)

class DepartmentInfo(models.Model):
    _name= 'department.info'
    dep_name = fields.Char('Department Name')
    department_id = fields.One2many('employee.info','dep_id', string='Department')
    gol_id = fields.One2many('goals','gol_id1',string='Dep')


class EmployeeInfo(models.Model):
    _name= 'employee.info'
    emp_name = fields.Char('Employee Name')
    #employee_id = fields.One2many('hr.employee','emp_id1', string='Employee')
    dep_id = fields.Many2one('department.info', 'Department')

class Goals(models.Model):
    _name = 'goals'
    goals = fields.Char('Goals')
    goal_id = fields.One2many('project.info','gl_id', string='Goals')
    gol_id1 = fields.Many2one('department.info','gol_id2')