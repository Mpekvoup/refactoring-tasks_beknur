import java.util.Date;

public class TextFormatter implements ReportFormatter {
    @Override
    public String format(String title, Date from, Date to, String content, String summary) {
        StringBuilder sb = new StringBuilder();
        sb.append("=== ").append(title).append(" ===\n");
        sb.append("Period: ").append(from).append(" - ").append(to).append("\n");
        sb.append(content);
        sb.append(summary).append("\n");
        return sb.toString();
    }

    @Override
    public String formatEmpty(String title, Date from, Date to) {
        return "=== " + title + " ===\n" + "Period: " + from + " - " + to + "\n" + "No data\n";
    }
}
