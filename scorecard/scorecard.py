# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Scorecard(models.Model):
    _name='scorecard.info'
    _rec_name='sc_name'

    sc_name = fields.Char('Scorecard Name', required=True)
    department = fields.Many2one('hr.department', 'Department')
    superviser = fields.Many2one('hr.employee', 'Superviser')
    sc_date = fields.Date('Dated')
#    sc_id = fields.One2many('objective.info','sop_obj', string='Objectives')
    kpi_id = fields.One2many('individual.kpi','kpi_id1', string='Scorecard Type')


class individual_kpi(models.Model):
    _name='individual.kpi'

    kpi_id1 = fields.Many2one('scorecard.info', 'Element KPI')
    kpi_type = fields.Selection(
        [('not_started', '--Select Kpi type--'), ('departmental', 'DEPARTMENTAL'), ('personal', 'PERSONAL'), ],
        default='not_started')

    current_situation = fields.Char('Current Situation')
    gap = fields.Char('Benchmark-Gap')
    kpi = fields.Char('KPI')


    performance_indicator = fields.Selection(
        [('kno', 'KNOWLEDGE'), ('ski', 'SKILLS'), ('cre', 'CREATIVITY'), ('inv', 'INVOLVEMENT'), ('pri', 'PRIDE'),
         ('busimp', 'BUSINESS IMPROVEMENT'), ('not_started', '--Select performance-indicators--'), ],
        default='not_started',

        #string="Duration", required=True, compute='_return_measure_kpi'
    )

    benchmark_source = fields.Selection(
        [('worclaorg', 'WORLD-CLASS ORGS'), ('uni', 'UNIVERSITIES'), ('chatra', 'CHAMB. TRADE'), ('col', 'COLLEGES'),
         ('proinf', 'PROF. INST.'),
         ('lib', 'LIBRARY'), ('cons', 'CONSULTANTS'), ('int', 'INTERNET'), ],
        default='worclaorg')


    measure_kpi = fields.Selection(
        [
        #knowledge
        ('not_started', '--Select Measures--'),
        ('skites', 'SKILL TESTING'),
        ('edupro', 'EDUCATIONAL PROGRAMMES'),
        ('staapp', 'STAFF APPRAISAL'),
        #skills
        ('mulski', 'MULTI SKILLING'),
        ('trabud', 'TRAINING BUDGET'),
        ('cou', 'COURSES'),
        #creativity
        ('sug', 'SUGGESTIONS'),
        ('pro', 'PROJECTS'),
        ('inn', 'INNOVATION'),
        #involvement
         ('teawor', 'TEAM WORK'),
        ('pre', 'PRESENTATIONS'),
        ('selimp', 'SELF-IMPROVEMENT'),
        #pride
        ('abs', 'ABSENTEEISM'),
        ('sic', 'SICKNESS'),
        ('dis', 'DISPUTES'),
        ('labtur', 'LABOUR TURNOVER'),
        ('restojobadv', 'RESPONSE TO JOB ADVERTS'),
        #business involvement
        ('perimp', 'PERFORMANCE IMPROVEMENT'),
        ('scrred', 'SCRAP REDUCTION'),
        ('impdel', 'IMPROVED DELIVERY'),
        ('cuscom', 'CUSTOMER COMPLAINTS'),
        ('saflostimacc', 'SAFETY-LOST-TIME-ACCIDENTS')

         ],
        default='not_started')

    '''
    @api.multi
    @api.depends('performance_indicator')
    def _return_measure_kpi(self):
        if not self.performance_indicator:
            return
        if self.performance_indicator == 'kno':
            self.measure_kpi.selection = [
                ('not_started', '--Select Measures--'),
                ('skites', 'SKILL TESTING'),
                ('edupro', 'EDUCATIONAL PROGRAMMES'),
                ('staapp', 'STAFF APPRAISAL')
            ]

        elif self.performance_indicator == 'ski':
            self.measure_kpi = [
                ('skites', 'SKILL TESTING'),
                ('edupro', 'EDUCATIONAL PROGRAMMES'),
                ('staapp', 'STAFF APPRAISAL'),

            ]

'''




'''
    knowledge = fields.Selection(
        [('not_started', '--Select Measures--'), ('skites', 'SKILL TESTING'), ('edupro', 'EDUCATIONAL PROGRAMMES'),
         ('staapp', 'STAFF APPRAISAL'), ],
        default='not_started')

    skills = fields.Selection(
        [('not_started', '--Select Measures--'), ('mulski', 'MULTI-SKILLING'), ('trabud', 'TRAINING BUDGET'),
         ('cou', 'COURSES'), ],
        default='not_started')
    creativity = fields.Selection(
        [('not_started', '--Select Measures--'), ('sug', 'SUGGESTIONS'), ('pro', 'PROJECTS'), ('inn', 'INNOVATION'), ],
        default='not_started')
    involvement = fields.Selection(
        [('not_started', '--Select Measures--'), ('teawor', 'TEAM WORK'), ('pre', 'PRESENTATIONS'),
         ('selimp', 'SELF-IMPROVEMENT'), ],
        default='not_started')
    pride = fields.Selection(
        [('not_started', '--Select Measures--'), ('abs', 'ABSENTEEISM'), ('sic', 'SICKNESS'), ('dis', 'DISPUTES'),
         ('labtur', 'LABOUR TURNOVER'), ('restojobadv', 'RESPONSE TO JOB ADVERTS'), ],
        default='not_started')

    business_improvement = fields.Selection(
        [('not_started', '--Select Measures--'), ('perimp', 'PERFORMANCE IMPROVEMENT'), ('scrred', 'SCRAP REDUCTION'),
         ('impdel', 'IMPROVED DELIVERY'), ('cuscom', 'CUSTOMER COMPLAINTS'),
         ('saflostimacc', 'SAFETY-LOST-TIME-ACCIDENTS'),],
        default='not_started')
'''


    #   indicators = fields.One2many('performance.indicator', 'per_in', string='Indicators')

#class performance_indicators(models.Model):
#    _name ='performance.indicator'


#    per_in = fields.Many2one('individual.kpi','Performance Indicators')


'''
class ObjectiveInfo(models.Model):
		_name='objective.info'
		_rec_name = 'obj_name'

		obj_name = fields.Char('Objective')
		target = fields.Char('Benchmark')
		measure = fields.Char('Measure')
		emp_id = fields.Many2one('hr.employee','Responsible')
		obj_id = fields.One2many('objecive.sop','sop_id', string='Initiatives')
		sop_obj = fields.Many2one('scorecard.info','Title_select')

class ObjectiveSop(models.Model):
		_name = 'objecive.sop'
		_rec_name ='sop_id'
		sop_id = fields.Many2one('objective.info', 'Select_Objective')
		step_no = fields.Integer('Step No : ')
		steps = fields.Text(string='Initiatives')
   
'''