import java.util.Date;
import java.util.List;

public class InventoryReportGenerator extends AbstractReportGenerator<Item> {

    public InventoryReportGenerator(DatabaseConnection db, ReportFormatter formatter, ReportHandler postProcessHandler) {
        super(db, formatter, postProcessHandler);
    }

    @Override
    protected String getTitle() {
        return "INVENTORY REPORT";
    }

    @Override
    protected List<Item> fetchData(Date from, Date to) {
        return db.query("SELECT * FROM inventory WHERE updated BETWEEN ? AND ?", from, to);
    }

    @Override
    protected String formatRow(Item item) {
        return item.getName() + ": " + item.getStock() + " units";
    }

    @Override
    protected String addSummary(List<Item> data) {
        return "Generated at: " + new Date();
    }

    @Override
    protected String getRecipient() {
        return "warehouse@co.com";
    }
}
