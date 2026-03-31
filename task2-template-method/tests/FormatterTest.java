import org.junit.Test;
import static org.junit.Assert.*;
import java.util.Date;

/**
 * Тесты для различных форматтеров отчетов.
 */
public class FormatterTest {

    @Test
    public void testTextFormatter() {
        ReportFormatter formatter = new TextFormatter();
        Date from = new Date();
        Date to = new Date();

        String result = formatter.format("Test Report", from, to, "Content", "Summary");

        assertNotNull(result);
        assertTrue(result.contains("Test Report"));
        assertTrue(result.contains("Content"));
        assertTrue(result.contains("Summary"));
    }

    @Test
    public void testCsvFormatter() {
        ReportFormatter formatter = new CsvFormatter();
        Date from = new Date();
        Date to = new Date();

        String result = formatter.format("Test Report", from, to, "Row1\nRow2", "Total: 100");

        assertNotNull(result);
        assertTrue(result.contains("Test Report"));
        assertTrue(result.contains(","));  // CSV должен содержать запятые
    }

    @Test
    public void testHtmlFormatter() {
        ReportFormatter formatter = new HtmlFormatter();
        Date from = new Date();
        Date to = new Date();

        String result = formatter.format("Test Report", from, to, "Content", "Summary");

        assertNotNull(result);
        assertTrue(result.contains("<html>"));
        assertTrue(result.contains("</html>"));
        assertTrue(result.contains("Test Report"));
    }

    @Test
    public void testTextFormatterEmpty() {
        ReportFormatter formatter = new TextFormatter();
        Date from = new Date();
        Date to = new Date();

        String result = formatter.formatEmpty("Empty Report", from, to);

        assertTrue(result.contains("Empty Report"));
        assertTrue(result.contains("No data"));
    }
}
