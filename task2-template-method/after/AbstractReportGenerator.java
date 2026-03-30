import java.util.Date;
import java.util.List;

public abstract class AbstractReportGenerator<T> {
    protected DatabaseConnection db;
    protected ReportFormatter formatter;
    protected ReportHandler postProcessHandler;

    public AbstractReportGenerator(DatabaseConnection db, ReportFormatter formatter, ReportHandler postProcessHandler) {
        this.db = db;
        this.formatter = formatter;
        this.postProcessHandler = postProcessHandler;
    }

    public final String generate(Date from, Date to) {
        String title = getTitle();
        List<T> data = fetchData(from, to);

        if (data.isEmpty()) {
            return formatter.formatEmpty(title, from, to);
        }

        StringBuilder content = new StringBuilder();
        for (T item : data) {
            content.append(formatRow(item)).append("\n");
        }

        String summary = addSummary(data);
        String report = formatter.format(title, from, to, content.toString(), summary);

        if (postProcessHandler != null) {
            postProcessHandler.handle(report, getRecipient());
        }

        return report;
    }

    protected abstract String getTitle();
    protected abstract List<T> fetchData(Date from, Date to);
    protected abstract String formatRow(T item);
    protected abstract String addSummary(List<T> data);
    protected abstract String getRecipient();
}
