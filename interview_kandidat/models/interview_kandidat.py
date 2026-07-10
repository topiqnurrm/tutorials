from odoo import fields, models

class InterviewKandidat(models.Model):
    _name = "interview.kandidat"
    _description = "Penilaian Interview Kandidat"

    kandidat_name = fields.Char(string="Nama Kandidat", required=True)
    posisi_dilamar = fields.Char(string="Posisi yang Dilamar")
    interviewer_id = fields.Many2one("res.users", string="Interviewer")
    waktu_interview = fields.Date(string="Tanggal Interview", default=fields.Date.context_today)

    status = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("done", "Selesai Dinilai"),
            ("passed", "Lolos"),
            ("rejected", "Ditolak"),
        ],
        string="Status",
        default="draft",
    )

    data_ids = fields.One2many(
        "interview.kandidat.data", "evaluasi_id", string="Baris Kriteria Penilaian"
    )


class InterviewKandidatData(models.Model):
    _name = "interview.kandidat.data"
    _description = "Baris Kriteria Penilaian Interview"

    evaluasi_id = fields.Many2one(
        "interview.kandidat", string="Penilaian Interview"
    )
    kriteria = fields.Char(string="Kriteria", required=True)
    skor = fields.Integer(string="Skor (1-5)")
    catatan = fields.Char(string="Catatan")
