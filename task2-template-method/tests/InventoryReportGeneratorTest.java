import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.*;
import java.util.Date;
import java.util.List;
import java.util.ArrayList;

/**
 * Тесты для InventoryReportGenerator.
 */
public class InventoryReportGeneratorTest {

    private InventoryReportGenerator generator;
    private DatabaseConnection mockDb;
    private TextFormatter textFormatter;
    private LogHandler logHandler;

    @Before
    public void setUp() {
        mockDb = new MockDatabaseConnection();
        textFormatter = new TextFormatter();
        logHandler = new LogHandler(new MockLogger());
        generator = new InventoryReportGenerator(mockDb, textFormatter, logHandler);
    }

    @Test
    public void testGenerateInventoryReport() {
        Date from = new Date();
        Date to = new Date();

        String report = generator.generate(from, to);

        assertNotNull(report);
        assertTrue(report.contains("INVENTORY REPORT"));
        assertTrue(report.contains("units"));
    }

    @Test
    public void testEmptyInventory() {
        mockDb = new EmptyMockDatabaseConnection();
        generator = new InventoryReportGenerator(mockDb, textFormatter, logHandler);

        Date from = new Date();
        Date to = new Date();
        String report = generator.generate(from, to);

        assertTrue(report.contains("No data"));
    }

    // Mock классы
    private static class MockDatabaseConnection implements DatabaseConnection {
        @Override
        public <T> List<T> query(String sql, Date from, Date to) {
            List<Item> items = new ArrayList<>();
            items.add(new Item("Widget", 100));
            items.add(new Item("Gadget", 50));
            return (List<T>) items;
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
