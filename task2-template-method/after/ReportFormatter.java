import java.util.Date;

public interface ReportFormatter {
    String format(String title, Date from, Date to, String content, String summary);
    String formatEmpty(String title, Date from, Date to);
}
