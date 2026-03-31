import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.*;
import java.util.Date;
import java.util.List;
import java.util.ArrayList;

/**
 * Тесты для SalesReportGenerator.
 */
public class SalesReportGeneratorTest {

    private SalesReportGenerator generator;
    private DatabaseConnection mockDb;
    private TextFormatter textFormatter;
    private LogHandler logHandler;

    @Before
    public void setUp() {
        mockDb = new MockDatabaseConnection();
        textFormatter = new TextFormatter();
        logHandler = new LogHandler(new MockLogger());
        generator = new SalesReportGenerator(mockDb, textFormatter, logHandler);
    }

    @Test
    public void testGenerateSalesReport() {
        Date from = new Date();
        Date to = new Date();

        String report = generator.generate(from, to);

        assertNotNull(report);
        assertTrue(report.contains("SALES REPORT"));
        assertTrue(report.contains("Total"));
    }

    @Test
    public void testEmptyData() {
        mockDb = new EmptyMockDatabaseConnection();
        generator = new SalesReportGenerator(mockDb, textFormatter, logHandler);

        Date from = new Date();
        Date to = new Date();
        String report = generator.generate(from, to);

        assertTrue(report.contains("No data"));
    }

    @Test
    public void testTotalCalculation() {
        Date from = new Date();
        Date to = new Date();

        String report = generator.generate(from, to);

        assertTrue(report.contains("Total:"));
    }

    // Mock классы
    private static class MockDatabaseConnection implements DatabaseConnection {
        @Override
        public <T> List<T> query(String sql, Date from, Date to) {
            List<Sale> sales = new ArrayList<>();
            sales.add(new Sale(1, 100.0));
            sales.add(new Sale(2, 200.0));
            return (List<T>) sales;
        }
    }

    private static class EmptyMockDatabaseConnection implements DatabaseConnection {
        @Override
        public <T> List<T> query(String sql, Date from, Date to) {
            return new ArrayList<>();
        }
    }

    private static class MockLogger implements Logger {
        @Override
        public void info(String message) {
            // Mock: ничего не делаем
        }
    }
}
