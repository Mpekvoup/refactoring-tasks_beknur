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
    private static class MockDatabaseConnection extends DatabaseConnection {
        @Override
        public List query(String sql, Object... params) {
            List<Item> items = new ArrayList<>();
            items.add(new Item("Widget", 100));
            items.add(new Item("Gadget", 50));
            return items;
        }
    }

    private static class EmptyMockDatabaseConnection extends DatabaseConnection {
        @Override
        public List query(String sql, Object... params) {
            return new ArrayList<>();
        }
    }

    private static class MockLogger extends Logger {
        @Override
        public void info(String message) {
            // Mock: ничего не делаем
        }
    }
}
