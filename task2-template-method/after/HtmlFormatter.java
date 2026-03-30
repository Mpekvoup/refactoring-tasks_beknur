import java.util.Date;

public class HtmlFormatter implements ReportFormatter {
    @Override
    public String format(String title, Date from, Date to, String content, String summary) {
        StringBuilder sb = new StringBuilder();
        sb.append("<html><body>\n");
        sb.append("<h1>").append(title).append("</h1>\n");
        sb.append("<p>Period: ").append(from).append(" - ").append(to).append("</p>\n");
        sb.append("<pre>").append(content).append("</pre>\n");
        sb.append("<p>").append(summary).append("</p>\n");
        sb.append("</body></html>\n");
        return sb.toString();
    }

    @Override
    public String formatEmpty(String title, Date from, Date to) {
        return "<html><body><h1>" + title + "</h1><p>Period: " + from + " - " + to + "</p><p>No data</p></body></html>";
    }
}
