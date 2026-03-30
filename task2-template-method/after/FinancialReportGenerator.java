import java.util.Date;
import java.util.List;

public class FinancialReportGenerator extends AbstractReportGenerator<Transaction> {

    public FinancialReportGenerator(DatabaseConnection db, ReportFormatter formatter, ReportHandler postProcessHandler) {
        super(db, formatter, postProcessHandler);
    }

    @Override
    protected String getTitle() {
        return "FINANCIAL REPORT";
    }

    @Override
    protected List<Transaction> fetchData(Date from, Date to) {
        return db.query("SELECT * FROM transactions WHERE date BETWEEN ? AND ?", from, to);
    }

    @Override
    protected String formatRow(Transaction item) {
        return item.getDate() + " - " + item.getDescription() + ": " + item.getAmount();
    }

    @Override
    protected String addSummary(List<Transaction> data) {
        double income = 0;
        double expense = 0;
        for (Transaction t : data) {
            if (t.getAmount() > 0) {
                income += t.getAmount();
            } else {
                expense += Math.abs(t.getAmount());
            }
        }
        return "Income: " + income + ", Expense: " + expense + ", Net: " + (income - expense);
    }

    @Override
    protected String getRecipient() {
        return "finance@co.com";
    }
}
