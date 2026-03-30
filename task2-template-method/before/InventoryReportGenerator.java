import java.util.Date;
import java.util.List;

public class InventoryReportGenerator {
    private DatabaseConnection db;
    private Logger logger;
    private EmailService emailService;

    public InventoryReportGenerator(DatabaseConnection db, Logger logger, EmailService emailService) {
        this.db = db;
        this.logger = logger;
        this.emailService = emailService;
    }

    public String generate(Date from, Date to) {
        StringBuilder sb = new StringBuilder();
        sb.append("=== INVENTORY REPORT ===\n");
        sb.append("Period: " + from + " - " + to + "\n");

        List<Item> data = db.query(
            "SELECT * FROM inventory WHERE updated BETWEEN ? AND ?", from, to);

        if (data.isEmpty()) {
            sb.append("No data\n");
            return sb.toString();
        }

        for (Item i : data) {
            sb.append(i.getName() + ": " + i.getStock() + " units\n");
        }

        sb.append("Generated at: " + new Date() + "\n");

        logger.info("Inventory report generated");
        emailService.send("warehouse@co.com", "Inventory Report", sb.toString());

        return sb.toString();
    }
}
