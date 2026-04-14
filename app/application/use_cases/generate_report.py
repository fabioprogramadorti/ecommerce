import os
import csv

class GenerateReportUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self):
        data = self.repo.get_report_data()

        # garantir pasta
        os.makedirs("reports", exist_ok=True)

        file_path = "reports/report.csv"

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["status", "total_pedidos", "valor_total"])

            formatted_data = []

            for row in data:
                status = row[0]
                total_pedidos = int(row[1])
                valor_total = float(row[2] or 0)

                writer.writerow([status, total_pedidos, valor_total])

                formatted_data.append({
                    "status": status,
                    "total_pedidos": total_pedidos,
                    "valor_total": valor_total
                })

        return formatted_data