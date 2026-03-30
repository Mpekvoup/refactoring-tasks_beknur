import java.util.Date;
import java.util.List;

public class SalesReportGenerator extends AbstractReportGenerator<Sale> {

    public SalesReportGenerator(DatabaseConnection db, ReportFormatter formatter, ReportHandler postProcessHandler) {
        super(db, formatter, postProcessHandler);
    }

    @Override
    protected String getTitle() {
        return "SALES REPORT";
    }

    @Override
    protected List<Sale> fetchData(Date from, Date to) {
        return db.query("SELECT * FROM sales WHERE date BETWEEN ? AND ?", from, to);
    }

    @Override
    protected String formatRow(Sale item) {
        return item.getId() + ": " + item.getAmount();
    }

    @Override
    protected String addSummary(List<Sale> data) {
        double total = 0;
        for (Sale s : data) {
            total += s.getAmount();
        }
        return "Total: " + total;
    }

    @Override
    protected String getRecipient() {
        return "manager@co.com";
    }
}
