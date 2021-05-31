from odoo import api, fields, models, _ 
import logging

_logger = logging.getLogger(__name__)

class reset_state_giro(models.Model):
    _inherit = 'vit.giro'

    @api.multi
    def reset_state(self):
        ref = self.name
        moves = self.env['account.move'].search( [ ( 'ref', '=', 'Payment giro '+ref ) ] )

        _logger.warning( moves )
        for move in moves:
            for move_line in move.line_ids:
                move_line.remove_move_reconcile()
            move.button_cancel()
            move.unlink()

        self.action_cancel()

