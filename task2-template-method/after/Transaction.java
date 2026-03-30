import java.util.Date;

public class Transaction {
    private Date date;
    private String description;
    private double amount;

    public Transaction(Date date, String description, double amount) {
        this.date = date;
        this.description = description;
        this.amount = amount;
    }

    public Date getDate() {
        return date;
    }

    public String getDescription() {
        return description;
    }

    public double getAmount() {
        return amount;
    }
}
