import java.util.Date;
import java.util.List;

public class SalesReportGenerator {
    private DatabaseConnection db;
    private Logger logger;
    private EmailService emailService;

    public SalesReportGenerator(DatabaseConnection db, Logger logger, EmailService emailService) {
        this.db = db;
        this.logger = logger;
        this.emailService = emailService;
    }

    public String generate(Date from, Date to) {
        StringBuilder sb = new StringBuilder();
        sb.append("=== SALES REPORT ===\n");
        sb.append("Period: " + from + " - " + to + "\n");

        List<Sale> data = db.query(
            "SELECT * FROM sales WHERE date BETWEEN ? AND ?", from, to);

        if (data.isEmpty()) {
            sb.append("No data\n");
            return sb.toString();
        }

        double total = 0;
        for (Sale s : data) {
            sb.append(s.getId() + ": " + s.getAmount() + "\n");
            total += s.getAmount();
        }

        sb.append("Total: " + total + "\n");

        logger.info("Sales report generated");
        emailService.send("manager@co.com", "Sales Report", sb.toString());

        return sb.toString();
    }
}
